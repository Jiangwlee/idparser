#!/usr/bin/env python
#-*- encoding:utf8 -*-

import json

# 城市映射表，从身份证的前六位映射出省市信息
CITYMAP=json.load(open('./gb2260.json'))

def parse_id(idstr):
    # Check the length of id
    if len(idstr)!=15 and len(idstr)!=18:
        return None
    # Get the city info
    city = CITYMAP[idstr[:6]]
    birthday = None
    gender = None
    if len(idstr) == 18:
        birthday = idstr[6:14]
        gender = 'M' if int(idstr[16])%2 else 'F'
    else:
        birthday = '19'+idstr[6:12]
        gender = 'M' if int(idstr[14])%2 else 'F'
    return [city, birthday, gender]

if __name__ == '__main__':
    print(parse_id('42118119871221112X'))
    print(parse_id('421181871221111'))
