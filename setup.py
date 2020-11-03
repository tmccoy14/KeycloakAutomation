"""Third party modules"""
from setuptools import setup, find_packages

setup(
    name="keycloakcli",
    version="0.1",
    description="Keycloak CLI is a tool to automate the creation of realms and clients to easily integrate authentication with your applications.",
    author="Accenture Federal Services",
    author_email="distillery@afsdigital.studio",
    keywords="keycloak authentication automation python",
    packages=find_packages(exclude=["tests"]),
    install_requires=["Click==7.0", "colorama==0.4.1", "python-keycloak==0.22.0"],
    entry_points={"console_scripts": ["keycloakcli=src.main:cli"]},
)
