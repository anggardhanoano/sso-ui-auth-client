import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="SSO-UI-auth-client-cas",
    version="1.0.0",
    description="General SSO UI Auth client for Python project",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Anggardha Febriano",
    author_email="anggardha.febriano@ui.ac.id",
    url="https://github.com/anggardhanoano/sso-ui-auth-client",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["cas-client>=1.0.0", "flask"],
)