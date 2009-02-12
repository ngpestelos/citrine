from setuptools import setup

setup(
  name = 'OPML Parser',
  version = '0.1',
  description = 'Python library for parsing OPML file',
  long_description = """Parses an OPML file and returns a corresponding \
list.""",
  author = 'Nestor G Pestelos Jr',
  author_email = 'ngpestelos@gmail.com',
  license = 'BSD',
  url = '',
  zip_safe = True,
  classifiers = [
      'Development Status :: 3 - Alpha'],
  packages = ['opml'],
  test_suite = '',
  install_requires = []
)
