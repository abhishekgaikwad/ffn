import setuptools
import codecs
import os
import re


def local_file(filename):
    return codecs.open(
        os.path.join(os.path.dirname(__file__), filename), 'r', 'utf-8'
    )


version = ('0', '3', '2')


setuptools.setup(
    name="ffn",
    version='.'.join(version),
    author='Philippe Morissette',
    author_email='morissette.philippe@gmail.com',
    description='Financial functions for Python',
    keywords='python finance quant functions',
    url='https://github.com/pmorissette/ffn',
    install_requires=[
        'decorator>=4',
        'numpy>=1.5',
        'pandas>=0.19',
        'pandas-datareader>=0.2',
        'tabulate>=0.7.5',
        'matplotlib>=1',
        'scikit-learn>=0.15',
        'scipy>=0.15',
        'future>=0.15',
        'fix_yahoo_finance>=0.0.18'
    ],
    packages=['ffn'],
    long_description=local_file('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python'
    ]
)
