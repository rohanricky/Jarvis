document.getElementById("input1").addEventListener('keypress',(event)=>{
  if(event.key=="Enter"){
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET","http://jarvis-messenger-pa.herokuapp.com/webhook",true)
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    json = {
	"name":"do the work here"
    }
    xhttp.send(json);
  }
})
