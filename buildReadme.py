#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

f = open('./config.yml')
x = yaml.load(f)

readmeStr = ''' # org-repository

'''
for i in range(0,len(x)):
    readmeStr+='- [{}](./{})\n'.format(x[i]['name'],x[i]['file'])

f.close()

readmeFile = open('./README.md','w+')
readmeFile.write(readmeStr)
readmeFile.close()



