from sqlalchemy import insert, select, update, delete, desc
from datetime import datetime
from concurrent import futures
from database.config import engine
import logging
import grpc
import jwt
import bcrypt

import kosts_pb2_grpc
import kosts_pb2
from models.kost import Kost

import auth_pb2_grpc
import auth_pb2
from models.auth import Auth, Roles, auth_roles
import secrets


jwt_secret = secrets.token_urlsafe(32)
jwt_algorithm = "HS256"


class AuthServicer(auth_pb2_grpc.AuthService):
    def generate_jwt_token(self, user_id, roles):
        payload = {"sub": str(user_id), "roles": roles}
        return jwt.encode(payload, jwt_secret, algorithm=jwt_algorithm)

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password

    def RegisterUser(self, request, context):
        try:
            if not (5 <= len(request.username) <= 16):
                return auth_pb2.RegisterResponse(
                    message="Username must be between 5 and 16 characters"
                )

            with engine.connect() as conn:
                conn.begin()

                existing_user = conn.execute(
                    select(Auth).where(Auth.username == request.username)
                ).first()

                if existing_user:
                    return auth_pb2.RegisterResponse(
                        message="Username already exists. Please choose a different one."
                    )

                new_user = Auth(
                    username=request.username,
                    password=self.hash_password(request.password),
                )
                conn.execute(
                    insert(Auth).values(
                        username=new_user.username, password=new_user.password
                    )
                )

                role_user = conn.execute(
                    select(Roles).where(Roles.role_name == "user")
                ).first()
                if role_user:
                    new_user.roles.append(role_user)

                roles = [request.role] if request.role else ["user"]
                for role_name in roles:
                    role = conn.execute(
                        select(Roles).where(Roles.role_name == role_name)
                    ).first()
                    if role:
                        new_user.roles.append(role)

                # Fetch the user ID after insertion
                new_user = conn.execute(
                    select(Auth).where(Auth.username == request.username)
                ).first()

                # Add the user to the "user" role in auth_roles table
                conn.execute(
                    insert(auth_roles).values(
                        auth_id=new_user.id,
                        role_id=role_user.id,
                    )
                )

                conn.commit()

                token = self.generate_jwt_token(new_user.id, roles)

                return auth_pb2.RegisterResponse(
                    message="User registered successfully", token=token
                )

        except Exception as e:
            print(f"Error registering user: {e}")
            return auth_pb2.RegisterResponse(message="Error")

    def AdminLogin(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                user = conn.execute(
                    select(Auth).where(Auth.username == request.username)
                ).first()

                if (
                    user
                    and user.password
                    and bcrypt.checkpw(
                        request.password.encode("utf-8"), user.password.encode("utf-8")
                    )
                ):
                    roles_query = conn.execute(
                        select(Roles.role_name)
                        .join(auth_roles)
                        .where(auth_roles.c.auth_id == user.id)
                    )

                    roles = [role[0] for role in roles_query]

                    token = self.generate_jwt_token(user.id, roles)

                    return auth_pb2.AdminLoginResponse(
                        token=token,
                        message="Admin login successful",
                        roles=",".join(roles),
                    )
                else:
                    return auth_pb2.AdminLoginResponse(message="Invalid credentials")

        except Exception as e:
            print(f"Error logging in admin: {e}")
            return auth_pb2.AdminLoginResponse(message="Error")

    def LoginUser(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                user = conn.execute(
                    select(Auth).where(Auth.username == request.username)
                ).first()

                if user and bcrypt.checkpw(
                    request.password.encode("utf-8"), user.password.encode("utf-8")
                ):
                    roles_query = conn.execute(
                        select(Roles.role_name)
                        .join(auth_roles)
                        .where(auth_roles.c.auth_id == user.id)
                    )

                    roles = [role[0] for role in roles_query]
                    token = self.generate_jwt_token(user.id, roles)

                    return auth_pb2.LoginResponse(
                        token=token,
                        message="Login successful",
                        role=roles[0] if roles else "user",
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
                        created_at=datetime.utcnow(),
                        updated_at=datetime.utcnow(),
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
                        rating=request.rating,
                        price=request.price,
                        gender=request.gender,
                        specification=request.specification,
                        rule=request.rule,
                        address=request.address,
                        facility=request.facility,
                        image_url=request.image_url,
                        updated_at=datetime.utcnow(),
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
