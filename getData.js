function getInitialPostsContent() {
	xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
		if (xmlhttp.readyState==4 && xmlhttp.status==200) {
			if (xmlhttp.responseText!="") {
				 constructInitialPostsContent(xmlhttp.responseText);
			}		
		}

	}
	xmlhttp.open("GET","http://127.0.0.1:8000/~paradigm72/HTMLScraper/getPosts",true);
	xmlhttp.send();
}

function constructInitialPostsContent(rawText) {
	targetDiv = document.getElementById("targetDiv")
	targetDiv.innerHTML = rawText;
	//set up timer to call getNextPostContent()
	setTimeout(getNextPostContent(), 2000)
	
}

function getNextPostContent() {
	//find the next <span> with class "futurePost"
	nextFutureSpan = nextInDOM($('body'),$('#futureURL'))
	
	//call AJAX request to get individual post contents
	xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
		if (xmlhttp.readyState==4 && xmlhttp.status==200) {
			if (xmlhttp.responsetext!="") {
				constructNextPostContent(xmlhttp.responseText,elementID);
			}
		}
	}
	xmlhttp.open("GET","http://127.0.0.1:8000/~paradigm72/HTMLScraper/getPostContents/"+thisElement.getAttribute("ID"),true);
	xmlhttp.send;
}

function constructNextPostContent(rawText,elementID) {
	//find the element
	//replace its innerHTML
	//squash its ID/class
	
	//setup timer to the next iteration
}