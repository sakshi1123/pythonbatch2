Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s="ab=c;def=ghi;"
>>> asd= dict(item.split("=") for item in s.split(";"))

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    asd= dict(item.split("=") for item in s.split(";"))
ValueError: dictionary update sequence element #2 has length 1; 2 is required
>>> ss="ab=c;def=ghi"
>>> asd= dict(item.split("=") for item in s.split(";"))

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    asd= dict(item.split("=") for item in s.split(";"))
ValueError: dictionary update sequence element #2 has length 1; 2 is required
>>> 
>>> 
>>> s="ab=c;def=ghi"
>>> asd= dict(item.split("=") for item in s.split(";"))
>>> asd
{'ab': 'c', 'def': 'ghi'}
>>> 
