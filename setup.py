import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-tarantool",
    version="0.0.13",
    package_dir={"django-tarantool": os.path.join("django_tarantool")},
    author="Artem Morozov",
    author_email="artembo@me.com",
    description="Tarantool database backend for Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/artembo/django-tarantool",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)