import html_core
from django.http import HttpResponse
import crossdomain_middleware


def getPosts(request):
    # add cross-site headers to request
    #request = middleware.XsSharing.process_request(request=request)

    response_string=html_core.soupify(html_core.getFullHTML("http://www.ndnation.com/boards/index.php?football"))
    myResponse = HttpResponse(response_string,mimetype='text/plain',status=200)

    # add cross-site headers to response
    myResponse = crossdomain_middleware.process_response(request,myResponse)

    return myResponse
    #return ""

#soupify(getFullHTML("http://www.ndnation.com/boards/index.php?football"))

