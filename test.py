#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/5 下午 02:47
# @Author  : kamino

import Core

"""
a = Core.Encrypt.aes_encrypt('123', '123')
print(a)
print(Core.Encrypt.aes_decrypt(a, '123'))
"""

print(Core.CqCode.findAll('[CQ:face,id=19]666[CQ:face,id=19]666[CQ:face,id=19]666'))
