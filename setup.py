from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.4'
DESCRIPTION = 'Ankiz Test PIP Package'
LONG_DESCRIPTION = 'Demo Package - to add , sub, mult, div two numbers. - version 0.0.3 - fixed init file again'

# Setting up
setup(
    name="akpycalc",
    version=VERSION,
    author="Ankiz",
    author_email="<ankit48365@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    #install_requires=[''],
    keywords=['python', 'ankiz', 'demo', 'ankitfotografia'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)