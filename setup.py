from os import path
from setuptools import setup, find_packages


version = __import__("rechat").__version__

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="django-rechat",
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description="A chat application for Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="synw",
    author_email="synwe@yahoo.com",
    url="https://github.com/synw/django-rechat",
    download_url="https://github.com/synw/django-rechat/releases/tag/" + version,
    keywords=["django", "chat", "websockets"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django :: 1.11",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=["django-instant"],
    zip_safe=False,
)
