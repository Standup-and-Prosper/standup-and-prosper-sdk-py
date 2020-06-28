import os
from setuptools import setup, find_packages

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "authress-sdk >= 1.0.40"]

# To install the library, run the following
#
# python setup.py install

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

with open(os.path.join(this_directory, 'standup_and_prosper_sdk', 'VERSION')) as version_file:
  VERSION = version_file.read().strip()

print("Building version", VERSION)

setup(
  name = 'standup-and-prosper-sdk',
  version = VERSION,
  description = 'The Standup & Prosper SDK for interacting with standups programmatically.',
  author = 'Rhosys Developers',
  author_email = 'developers@teaminator.io',
  url = 'https://github.com/Teaminator/standup-and-prosper-sdk.py.git',
  include_package_data = True,
  install_requires=REQUIRES,
  packages = find_packages(exclude=['tests', 'integrationTests']),
  data_files=[('', ['standup_and_prosper_sdk/VERSION'])],
  keywords = ['Standups', 'Stand ups', 'Dailies', 'Standup & Prosper', 'Teaminator'],
  classifiers = [],
  license = 'Apache-2.0',
  long_description=long_description,
  long_description_content_type='text/markdown'
)
