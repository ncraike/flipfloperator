from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='flipfloperator-deluxe',

    version='0.1.0',

    description='Flipflop operators, all kinds',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/ncraike/flipfloperator',

    # Author details
    author='Nathan Craike',
    author_email='me@ncraike.com',

    # Choose your license
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='flipfloperator novelty comedy horror romcom',

    packages=find_packages(exclude=['contrib', 'docs']),

    install_requires=[],

    extras_require = {
        'docs': ['docutils', 'Pygments'],
    },

    entry_points={
    },
)
