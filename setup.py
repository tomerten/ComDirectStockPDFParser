import os

from setuptools import setup, find_packages

with open("ComDirectStockPDFParser/__about__.py") as file:
    about = {}
    for line in file:
        k, v = line.split("=")
        about[k] = v

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        readinput = f.read()
    return readinput


setup(
    ame=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url=about["__url__"],
    author=about["__author__"],
    license=about["__license__"],
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'ComDirectStockPDFParser=ComDirectStockPDFParser.cli:main'
        ]
    },
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Office/Business :: Financial",
        "Intended Audience :: Financial and Insurance Industry",
    ],
)
