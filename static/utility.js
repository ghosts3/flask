document.querySelector("#submit-url").addEventListener("submit", function () {
  this.querySelector("input[type=submit]").disabled = true;
  this.querySelector(".loader").style.display = "block";
  return true;
});
