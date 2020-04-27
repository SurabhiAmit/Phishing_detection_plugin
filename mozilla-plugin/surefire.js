var currentURL = window.location.href
var postData = {"url": currentURL}
const Http = new XMLHttpRequest();
const url = 'http://localhost:9000/scanurl';
Http.open("POST", url);
Http.setRequestHeader("Content-type", "application/json");
Http.onload = function (){
  data = JSON.parse(Http.responseText)
  var safe = false
  if (data["finalSureFireScore"] <= 0.6){
    safe = true
  }
  if (safe != true){
    html = document.getElementsByTagName("html")[0]
    html.innerHTML = "<body bgcolor='red' align='center'><h1>This is Phishing Website</h1></body>"
  }
}
console.log(JSON.parse(JSON.stringify(postData))["url"])
Http.send(JSON.stringify(postData));
