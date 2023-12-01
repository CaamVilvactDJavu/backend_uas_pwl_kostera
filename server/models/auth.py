from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Auth(Base):
    __tablename__ = "auth"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    roles = relationship("Roles", secondary="auth_roles")


class Roles(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(255), nullable=False)
    auth = relationship("Auth", secondary="auth_roles", back_populates="roles")


auth_roles = Table(
    "auth_roles",
    Base.metadata,
    Column("auth_id", Integer, ForeignKey("auth.id"), primary_key=True),
    Column("role_id", Integer, ForeignKey("roles.id"), primary_key=True),
)
