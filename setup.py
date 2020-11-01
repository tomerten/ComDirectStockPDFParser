from pathlib import Path
from typing import Dict

from setuptools import find_packages, setup

base_path = Path(__file__).resolve().parent
about: Dict[str, str] = {}
exec((base_path / "ComDirectStockPDFParser/__about__.py").read_text(), about)
readme = (base_path / "README.md").read_text()
requirements = (base_path / "requirements.txt").read_text()


setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    url=about["__url__"],
    author=about["__author__"],
    license=about["__license__"],
    packages=find_packages(),
    install_requires=requirements,
    entry_points={"console_scripts": ["ComDirectStockPDFParser=ComDirectStockPDFParser.cli:main"]},
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
