# setup.py
from setuptools import setup, find_packages

setup(
    name="warframe",
    version="0.1.0", 
    author="NathanYYDS", 
    author_email="zgc2200394635@gmail.com",
    description="Warframe API package of Python",
    packages=find_packages(), 
    install_requires=["requests"],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Intended Audience :: Developers",
    ],
)