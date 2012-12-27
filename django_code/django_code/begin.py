import html_core
from django.http import HttpResponse
import crossdomain_middleware


def getPosts(request):
    # add cross-site headers to request - not currently implemented
    #request = middleware.XsSharing.process_request(request=request)

    response_string=html_core.getAllPosts(html_core.getFullHTML("http://www.ndnation.com/boards/index.php?football"))
    myResponseObj = HttpResponse(response_string,mimetype='text/plain',status=200)

    # add cross-site headers to response
    myResponseObj = crossdomain_middleware.process_response(request,myResponseObj)
    return myResponseObj



def getIndividualPost(request,href):
    response_string = html_core.getOnePostFullContents(href)
    myResponseObj = HttpResponse(response_string,mimetype='text/plain',status=200)

    # add cross-site headers to response
    myResponseObj = crossdomain_middleware.process_response(request,myResponseObj)
    return myResponseObj



#debug
#soupify(getFullHTML("http://www.ndnation.com/boards/index.php?football"))

