document.addEventListener('DOMContentLoaded',domloaded,false);
function domloaded(){
    const vers = " v14";
    console.log("in consol+" + vers);
    // jQuery methods go here...
    document.getElementById("div1").innerHTML = "Hello JavaScript!";
    
    //https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API
    //rectangle vert 
    const canvas1 = document.getElementById("canvas");
    const ctx1 = canvas1.getContext("2d");
    
    ctx1.fillStyle = "green";
    ctx1.fillRect(10, 10, 150, 100);
    
    
    //canevas 3 :
    var c3 = document.getElementById("myCanvas3");
    const c33 = document.getElementById("myCanvas3");

    var ctx3 = c3.getContext("2d");
    const ctx33= c33.getContext("2d");

    ctx3.moveTo(0, 0);
    ctx3.lineTo(200, 100);
    ctx3.stroke();

    document.getElementById("loopstopid2").onclick = function() {
	//https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_onclick_dom
	stoploop();
    };
    function stoploop(){
	var c4 = document.getElementById("stopscreen2");
	c4.innerHTML = "stopped";
    }
}


