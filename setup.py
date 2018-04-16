import os
from setuptools import setup

base_dir = os.path.dirname(__file__)

with open(os.path.join(base_dir, "opentdb", "__about__.py")) as f:
    about = {}
    exec(f.read(), about)

with open(os.path.join(base_dir, "README.md")) as f:
    long_description = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email = about['__email__'],
    license=about['__license__'],
    description=about['__summary__'],
    long_description=long_description,
    url=about['__uri__'],
    scripts=['opentdb']
)
