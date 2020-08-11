################################################################################
# Name        : setup
# Description : The installer for the package.
# Version     : 0.0.5
# Created On  : 2019-01-10
# Modified On : 2020-08-11
# Authors     : Hamid R. Darabi, Ph.D.
#               Vaibhav Sharma
################################################################################

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ds_lib",
    version="0.0.6",
    author="Hamid R. Darabi, Vaibhav Sharma",
    author_email="***@***.com",
    description="Includes all utility functions that makes my daily life easier.",
    long_description_content_type="text/markdown",
    url="***",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)