from setuptools import setup

setup(name='pygbif',
	version='0.0.4.9000',
	description='Python client for GBIF',
    author='Scott Chamberlain',
    author_email='myrmecocystus@gmail.com',
    url='http://github.com/sckott/pygbif',
    packages=['pygbif'],
    install_requires=['requests>2.7',
                      'simplejson>3.8'],
    )
