//global flag to stop execution the next time we get to a readystatechange
var stopRequestsOnNextReturn;

function getInitialPostsContent() {
	//clear stop flag, if it was set
	stopRequestsOnNextReturn = false;
	
	var xmlhttp;
	xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
		if (xmlhttp.readyState==4 && xmlhttp.status==200) {
			if (xmlhttp.responseText!=="") {
				 constructInitialPostsContent(xmlhttp.responseText);
			}
		}
    };
	xmlhttp.open("GET","http://127.0.0.1:8000/~paradigm72/HTMLScraper/getPosts/",true);
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
	$(".futureURL").first().html(rawText);
	
	//squash its class marker
	$(".futureURL").first().addClass("usedURL");
	$(".futureURL").first().removeClass("futureURL");
	
	//set up timer to the next iteration
	if (!stopRequestsOnNextReturn) {
		setTimeout(getNextPostContent(), 10000);	
	}	
}

function stopRequests() {
	stopRequestsOnNextReturn = true;
}