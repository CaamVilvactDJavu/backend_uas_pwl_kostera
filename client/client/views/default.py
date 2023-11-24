from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name="home", renderer="json")
def kost(request):
    return Response(json_body={"message": "Hello World!"})
