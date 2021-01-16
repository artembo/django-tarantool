import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-tarantool",
    version="0.0.20",
    package_dir={"django-tarantool": os.path.join("django_tarantool")},
    author="Artem Morozov",
    author_email="artembo@me.com",
    description="Tarantool database backend for Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/artembo/django-tarantool",
    packages=setuptools.find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'tarantool>=0.7.1',
    ],
)
