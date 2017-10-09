from bs4 import BeautifulSoup
import urllib2,urllib
import re

def _getFullHTML(url):
    htmlBody = ""
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req)
    while 1:
        data = fd.read(1024)
        if not len(data):
            break
        htmlBody += data
    return htmlBody


def _getOnePostFullContents(local_href):
    html_doc = _getFullHTML("http://www.ndnation.com/boards/"+local_href)
    soup = BeautifulSoup(html_doc)
    postBody = soup.find(id='PostBody')
    #weird hack to get string index 2, not sure of the right syntax
    i = 1
    postBodySanitized = "<br><span class=""postBody"">"  #start a new span to style the post contents
    for string in postBody.strings:
        if i==2:
            if len(string) > 0:
                postBodySanitized += string
        i += 1
        print string['href']
    postBodySanitized += "</span>"
    return postBodySanitized

def _addOnePostFullContentsToResponse(responseSoFar,showPostLink):
    responseSoFar += _getOnePostFullContents(showPostLink['href'])
    return responseSoFar


def _getAllPosts(html_doc):
    print "got into _getAllPosts"

    soup = BeautifulSoup(html_doc)
    response = ""
    postCounter = 0
    subsequentThread = False

    for showPostLink in soup.find_all(href=re.compile('showpost.*this')):
        #if this post is part of a ThreadPrime span, it's the first in a thread so start a new thread div
        if showPostLink.parent.get("class")[0]==unicode("ThreadPrime"):
            # print "condition matched!"
            if subsequentThread==True:
                response += "</div>"
            else:
                subsequentThread=True
            response += "<div class=""thread"">"
        else:
            response += "<br>"   #new line only if this *isn't* the first post in the thread

        #print the post title
        response += showPostLink.string

        #if this post has any content, tag it for future retrieval (separate AJAX request)
        if not "*" in showPostLink.string:
           response += "<span class=""futureURL"" id="""+urllib.quote_plus(showPostLink['href'])+"""></span>"""


    response += "</div>"
    return response


##print soupify(getFullHTML("http://www.ndnation.com/boards/index.php?football"))
##print getOnePostFullContents("showpost.php?b=football;pid=421237;d=this")