import setuptools
import re

with open("Ionburst/__init__.py", "r") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ionburst-sdk-python',
    version=version,
    scripts=[],
    author="Ionburst Limited",
    author_email="sdk@ionburst.io",
    license="Apache-2.0",
    description="Ionburst SDK for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/ionburst/ionburst-sdk-python/",
    packages=['Ionburst'],
    install_requires=[
        'certifi==2020.4.5.1',
        'chardet>=3.0.4',
        'idna>=2.9',
        'python-dotenv>=0.13.0',
        'requests>=2.23.0',
        'urllib3>=1.25.9'
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)