messages = [
  {'type': 'error', 'lastLine': 207, 'lastColumn': 538, 'message': 'No space between attributes.', 'extract': 'ple-touch-icon"sizes="180x180"', 'hiliteStart': 15, 'hiliteLength': 1}, 
  {'type': 'error', 'lastLine': 207, 'lastColumn': 553, 'message': 'No space between attributes.', 'extract': 'sizes="180x180"href="/apple-to', 'hiliteStart': 15, 'hiliteLength': 1}, 
  {'type': 'error', 'lastLine': 208, 'lastColumn': 17, 'message': 'No space between attributes.', 'extract': 'link rel="icon"type="image/png', 'hiliteStart': 15, 'hiliteLength': 1}, 
  {'type': 'error', 'lastLine': 208, 'lastColumn': 33, 'message': 'No space between attributes.', 'extract': 'ype="image/png"href="/favicon-', 'hiliteStart': 15, 'hiliteLength': 1}, 
  {'type': 'error', 'lastLine': 209, 'lastColumn': 17, 'message': 'No space between attributes.', 'extract': 'link rel="icon"type="image/png', 'hiliteStart': 15, 'hiliteLength': 1}, 
  {'type': 'error', 'lastLine': 209, 'lastColumn': 33, 'message': 'No space between attributes.', 'extract': 'ype="image/png"href="/favicon-', 'hiliteStart': 15, 'hiliteLength': 1}, 
  {'type': 'info', 'lastLine': 383, 'lastColumn': 99, 'firstColumn': 1, 'subType': 'warning', 'message': 'The “type” attribute is unnecessary for JavaScript resources.', 'extract': '</script>\n<script type="application/javascript" src="//script.crazyegg.com/pages/scripts/0053/5042.js" async></scri', 'hiliteStart': 10, 'hiliteLength': 99}, 
  {'type': 'info', 'lastLine': 384, 'lastColumn': 52, 'firstColumn': 1, 'subType': 'warning', 'message': 'The “type” attribute is unnecessary for JavaScript resources.', 'extract': "</script>\n<script type='text/javascript' data-cfasync='false'>window", 'hiliteStart': 10, 'hiliteLength': 52}, 
  {'type': 'error', 'lastLine': 392, 'lastColumn': 65, 'message': 'No space between attributes.', 'extract': '="display:none"class="icons-ma', 'hiliteStart': 15, 'hiliteLength': 1}, 
  {'type': 'error', 'lastLine': 510, 'lastColumn': 31, 'message': 'No space between attributes.', 'extract': '"icon-unfollow"viewBox="0 0 13', 'hiliteStart': 15, 'hiliteLength': 1}, 
  {'type': 'error', 'lastLine': 608, 'lastColumn': 68, 'firstColumn': 9, 'message': 'Bad value “bullet/chevron” for attribute “id” on element “g”: Not a valid XML 1.0 name.', 'extract': '>\n        <g id="bullet/chevron" stroke-width="1" fill-rule="evenodd">\n     ', 'hiliteStart': 10, 'hiliteLength': 60}, 
  {'type': 'error', 'lastLine': 614, 'lastColumn': 65, 'firstColumn': 9, 'message': 'Bad value “bullet/dash” for attribute “id” on element “g”: Not a valid XML 1.0 name.', 'extract': '>\n        <g id="bullet/dash" stroke-width="1" fill-rule="evenodd">\n     ', 'hiliteStart': 10, 'hiliteLength': 57}, 
  {'type': 'error', 'lastLine': 665, 'lastColumn': 7, 'firstColumn': 1, 'message': 'Stray end tag “head”.', 'extract': '>\n</svg>\n\n</head>\n\n\n<bo', 'hiliteStart': 10, 'hiliteLength': 7}, 
  {'type': 'error', 'lastLine': 673, 'firstLine': 668, 'lastColumn': 1, 'message': 'Start tag “body” seen but an element of the same type was already open.', 'extract': '</head>\n\n\n<body class="Page-body  header-large"\n    \n\n\n\n>\n    \n', 'hiliteStart': 10, 'hiliteLength': 47}, 
  {'type': 'error', 'lastLine': 673, 'firstLine': 668, 'lastColumn': 1, 'subType': 'fatal', 'message': 'Cannot recover after last error. Any further errors will be ignored.', 'extract': '</head>\n\n\n<body class="Page-body  header-large"\n    \n\n\n\n>\n    \n', 'hiliteStart': 10, 'hiliteLength': 47}
]

sort = sorted(messages, key = lambda k: (k['type'],k['lastLine']) )
for item in sort:
  print(item['type'],": line ", item['lastLine'])

print("ERRORS\n",[(item['lastLine'], item['message'], item["extract"]) for item in sort if item['type'] == 'error'])
print("\n\nWARNINGS\n",[(item['lastLine'], item['message'], item['extract']) for item in sort if item['type'] == 'info'])
