from bs4 import BeautifulSoup
import urllib2,urllib
import re

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


def getOnePostFullContents(local_href):
    html_doc = getFullHTML("http://www.ndnation.com/boards/"+local_href)
    soup = BeautifulSoup(html_doc)
    postBody = soup.find(id='PostBody')
    return postBody

def addOnePostFullContentsToResponse(responseSoFar,showPostLink):
    postBody = getOnePostFullContents(showPostLink['href'])
    #weird hack to get string index 2, not sure of the right syntax
    i = 1
    responseSoFar += "<div class=""postBody"">"  #start a new div to style the post contents
    for string in postBody.strings:
        if i==2:
            if len(string) > 0:
                responseSoFar += string
        i += 1
    responseSoFar += "</div>"
    return responseSoFar


def getAllPosts(html_doc):
    soup = BeautifulSoup(html_doc)
    response = ""
    postCounter = 0
    subsequentThread = False

    for showPostLink in soup.find_all(href=re.compile('showpost.*this')):
        #if this post is 4 levels under a "font", it's a thread title so start a new thread div
        if showPostLink.parent.parent.parent.parent.name=="font":
            if subsequentThread==True:
                response += "</div>"
            else:
                subsequentThread=True
            response += "<div class=""thread"">"
        else:
            response += "<br>"   #new line only if this *isn't* the first post in the thread

        #print the post title
        response += showPostLink.string

        ### BELOW CODE IS TO GET THE FULL POST TEXT - VERY SLOW AND EXPENSIVE, SO LIMITING TO 10 FOR NOW
        if not "*" in showPostLink.string:  #if this post has any content,
            if postCounter <= 10:
                response = addOnePostFullContentsToResponse(response,showPostLink)
            else:
                response += "<span class=""futureURL"" id="""+urllib.quote_plus(showPostLink['href'])+"""></span>"""
            postCounter += 1


    response += "</div>"
    return response


#print soupify(getFullHTML("http://www.ndnation.com/boards/index.php?football"))