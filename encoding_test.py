#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

#print((json.loads('{"text":"абвТ"}')).encode('utf-8'))
j=json.loads('{"text":"абвТ"}')
print(j['text'].encode('utf-8'))

