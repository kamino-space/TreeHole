#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 下午 07:40
# @Author  : kamino

import re


class CqCode(object):
    """
    解析CQ码
    [CQ:face,id={1}] - QQ表情
    [CQ:emoji,id={1}] - emoji表情
    [CQ:bface,id={1}] - 原创表情
    [CQ:sface,id={1}] - 小表情
    [CQ:image,file={1}] - 发送自定义图片
    [CQ:record,file={1},magic={2}] - 发送语音
    [CQ:at,qq={1}] - @某人
    [CQ:rps,type={1}] - 发送猜拳魔法表情
    [CQ:dice,type={1}] - 发送掷骰子魔法表情
    [CQ:shake] - 戳一戳（原窗口抖动，仅支持好友消息使用）
    [CQ:anonymous,ignore={1}] - 匿名发消息（仅支持群消息使用）
    [CQ:music,type={1},id={2}] - 发送音乐
    [CQ:music,type=custom,url={1},audio={2},title={3},content={4},image={5}] - 发送音乐自定义分享
    [CQ:share,url={1},title={2},content={3},image={4}] - 发送链接分享
    """

    @staticmethod
    def findAll(text=None):
        """
        查找所有的CQ码
        :param text:
        :return:
        """
        r = re.search(r'\[CQ:(.*)\]', text)
        return r.groups()
