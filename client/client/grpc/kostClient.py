import grpc

import client.grpc.kosts_pb2 as kosts_pb2
import client.grpc.kosts_pb2_grpc as kosts_pb2_grpc


class KostClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 6000

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = kosts_pb2_grpc.KostsStub(self.channel)

    def create_kost(
        self,
        name,
        price,
        rating,
        gender,
        specification,
        rule,
        address,
        facility,
        image_url,
    ):
        response = self.stub.CreateKost(
            kosts_pb2.KostCreateRequest(
                name=name,
                price=price,
                rating=rating,
                gender=gender,
                specification=specification,
                rule=rule,
                address=address,
                facility=facility,
                image_url=image_url,
            )
        )
        return dict(
            id=response.kost.id,
            name=response.kost.name,
            price=response.kost.price,
            rating=response.kost.rating,
            gender=response.kost.gender,
            specification=response.kost.specification,
            rule=response.kost.rule,
            address=response.kost.address,
            facility=response.kost.facility,
            image_url=response.kost.image_url,
        )

    def get_kost(self, id):
        response = self.stub.GetKost(kosts_pb2.KostRequest(id=id))

        if response.kost.id == 0:
            return None

        return dict(
            id=response.kost.id,
            name=response.kost.name,
            price=response.kost.price,
            rating=response.kost.rating,
            gender=response.kost.gender,
            specification=response.kost.specification,
            rule=response.kost.rule,
            address=response.kost.address,
            facility=response.kost.facility,
            image_url=response.kost.image_url,
        )

    def get_kosts(self):
        response = self.stub.GetKosts(kosts_pb2.KostListRequest())

        if len(response.kosts) == 0:
            return None

        return [
            dict(
                id=kost.id,
                name=kost.name,
                price=kost.price,
                rating=kost.rating,
                gender=kost.gender,
                specification=kost.specification,
                rule=kost.rule,
                address=kost.address,
                facility=kost.facility,
                image_url=kost.image_url,
            )
            for kost in response.kosts
        ]

    def update_kost(
        self,
        id,
        name,
        price,
        rating,
        gender,
        specification,
        rule,
        address,
        facility,
        image_url,
    ):
        response = self.stub.UpdateKost(
            kosts_pb2.KostUpdateRequest(
                id=id,
                name=name,
                price=price,
                rating=rating,
                gender=gender,
                specification=specification,
                rule=rule,
                address=address,
                facility=facility,
                image_url=image_url,
            )
        )

        if response.kost.id == 0:
            return None

        return dict(
            id=response.kost.id,
            name=response.kost.name,
            price=response.kost.price,
            rating=response.kost.rating,
            gender=response.kost.gender,
            specification=response.kost.specification,
            rule=response.kost.rule,
            address=response.kost.address,
            facility=response.kost.facility,
            image_url=response.kost.image_url,
        )

    def delete_kost(self, id):
        response = self.stub.DeleteKost(kosts_pb2.KostDeleteRequest(id=id))

        if response.message is None:
            return None

        return dict(message=response.message)
