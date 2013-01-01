function getInitialPostsContent() {
	var xmlhttp;
	xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
		if (xmlhttp.readyState==4 && xmlhttp.status==200) {
			if (xmlhttp.responseText!=="") {
				 constructInitialPostsContent(xmlhttp.responseText);
			}		
		}

	};
	xmlhttp.open("GET","http://127.0.0.1:8000/~paradigm72/HTMLScraper/getPosts",true);
	xmlhttp.send();
}

function constructInitialPostsContent(rawText) {
	targetDiv = document.getElementById("targetDiv");
	targetDiv.innerHTML = rawText;
	//set up timer to call getNextPostContent()
	setTimeout(getNextPostContent(), 2000);
	
}

function getNextPostContent() {
		
	//call AJAX request to get individual post contents
	var xmlhttp;
	xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
		if (xmlhttp.readyState==4 && xmlhttp.status==200) {
			if (xmlhttp.responseText!=="") {
				constructNextPostContent(xmlhttp.responseText,$(".futureURL").attr("ID"));
			}
		}
	};
	xmlhttp.open("GET",
				 "http://127.0.0.1:8000/~paradigm72/HTMLScraper/getPostContents/"+
				 		$(".futureURL").attr("ID"),
				 true);
	xmlhttp.send();
}

function constructNextPostContent(rawText,elementID) {
	//find the element, replace its innerHTML
	$(".futureURL").innerHTML = rawText;
	$(".futureURL").className = "usedURL";
	//squash its ID/class
	
	//setup timer to the next iteration
	setTimeout(getNextPostContent(), 10000);
}