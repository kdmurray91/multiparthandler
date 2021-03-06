# Copyright (c) 2012 Kevin Murray k.d.murray.91@gmail.com
# multiparthandler is licensed under the LGPL v3

try:
    from distutils2.core import setup
except ImportError:
    from distutils.core import setup

setup(
    name="multiparthandler",
    packages=['multiparthandler', ],
    version="0.1",
    description=("A handler for urllib2/urllib.request that allows "
        "multipart form uploading"),
    author="Kevin Murray",
    author_email="k.d.murray.91@gmail.com",
    url="https://github.com/kdmurray91/multiparthandler",
    keywords=["http", "multipart", "post", "urllib2"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 "
        "(LGPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    )
