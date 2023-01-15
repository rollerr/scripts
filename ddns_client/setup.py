from setuptools import setup, find_packages

setup(
    name="ddns_client",
    version="0.0.1",
    author="Ric Roller",
    packages=find_packages(),
    test_suite="tox",
    tests_require=["tox"],
    install_requires=[
        "paramiko",
        "requests",
        "pytest",
        "pytest-cov",
        "pytest-mock",
    ],
    python_requires=">=3.6",
)
