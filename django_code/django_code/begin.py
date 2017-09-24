import html_core
from django.http import HttpResponse
import crossdomain_response


def getPosts(request):
    # add cross-site headers to request - not currently implemented
    # response_string = crossdomain_response.process_request(request=request)

    response_string = html_core.getAllPosts(html_core.getFullHTML("http://www.ndnation.com/boards/index.php?football"))
    myResponseObj = HttpResponse(response_string,mimetype='text/plain',status=200)

    # add cross-site headers to response
    myResponseObj = crossdomain_response.process_response(request,myResponseObj)
    return myResponseObj



def getIndividualPost(request,href):
    try:
        response_string = html_core.getOnePostFullContents(href)
    except:
        response_string = ""
        print "Error in getOnePostFullContents"
    finally:
        myResponseObj = HttpResponse(response_string,mimetype='text/plain',status=200)
        # add cross-site headers to response
        myResponseObj = crossdomain_response.process_response(request,myResponseObj)
        return myResponseObj



#debug
#soupify(getFullHTML("http://www.ndnation.com/boards/index.php?football"))

