from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UserRequest(_message.Message):
    __slots__ = ["username", "password", "role"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    role: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., role: _Optional[str] = ...) -> None: ...

class RegisterResponse(_message.Message):
    __slots__ = ["message", "token"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    message: str
    token: str
    def __init__(self, message: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ["message", "token", "role"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    message: str
    token: str
    role: str
    def __init__(self, message: _Optional[str] = ..., token: _Optional[str] = ..., role: _Optional[str] = ...) -> None: ...

class AdminLoginResponse(_message.Message):
    __slots__ = ["message", "token", "role", "roles"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    message: str
    token: str
    role: _containers.RepeatedScalarFieldContainer[str]
    roles: str
    def __init__(self, message: _Optional[str] = ..., token: _Optional[str] = ..., role: _Optional[_Iterable[str]] = ..., roles: _Optional[str] = ...) -> None: ...

class TokenRequest(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class VerifyTokenResponse(_message.Message):
    __slots__ = ["message", "valid", "roles"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    VALID_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    message: str
    valid: bool
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, message: _Optional[str] = ..., valid: bool = ..., roles: _Optional[_Iterable[str]] = ...) -> None: ...
