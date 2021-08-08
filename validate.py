import requests
from pprint import pprint

def getType(list, type_value):
  return [{'lastLine': item['lastLine'], 
            'message': item['message'], 
            'extract': item["extract"]} for item in list if item['type'] == type_value ]

def groupMessages(list, primary_key):
  grouped = sorted(list, key=lambda k: k[primary_key])
  return grouped

def validate(siteURL, validator="https://validator.w3.org/nu/?out=json"):
  result = {}
  result['connect_fail'] = False
  response = None

  try:
    # grab site content
    response = requests.get(siteURL)
  except Exception as e: 
    result['connect_fail'] = True
    result['exception'] = repr(e)
    result['error'] = "Can't access website - check the spelling???"
    return result

  data = response.content
  
  headers = {
      "Content-Type": "text/html",
      "charset": "utf-8",
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36"
  }

  try:
    # send site content to validator with website content as body
    response = requests.post(validator, data=data, headers=headers)
  except requests.exceptions.RequestException as e: 
    result['hasErrors'] = True
    result['exception'] = repr(e)
    result['error'] = "OOPS - couldn't connect to validator. Try again later."
    return result
  else:   
    data = response.json()

    messages = data["messages"]

    # result['messages'] = sorted(messages, key = lambda k: (k['type'],k['lastLine']) )
    result['errors'] = groupMessages(getType(messages, 'error'), 'message')
    result['warnings'] = groupMessages(getType(messages, 'info'), 'message')
    result['num_errors'] = len(result['errors'])
    result['num_warnings'] = len(result['warnings'])

    print("ERRORS")
    # print(result['errors'])
    
 
    data = result['errors']

    # for key, group in groupby(data, key="message"):
    #   print(key,": ",list(group))
     
  
    


    # print(len(result['errors'])," ERRORS:")
    # pprint(result['errors'])
    # print(len(result['warnings'])," WARNINGS:")
    # pprint(result['warnings'])
    return result 

if __name__ == '__main__':
  validate('https://lds.org')
