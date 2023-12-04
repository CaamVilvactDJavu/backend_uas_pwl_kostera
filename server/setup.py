import os

from setuptools import setup, find_packages

requires = [
    "alembic",
    "SQLAlchemy",
    "grpcio",
    "grpcio-tools",
    "PyMySQL",
    "mysql-connector-python",
    "pyramid_jwt",
    "PyJWT",
    "bcrypt",
]

tests_require = [
    "pytest",
    "pytest-cov",
]

setup(
    name="server",
    version="0.0",
    description="backend_uas_pwl_kostera",
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author="c.a._.a.m",
    author_email="",
    url="",
    keywords="grpc pyramid",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        "testing": tests_require,
    },
    install_requires=requires,
)
