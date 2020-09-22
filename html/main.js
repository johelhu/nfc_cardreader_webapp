
if (typeof(Worker) !== "undefined") {
    // Yes! Web worker support!
    console.log("Web Worker soportado");
} else {
    // Sorry! No Web Worker support..
    console.log("Web Worker no soportado");
} 

var greeting_str = "Iniciando la herramienta";

//alert(greeting_str);

console.log("Mensaje en consola");
console.log("Holaaaaaasdasdasd");

var table = document.getElementById("tabla");

//console.log(table);

function sleep(ms) {
    var unixtime_ms = new Date().getTime();
    while(new Date().getTime() < unixtime_ms + ms) {}
}

function renovar () {
    var arrayData = new Array();
    var archivoTxt = new XMLHttpRequest();
    var filePath = './ingreso.log.txt';
    
    archivoTxt.open("GET", filePath, false);
    archivoTxt.send(null);

    var txt = archivoTxt.responseText;
    var txt_html = "";

    var tmp = "";
    for (var i = 0; i < txt.length; i++ )
    {
	//arrayData.push(txt[i]);
	//console.log(i);
	//console.log(txt[i]);

	tmp = tmp + txt[i]
	
	if (txt[i] == '\n' ){
	    console.log(tmp);
	    //alert(tmp);
	    console.log("NUEVA LINEA");
	    arrayData.push("<br>"+tmp+"</br>");
	    //txt_html += "<br>"+tmp+"</br>";
	    tmp = "";
	}
	
    }

    //table.innerHTML = txt_html;

    var temporal;
    for ( var i = 1; i < 10; i++)
    {
	temporal = arrayData[arrayData.length -i];
	txt_html +=  temporal;
	console.log("Hola");
	console.log(temporal);
    }


    table.innerHTML = txt_html;
    //postMessage(txt_html);
}

while(true){    
    renovar();
    sleep(50);
}

//setInterval(renovar(), 500);
