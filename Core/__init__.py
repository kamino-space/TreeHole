#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/5 下午 02:44
# @Author  : kamino

import queue

from .encrypt import Encrypt
from .timer import Timer
from .message import MsgBuilder, MsgSender
from .cqcode import CqCode

SQ = queue.Queue(1024)  # 发送队列
