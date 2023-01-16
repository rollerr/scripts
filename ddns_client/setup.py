from setuptools import setup, find_packages

setup(
    name="ddns_client",
    version="0.0.1",
    author="Ric Roller",
    packages=find_packages(where="ddns_client"),
    package_dir={"ddns_client": "ddns_client"},
    test_suite="tox",
    tests_require=["tox"],
    install_requires=[
        "click",
        "paramiko",
        "requests",
        "pytest",
        "pytest-cov",
        "pytest-mock",
    ],
    python_requires=">=3.6",
)
