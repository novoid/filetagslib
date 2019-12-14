# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name="filetagslib",
    version="2019.12.14.1",
    description="Utility library for providing functions related to the filetags file name convention: https://github.com/novoid/filetags",
    license='GPLv3',
    author="Karl Voit",
    author_email="tools@Karl-Voit.at",
    url="https://github.com/novoid/filetagslib",
    download_url="https://github.com/novoid/filetagslib/zipball/master",
    keywords=["tagging", "tags", "file managing", "file management", "files", "tagtrees", "tagstore", "tag-based navigation", "tag-based filter"],
    packages=find_packages(),
    #install_requires=["pyreadline", "clint"],  # add dependencies if they are included in the code
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        ]
)
