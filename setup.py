import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ionburst-sdk',
    version='0.9.10',
    scripts=[],
    author="Costin Botez",
    author_email="contact@costinbotez.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
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