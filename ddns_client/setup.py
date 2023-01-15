from setuptools import setup, find_packages

setup(
    name="ddns_client",
    version="0.0.1",
    author="Ric Roller",
    packages=find_packages(include=["ddns_client", "ddns_client.*", "tests"]),
    package_dir={"": "src"},
    install_requires=[
        "paramiko",
        "requests",
        "pytest",
        "pytest-cov",
        "pytest-mock",
    ],
    python_requires=">=3.6",
)
