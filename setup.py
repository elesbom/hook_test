# coding: utf-8
from setuptools import setup, find_packages

setup(
    name = 'apresentador',
    version = '1.2.8',
    description = u'App do projeto Variedades que contem o modelo de Apresentador'.encode('utf-8'),
    author = 'Entretenimento',
    author_email = 'entretenimento@corp.globo.com',
    url = 'http://ngit.globoi.com/base-variedades/apresentador',
    packages = find_packages(),
    zip_safe = False,
    include_package_data = True,
)
