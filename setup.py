import os
import sys

if sys.version_info[0:2] < (3, 6):
    raise Exception("aionewton requires Python 3.6+")

from setuptools import setup

rootpath = os.path.abspath(os.path.dirname(__file__))


def extract_version(_module='aionewton'):
    version = None
    fname = os.path.join(rootpath, _module, '__init__.py')
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                _, version = line.split('=')
                version = version.strip()[1:-1]  # Remove quotation characters.
                break
    return version

setup(
    name='aionewton',
    version=extract_version(),
    packages=['aionewton'],
    url='https://github.com/ilevn/aionewton',
    license='MIT',
    author='Nils Theres',
    author_email='nilsntth@gmail.com',
    description='An asyncio-based wrapper for the newton-api',
    install_requires=['aiohttp>=2.0.5']
)
