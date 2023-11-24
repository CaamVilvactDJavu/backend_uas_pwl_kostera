from pyramid.view import notfound_view_config
from pyramid.response import Response


@notfound_view_config(renderer="json")
def notfound_view(request):
    return Response(json_body={"message": "Not Found"}, status=404)
