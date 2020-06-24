from setuptools import setup
from distutils.util import convert_path

from typing import Dict, Any

# Version Information
main_ns: Dict[Any, Any] = {}
version_path = convert_path('cannalysis_api/version.py')
with open(version_path) as version_file:
    exec(version_file.read(), main_ns)

# Long Description via README.md
with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(name='cannalysis_api',
      version=main_ns['__version__'],
      description='''
        An API wrapping METRC's Colorado API for regulated marijuana tracking
        and inventory.
        ''',
      long_description=long_description,
      url='https://github.com/ashwig/cannalysis_api',
      packages=['cannalysis_api'],
      include_package_data=True,
      install_requires=[],
      entry_points={'console_scripts': ['cannalysis_api=cannalysis_api:cli']},
      zip_safe=False,
      classifiers=[
          'Framework :: Flask', 'License :: Other/Proprietary License',
          'Natural Language :: English', 'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: SQL', 'Programming Language :: Unix Shell',
          'Topic :: Internet:: WWW/HTTP:: WSGI :: Application',
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Typing :: Typed'
      ])
