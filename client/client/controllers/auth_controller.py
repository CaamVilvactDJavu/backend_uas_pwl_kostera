from pyramid.view import view_config, view_defaults
from pyramid.response import Response
from client.grpc.authClient import AuthClient


@view_defaults(route_name="auth", renderer="json")
class AuthView:
    def __init__(self, request):
        self.request = request
        self.auth_client = AuthClient()

    @view_config(route_name="register", request_method="POST")
    def register_user(self):
        try:
            result = self.auth_client.register_user(
                username=self.request.json_body.get("username"),
                password=self.request.json_body.get("password"),
            )
            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(route_name="login", request_method="POST")
    def login_user(self):
        try:
            result = self.auth_client.login_user(
                username=self.request.json_body.get("username"),
                password=self.request.json_body.get("password"),
            )
            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(route_name="verify", request_method="POST")
    def verify_token(self):
        try:
            result = self.auth_client.verify_token(
                token=self.request.json_body.get("token"),
            )
            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)
