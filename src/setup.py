import io
from setuptools import find_packages, setup


def long_description():
    with io.open('./README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


setup(name='se-service',
      version='0.1',
      description='Search Engine service',
      long_description=long_description(),
      url='https://github.com/lafamia/custom_search_engine',
      author='lafamila',
      author_email='lafamila@naver.com',
      license='',
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 3.8.7',
          ],
      zip_safe=False)