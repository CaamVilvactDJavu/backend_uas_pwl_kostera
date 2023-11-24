from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Kost(_message.Message):
    __slots__ = ["id", "name", "price", "specification", "rule", "address", "facility", "image_url"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FACILITY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    price: float
    specification: str
    rule: str
    address: str
    facility: str
    image_url: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., price: _Optional[float] = ..., specification: _Optional[str] = ..., rule: _Optional[str] = ..., address: _Optional[str] = ..., facility: _Optional[str] = ..., image_url: _Optional[str] = ...) -> None: ...

class KostListResponse(_message.Message):
    __slots__ = ["kosts", "message"]
    KOSTS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    kosts: _containers.RepeatedCompositeFieldContainer[Kost]
    message: str
    def __init__(self, kosts: _Optional[_Iterable[_Union[Kost, _Mapping]]] = ..., message: _Optional[str] = ...) -> None: ...

class KostListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class KostRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class KostResponse(_message.Message):
    __slots__ = ["kost", "message"]
    KOST_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    kost: Kost
    message: str
    def __init__(self, kost: _Optional[_Union[Kost, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class KostCreateRequest(_message.Message):
    __slots__ = ["name", "price", "specification", "rule", "address", "facility", "image_url"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FACILITY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    price: float
    specification: str
    rule: str
    address: str
    facility: str
    image_url: str
    def __init__(self, name: _Optional[str] = ..., price: _Optional[float] = ..., specification: _Optional[str] = ..., rule: _Optional[str] = ..., address: _Optional[str] = ..., facility: _Optional[str] = ..., image_url: _Optional[str] = ...) -> None: ...

class KostUpdateRequest(_message.Message):
    __slots__ = ["id", "name", "price", "specification", "rule", "address", "facility", "image_url"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FACILITY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    price: float
    specification: str
    rule: str
    address: str
    facility: str
    image_url: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., price: _Optional[float] = ..., specification: _Optional[str] = ..., rule: _Optional[str] = ..., address: _Optional[str] = ..., facility: _Optional[str] = ..., image_url: _Optional[str] = ...) -> None: ...

class KostDeleteRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class KostDeleteResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
