from setuptools import setup, find_packages

setup(name='test-pip-package',
      version='0.0.1',
      description='Test Pip Package',
      author='Brian J. Bowler',
      url='https://localhost',
      packages=['test-pip-package'],
      install_requires=['nltk'])
