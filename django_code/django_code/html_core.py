from bs4 import BeautifulSoup
import urllib2
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


def getPostFullContents(href):
    html_doc = getFullHTML(href)
    soup = BeautifulSoup(html_doc)
    postBody = soup.find(id='PostBody')
    return postBody

def addPostFullContents(responseSoFar,showPostLink):
    postBody = getPostFullContents("http://www.ndnation.com/boards/"+showPostLink['href'])
    #weird hack to get string index 2, not sure of the right syntax
    if not "*" in showPostLink.string:
        i = 1
        for string in postBody.strings:
            if i==2:
                if len(string) > 0:
                    responseSoFar += "<br>;nbsp;nbsp"+string
            i += 1
    return responseSoFar

def soupify(html_doc):
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

        ### BELOW CODE IS TO GET THE FULL POST TEXT - VERY SLOW AND EXPENSIVE
        if postCounter <= 10:
            addPostFullContents(response,showPostLink)
            postCounter += 1

    response += "</div>"
    return response