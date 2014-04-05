try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'describption': 'My Project',
        'author': 'Leo',
        'author_email': 'joelleo.mao@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['tictoctie'],
        'scripts': [],
        'name': 'a simple game'
        }

setup(**config)
