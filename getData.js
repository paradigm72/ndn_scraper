function doAjax() {
	xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
		if (xmlhttp.readyState==4 && xmlhttp.status==200) {
			if (xmlhttp.responseText!="") {
				 constructPostContent(xmlhttp.responseText);
			}		
		}

	}
	xmlhttp.open("GET","http://127.0.0.1:8000/~paradigm72/HTMLScraper/getPosts",true);
	xmlhttp.send();
}

function constructPostContent(rawText) {
	targetDiv = document.getElementById("targetDiv")
	targetDiv.innerHTML = rawText;
	
}