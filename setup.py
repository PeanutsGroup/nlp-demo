from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup


setup(
    name='nlp-demo',
    version='0.1',
    author='Buckaroo Cheung',
    author_email='',
    packages=['nlpdemo'],
    url='',
    license='See LICENSE',
    description='Demo program about Natural Language Processing.',
    long_description=open('README').read(),
)
