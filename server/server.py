from concurrent import futures
import logging
import kosts_pb2_grpc
import grpc
import kosts_pb2
from sqlalchemy import insert, select, update, delete, desc

from database.config import engine
from models.kost import Kost


class KostsServicer(kosts_pb2_grpc.KostsServicer):
    def GetKost(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    select(Kost).where(Kost.id == request.id)
                ).first()

                conn.commit()

            if res:
                return kosts_pb2.KostResponse(
                    kost=kosts_pb2.Kost(
                        id=res[0],
                        name=res[1],
                        price=res[2],
                        rating=res[3],
                        gender=res[4],
                        specification=res[5],
                        rule=res[6],
                        address=res[7],
                        facility=res[8],
                        image_url=res[9],
                    ),
                    message="Kost retrieved",
                )
            else:
                print("No result found")

        except Exception as e:
            print(f"Error fd {e}")
            return kosts_pb2.KostResponse(message="Error")

    def GetKosts(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    select(Kost).order_by(desc(Kost.id))).all()

                kosts = []

                for row in res:
                    kosts.append(
                        kosts_pb2.Kost(
                            id=row[0],
                            name=row[1],
                            price=row[2],
                            rating=row[3],
                            gender=row[4],
                            specification=row[5],
                            rule=row[6],
                            address=row[7],
                            facility=row[8],
                            image_url=row[9],
                        )
                    )

                conn.commit()

            return kosts_pb2.KostListResponse(
                kosts=kosts,
                message="Kosts retrieved",
            )
        except Exception as e:
            print(f"Error df {e}")
            return kosts_pb2.KostListResponse(message="Error")

    def CreateKost(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    insert(Kost).values(
                        name=request.name,
                        price=request.price,
                        rating=request.rating,
                        gender=request.gender,
                        specification=request.specification,
                        rule=request.rule,
                        address=request.address,
                        facility=request.facility,
                        image_url=request.image_url,
                    )
                )

                conn.commit()

            print(f"Kost {request.name} created")

            return kosts_pb2.KostResponse(
                kost=kosts_pb2.Kost(
                    name=request.name,
                    price=request.price,
                    rating=request.rating,
                    gender=request.gender,
                    specification=request.specification,
                    rule=request.rule,
                    address=request.address,
                    facility=request.facility,
                    image_url=request.image_url,
                ),
                message="Kost created",
            )

        except Exception as e:
            print(f"Error sd {e}")
            return kosts_pb2.KostResponse(message="Error")

    def UpdateKost(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    update(Kost)
                    .where(Kost.id == request.id)
                    .values(
                        name=request.name,
                        price=request.price,
                        rating=request.rating,
                        gender=request.gender,
                        specification=request.specification,
                        rule=request.rule,
                        address=request.address,
                        facility=request.facility,
                        image_url=request.image_url,
                    )
                )

                conn.commit()

            print(f"Kost {request.name} updated")

            return kosts_pb2.KostResponse(
                kost=kosts_pb2.Kost(
                    id=request.id,
                    name=request.name,
                    price=request.price,
                    rating=request.rating,
                    gender=request.gender,
                    specification=request.specification,
                    rule=request.rule,
                    address=request.address,
                    facility=request.facility,
                    image_url=request.image_url,
                ),
                message="Kost updated",
            )

        except Exception as e:
            print(f"Error as {e}")
            return kosts_pb2.KostResponse(message="Error")

    def DeleteKost(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                conn.execute(delete(Kost).where(Kost.id == request.id))

                conn.commit()

            return kosts_pb2.KostDeleteResponse(message="Kost deleted")

        except Exception as e:
            print(f"Error as {e}")
            return kosts_pb2.KostDeleteResponse(message="Error")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kosts_pb2_grpc.add_KostsServicer_to_server(
        KostsServicer(), server)
    server.add_insecure_port("localhost:6000")
    server.start()
    print("Server started at localhost:6000")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
