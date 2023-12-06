import grpc

import client.grpc.auth_pb2 as auth_pb2
import client.grpc.auth_pb2_grpc as auth_pb2_grpc


class AuthClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 6000
        self.service_path = "/api/v1/auth/"

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = auth_pb2_grpc.AuthServiceStub(self.channel)

    def register_user(self, username, password, role):
        response = self.stub.RegisterUser(
            auth_pb2.UserRequest(
                username=username,
                password=password,
                role=role,
            )
        )
        return dict(message=response.message, token=response.token)

    def admin_login(self, username, password):
        response = self.stub.AdminLogin(
            auth_pb2.UserRequest(
                username=username,
                password=password,
            )
        )
        return dict(
            message=response.message,
            token=response.token,
            roles=response.roles if response.roles else [],
        )

    def login_user(self, username, password, role):  # Make sure role is optional
        response = self.stub.LoginUser(
            auth_pb2.UserRequest(
                username=username,
                password=password,
                role=role,
            )
        )
        return dict(message=response.message, token=response.token)

    def verify_token(self, token):
        response = self.stub.VerifyToken(auth_pb2.TokenRequest(token=token))
        return dict(
            message=response.message, valid=response.valid, roles=response.roles
        )
