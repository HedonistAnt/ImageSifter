from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='imagesifter',
    version='1.0.6',
    description='Easy-to-use package for downloading originals of images from web sites ',
    long_description=long_description,
    packages=find_packages(),
    author='Hedonist_Ant',
    author_email='redkandibober666@gmail.com',
    url='https://github.com/HedonistAnt/ImageSifter',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='download image web sites',

    python_requires='>=2.7'
)