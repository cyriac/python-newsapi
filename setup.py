import os
from pip.download import PipSession
from pip.req import parse_requirements
from setuptools import setup, find_packages

install_reqs = parse_requirements('requirements.txt', session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]
version = '1.0.2'

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name='python-newsapi',
    version=version,
    packages=find_packages(),
    install_requires=reqs,
    include_package_data=True,
    license='MIT',
    description='python wrapper for newsapi.org',
    keywords = ['newsapi.org', 'newsapi'],
    url='https://github.com/cyriac/python-newsapi',
    download_url = 'https://github.com/cyriac/python-newsapi/archive/v{version}.tar.gz'.format(version=version),
    author='Compile Inc',
    author_email='dev@compile.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
