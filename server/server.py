from sqlalchemy import insert, select, update, delete, desc
from concurrent import futures
from database.config import engine
import logging
import grpc
import jwt

import kosts_pb2_grpc
import kosts_pb2
from models.kost import Kost

import auth_pb2_grpc
import auth_pb2
from models.auth import Auth, Roles, auth_roles
import secrets


jwt_secret = secrets.token_urlsafe(32)
jwt_algorithm = "HS256"

print("Generated JWT Secret Key:", jwt_secret)


class AuthServicer(auth_pb2_grpc.AuthService):
    def generate_jwt_token(self, user_id, roles):
        payload = {"sub": str(user_id), "roles": roles}
        return jwt.encode(payload, jwt_secret, algorithm=jwt_algorithm)

    def RegisterUser(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                new_user = Auth(username=request.username, password=request.password)
                conn.execute(
                    insert(Auth).values(
                        username=new_user.username, password=new_user.password
                    )
                )

                roles = []  # Modify this to assign roles based on your logic
                for role_name in roles:
                    role = conn.execute(
                        select(Roles).where(Roles.role_name == role_name)
                    ).first()
                    if role:
                        new_user.roles.append(role)

                conn.commit()

            token = self.generate_jwt_token(new_user.id, roles)

            return auth_pb2.RegisterResponse(
                message="User registered successfully", token=token
            )
        except Exception as e:
            print(f"Error registering user: {e}")
            return auth_pb2.RegisterResponse(message="Error")

    def LoginUser(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                user = conn.execute(
                    select(Auth).where(Auth.username == request.username)
                ).first()

                if user and user.password == request.password:
                    # Fetch roles information from the database
                    roles_query = conn.execute(
                        select(Roles.role_name)
                        .join(auth_roles)
                        .where(auth_roles.c.auth_id == user.id)
                    )

                    roles = [role[0] for role in roles_query]

                    # Use a new connection for subsequent operations
                    with engine.connect() as new_conn:
                        new_conn.begin()

                        # Generate token using the new connection
                        token = self.generate_jwt_token(user.id, roles)

                        new_conn.commit()

                    return auth_pb2.LoginResponse(
                        token=token,
                        message="Login successful",
                    )
                else:
                    return auth_pb2.LoginResponse(message="Invalid credentials")

        except Exception as e:
            print(f"Error logging in user: {e}")
            return auth_pb2.LoginResponse(message="Error")

    def VerifyToken(self, request, context):
        try:
            decoded_token = jwt.decode(
                request.token, jwt_secret, algorithms=[jwt_algorithm]
            )

            user_roles = decoded_token.get("roles", [])
            if "admin" in user_roles:
                return auth_pb2.VerifyTokenResponse(message="Token is valid")
            else:
                return auth_pb2.VerifyTokenResponse(message="Unauthorized user")

        except jwt.ExpiredSignatureError:
            return auth_pb2.VerifyTokenResponse(message="Token has expired")
        except jwt.InvalidTokenError:
            return auth_pb2.VerifyTokenResponse(message="Invalid token")
        except Exception as e:
            print(f"Error verifying token: {e}")
            return auth_pb2.VerifyTokenResponse(message="Error")


class KostsServicer(kosts_pb2_grpc.KostsServicer):
    def GetKost(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(select(Kost).where(Kost.id == request.id)).first()

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

                res = conn.execute(select(Kost).order_by(desc(Kost.id))).all()

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
    auth_servicer = AuthServicer()
    kosts_pb2_grpc.add_KostsServicer_to_server(KostsServicer(), server)
    auth_pb2_grpc.add_AuthServiceServicer_to_server(auth_servicer, server)
    server.add_insecure_port("localhost:6000")
    server.start()
    print("Server started at localhost:6000")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
