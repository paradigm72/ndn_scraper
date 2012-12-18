from bs4 import BeautifulSoup
from django.http import HttpResponse
import  urllib2
import re
import crossdomain_middleware

def getFullHTML(url):
    htmlBody = ""
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req)
    while 1:
        data = fd.read(1024)
        if not len(data):
            break
        htmlBody += data
    return htmlBody


def getPostFullContents(href):
    html_doc = getFullHTML(href)
    soup = BeautifulSoup(html_doc)
    postBody = soup.find(id='PostBody')
    return postBody


def soupify(html_doc):
    soup = BeautifulSoup(html_doc)
    response = ""

    for showPostLink in soup.find_all(href=re.compile('showpost.*this')):
        #if this post is 4 levels under a "font", it's a thread title so put a space before it
        if showPostLink.parent.parent.parent.parent.name=="font":
           response += "<br>"

        #print the post title
        response += "<br>"+"##"+showPostLink.string
        #postBody = getPostFullContents("http://www.ndnation.com/boards/"+showPostLink['href'])


        #weird hack to get string index 2, not sure of the right syntax
        #if not "*" in showPostLink.string:
        #    i = 1
        #    for string in postBody.strings:
        #        if i==2:
        #            if len(string) > 0:
        #                print string
        #        i += 1
    return response

def getPosts(request):
    # add cross-site headers to request
    #request = middleware.XsSharing.process_request(request=request)

    response_string=soupify(getFullHTML("http://www.ndnation.com/boards/index.php?football"))
    myResponse = HttpResponse(response_string,mimetype='text/plain',status=200)

    # add cross-site headers to response
    myResponse = crossdomain_middleware.process_response(request,myResponse)

    return myResponse
    #return ""

#soupify(getFullHTML("http://www.ndnation.com/boards/index.php?football"))
