multiparthandler:
================

A module to allow urllib2 and urllib.request to POST multipart requests.
This is an updated version of MultipartPostHandler, by Will Holcomb.
The original module has been modernized, and made compatible with Python 3.x.

License:
=======
Copyright (c) 2012 Kevin Murray k.d.murray.91@gmail.com <br />

multiparthandler is licensed under the LGPL v3
See <http://www.gnu.org/copyleft/lesser.html> for full license text.<br />

NOTE: This is not an official updated version of MultipartPostHandler,
and is not affiliated with the original author in any way.

Example Usage:
==============
(Adapted from MultipartPostHandler's example)
```
>>>import multiparthandler
>>>import urllib2
>>>import cookielib
>>>cookies = cookielib.CookieJar()
>>>opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies),
...                        multiparthandler.multiparthandler)
>>>params = { "username" : "bob", "password" : "riviera",
...          "file" : open("filename", "rb") }
>>>opener.open("http://wwww.bobsite.com/upload/", params)
```
Further Examples can be found in the unittests provided in the ```tests/``
directory.
