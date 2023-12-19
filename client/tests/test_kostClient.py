import pytest
from unittest.mock import MagicMock

from client.grpc.kostClient import KostClient


@pytest.fixture
def mock_grpc_stub():
    return MagicMock()


@pytest.fixture
def kost_client(mock_grpc_stub):
    client = KostClient()
    client.stub = mock_grpc_stub
    return client


def test_create_kost(kost_client):
    kost_client.stub.CreateKost.return_value = MagicMock(
        kost=MagicMock(id=1, name="Test Kost", price=100.0,
                       rating=4.5, gender="Male")
    )

    result = kost_client.create_kost(
        "Test Kost", 100.0, 4.5, "Male", "Spec", "Rule", "Address", "Facility", "ImageURL")

    assert result["id"] == 1
    assert result["name"] == "Test Kost"
    assert result["price"] == 100.0
    assert result["rating"] == 4.5
    assert result["gender"] == "Male"


if __name__ == "__main__":
    pytest.main()
