import re
from setuptools import setup

version = ''
with open('PhoenixScanner/__init__.py') as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)


requirements = ['requests']
    

if not version:
    raise RuntimeError('version is not set')

readme = ''
with open('README.md', encoding="utf8") as f:
    readme = f.read()

setup(
    name='PhoenixScanner',
    author='SOME1HING',
    author_email='yashprakash2005@gmail.com',
    version=version,
    long_description=readme,
    url='https://github.com/SOME-1HING/PhoenixScanner',
    packages=['PhoenixScanner'],
    license='GNU General Public License v3.0',
    classifiers=[
        "Framework :: AsyncIO",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        "Natural Language :: English",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Build Tools",

    ],
    description='A API bassed telegram gban scanner.',
    include_package_data=True,
    keywords=['telegram', 'phoenix', 'bot', 'api', 'gban',
              'scan'],
    install_requires=requirements
)