import pytest
from unittest.mock import MagicMock
from client.grpc.authClient import AuthClient
import client.grpc.auth_pb2 as auth_pb2


@pytest.fixture
def auth_client():
    return AuthClient()


def test_register_user(auth_client):
    # Mock the RegisterUser RPC call
    auth_client.stub.RegisterUser = MagicMock()
    auth_client.stub.RegisterUser.return_value = auth_pb2.RegisterResponse(
        message="Success", token="xyz")

    # Perform the test
    result = auth_client.register_user("test_user", "password123", "user")

    # Assertions
    auth_client.stub.RegisterUser.assert_called_once_with(
        auth_pb2.UserRequest(username="test_user",
                             password="password123", role="user")
    )
    assert result == {"message": "Success", "token": "xyz"}


def test_admin_login(auth_client):
    auth_client.stub.AdminLogin = MagicMock()
    auth_client.stub.AdminLogin.return_value = auth_pb2.AdminLoginResponse(
        message="Success", token="xyz", roles=["admin"])

    result = auth_client.admin_login("admin_user", "admin_password")

    auth_client.stub.AdminLogin.assert_called_once_with(
        auth_pb2.UserRequest(username="admin_user", password="admin_password")
    )
    assert result == {"message": "Success", "token": "xyz", "roles": ["admin"]}


def test_login_user(auth_client):
    auth_client.stub.LoginUser = MagicMock()
    auth_client.stub.LoginUser.return_value = auth_pb2.LoginResponse(
        message="Success", token="xyz")

    result = auth_client.login_user("test_user", "password123", "user")

    auth_client.stub.LoginUser.assert_called_once_with(
        auth_pb2.UserRequest(username="test_user",
                             password="password123", role="user")
    )
    assert result == {"message": "Success", "token": "xyz"}


def test_verify_token(auth_client):
    auth_client.stub.VerifyToken = MagicMock()
    auth_client.stub.VerifyToken.return_value = auth_pb2.VerifyTokenResponse(
        message="Success", valid=True, roles=["user"])

    result = auth_client.verify_token("xyz_token")

    auth_client.stub.VerifyToken.assert_called_once_with(
        auth_pb2.TokenRequest(token="xyz_token"))
    assert result == {"message": "Success", "valid": True, "roles": ["user"]}
