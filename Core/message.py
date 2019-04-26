#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 下午 08:20
# @Author  : kamino

import json
import queue
import Core


class MsgBuilder(object):
    @staticmethod
    def build(action, params=None):
        """创建json消息"""
        return json.dumps({
            'action': action,
            'params': params
        })

    @staticmethod
    def send_private_msg(user_id, message, auto_escape=False):
        """
        发送私聊消息
        :param user_id: 对方 QQ 号
        :param message: 要发送的内容
        :param auto_escape: 消息内容是否作为纯文本发送（即不解析 CQ 码），只在 message 字段是字符串时有效
        :return: json
        """
        return MsgBuilder.build('send_private_msg', {
            'user_id': user_id,
            'message': message,
            'auto_escape': auto_escape
        })

    @staticmethod
    def send_group_msg(group_id, message, auto_escape=False):
        """
        发送群消息
        :param group_id: 群号
        :param message: 要发送的内容
        :param auto_escape: 消息内容是否作为纯文本发送（即不解析 CQ 码），只在 message 字段是字符串时有效
        :return: json
        """
        return MsgBuilder.build('send_group_msg', {
            'group_id': group_id,
            'message': message,
            'auto_escape': auto_escape
        })

    @staticmethod
    def send_discuss_msg(discuss_id, message, auto_escape=False):
        """
        发送讨论组消息
        :param discuss_id: 讨论组 ID（正常情况下看不到，需要从讨论组消息上报的数据中获得）
        :param message: 要发送的内容
        :param auto_escape: 消息内容是否作为纯文本发送（即不解析 CQ 码），只在 message 字段是字符串时有效
        :return: json
        """
        return MsgBuilder.build('send_discuss_msg', {
            'discuss_id': discuss_id,
            'message': message,
            'auto_escape': auto_escape
        })

    @staticmethod
    def delete_msg(message_id):
        """
        撤回消息
        :param message_id: 消息 ID
        :return: json
        """
        return MsgBuilder.build('delete_msg', {
            'message_id': message_id
        })

    @staticmethod
    def send_like(user_id, times=1):
        """
        发送好友赞
        :param user_id: 对方 QQ 号
        :param times: 赞的次数，每个好友每天最多 10 次
        :return: json
        """
        return MsgBuilder.build('send_like', {
            'user_id': user_id,
            'times': times
        })

    @staticmethod
    def set_group_kick(group_id, user_id, reject_add_request=False):
        """
        群组踢人
        :param group_id: 群号
        :param user_id: 要踢的 QQ 号
        :param reject_add_request: 拒绝此人的加群请求
        :return: json
        """
        return MsgBuilder.build('set_group_kick', {
            'group_id': group_id,
            'user_id': user_id,
            'reject_add_request': reject_add_request
        })

    @staticmethod
    def set_group_ban(group_id, user_id, duration=1800):
        """
        群组单人禁言
        :param group_id: 群号
        :param user_id: 要禁言的 QQ 号
        :param duration: 禁言时长，单位秒，0 表示取消禁言
        :return: json
        """
        return MsgBuilder.build('set_group_ban', {
            'group_id': group_id,
            'user_id': user_id,
            'duration': duration
        })

    @staticmethod
    def set_group_anonymous_ban(group_id, anonymous, anonymous_flag, duration=1800):
        """
        群组匿名用户禁言
        :param group_id: 群号
        :param anonymous: 可选，要禁言的匿名用户对象（群消息上报的 anonymous 字段）
        :param anonymous_flag: 可选，要禁言的匿名用户的 flag（需从群消息上报的数据中获得）
        :param duration: 禁言时长，单位秒，无法取消匿名用户禁言
        :return: json
        """
        return MsgBuilder.build('set_group_anonymous_ban', {
            'group_id': group_id,
            'anonymous': anonymous,
            'anonymous_flag': anonymous_flag,
            'duration': duration
        })

    @staticmethod
    def set_group_whole_ban(group_id, enable=True):
        """
        群组全员禁言
        :param group_id: 群号
        :param enable: 是否禁言
        :return: json
        """
        return MsgBuilder.build('set_group_whole_ban', {
            'group_id': group_id,
            'enable': enable
        })

    @staticmethod
    def set_group_admin(group_id, user_id, enable=True):
        """
        群组设置管理员
        :param group_id: 群号
        :param user_id: 要设置管理员的 QQ 号
        :param enable: true 为设置，false 为取消
        :return: json
        """
        return MsgBuilder.build('set_group_admin', {
            'group_id': group_id,
            'user_id': user_id,
            'enable': enable
        })

    @staticmethod
    def set_group_anonymous(group_id, enable=True):
        """
        群组匿名
        :param group_id: 群号
        :param enable: 是否允许匿名聊天
        :return: json
        """
        return MsgBuilder.build('set_group_anonymous', {
            'group_id': group_id,
            'enable': enable
        })

    @staticmethod
    def set_group_card(group_id, user_id, card=None):
        """
        设置群名片（群备注）
        :param group_id: 群号
        :param user_id: 要设置的 QQ 号
        :param card: 群名片内容，不填或空字符串表示删除群名片
        :return: json
        """
        return MsgBuilder.build('set_group_card', {
            'group_id': group_id,
            'user_id': user_id,
            'card': card
        })

    @staticmethod
    def set_group_leave(group_id, is_dismiss=False):
        """
        退出群组
        :param group_id: 退出群组
        :param is_dismiss: 是否解散，如果登录号是群主，则仅在此项为 true 时能够解散
        :return: json
        """
        return MsgBuilder.build('set_group_leave', {
            'group_id': group_id,
            'is_dismiss': is_dismiss
        })

    @staticmethod
    def set_group_special_title(group_id, user_id, special_title=None, duration=-1):
        """
        设置群组专属头衔
        :param group_id: 群号
        :param user_id: 要设置的 QQ 号
        :param special_title: 专属头衔，不填或空字符串表示删除专属头衔
        :param duration: 专属头衔有效期，单位秒，-1 表示永久，不过此项似乎没有效果，可能是只有某些特殊的时间长度有效，有待测试
        :return: json
        """
        return MsgBuilder.build('set_group_special_title', {
            'group_id': group_id,
            'user_id': user_id,
            'special_title': special_title,
            'duration': duration
        })

    @staticmethod
    def set_discuss_leave(discuss_id):
        """
        退出讨论组
        :param discuss_id: 讨论组 ID（正常情况下看不到，需要从讨论组消息上报的数据中获得）
        :return: json
        """
        return MsgBuilder.build('set_discuss_leave', {
            'discuss_id': discuss_id
        })

    @staticmethod
    def set_friend_add_request(flag, approve=True, remark=None):
        """
        处理加好友请求
        :param flag: 加好友请求的 flag（需从上报的数据中获得）
        :param approve: 是否同意请求
        :param remark: 添加后的好友备注（仅在同意时有效）
        :return: json
        """
        return MsgBuilder.build('set_friend_add_request', {
            'flag': flag,
            'approve': approve,
            'remark': remark
        })

    @staticmethod
    def set_group_add_request(flag, sub_type, approve=True, reason=None):
        """
        处理加群请求／邀请
        :param flag: 加群请求的 flag（需从上报的数据中获得）
        :param sub_type: add 或 invite，请求类型（需要和上报消息中的 sub_type 字段相符）
        :param approve: 是否同意请求／邀请
        :param reason: 拒绝理由（仅在拒绝时有效）
        :return: json
        """
        return MsgBuilder.build('set_group_add_request', {
            'flag': flag,
            'sub_type': sub_type,
            'approve': approve,
            'reason': reason
        })

    @staticmethod
    def get_login_info():
        """
        获取登录号信息
        :return: json
        """
        return MsgBuilder.build('get_login_info', {})

    @staticmethod
    def get_stranger_info(user_id, no_cache=False):
        """
        获取陌生人信息
        :param user_id: QQ 号
        :param no_cache: 是否不使用缓存（使用缓存可能更新不及时，但响应更快）
        :return: json
        """
        return MsgBuilder.build('get_stranger_info', {
            'user_id': user_id,
            'no_cache': no_cache
        })

    @staticmethod
    def get_group_list():
        """
        获取群列表
        :return: json
        """
        return MsgBuilder.build('get_group_list', {})

    @staticmethod
    def get_group_member_info(group_id, user_id, no_cache=False):
        """
        获取群成员信息
        :param group_id: 群号
        :param user_id: 群号
        :param no_cache: 是否不使用缓存（使用缓存可能更新不及时，但响应更快）
        :return: json
        """
        return MsgBuilder.build('get_group_member_info', {
            'group_id': group_id,
            'user_id': user_id,
            'no_cache': no_cache
        })

    @staticmethod
    def get_group_member_list(group_id):
        """
        获取群成员列表
        :param group_id: 群号
        :return: json
        """
        return MsgBuilder.build('get_group_member_list', {
            'group_id': group_id
        })

    @staticmethod
    def get_cookies():
        """
        获取 Cookies
        :return: json
        """
        return MsgBuilder.build('get_cookies', {})

    @staticmethod
    def get_csrf_token():
        """
        获取 CSRF Token
        :return:
        """
        return MsgBuilder.build('get_csrf_token', {})

    @staticmethod
    def get_credentials():
        """
        获取 QQ 相关接口凭证
        :return:
        """
        return MsgBuilder.build('get_credentials', {})

    @staticmethod
    def get_record(file, out_format, full_path=False):
        """
        获取语音
        :param file: 收到的语音文件名（CQ 码的 file 参数），如 0B38145AA44505000B38145AA4450500.silk
        :param out_format: 要转换到的格式，目前支持 mp3、amr、wma、m4a、spx、ogg、wav、flac
        :param full_path: 是否返回文件的绝对路径（Windows 环境下建议使用，Docker 中不建议）
        :return: json
        """
        return MsgBuilder.build('get_record', {
            'file': file,
            'out_format': out_format,
            'full_path': full_path
        })

    @staticmethod
    def get_image(file):
        """
        获取图片
        :param file: 收到的图片文件名（CQ 码的 file 参数），如 6B4DE3DFD1BD271E3297859D41C530F5.jpg
        :return: json
        """
        return MsgBuilder.build('get_image', {
            'file': file
        })

    @staticmethod
    def can_send_image():
        """
        检查是否可以发送图片
        :return: json
        """
        return MsgBuilder.build('can_send_image', {})

    @staticmethod
    def can_send_record():
        """
        检查是否可以发送语音
        :return:
        """
        return MsgBuilder.build('can_send_record', {})

    @staticmethod
    def get_status():
        """
        获取插件运行状态
        :return: json
        """
        return MsgBuilder.build('get_status', {})

    @staticmethod
    def get_version_info():
        """
        获取酷 Q 及 HTTP API 插件的版本信息
        :return: json
        """
        return MsgBuilder.build('get_version_info', {})

    @staticmethod
    def set_restart(clean_log=False, clean_cache=False, clean_event=False):
        """
        重启酷 Q，并以当前登录号自动登录（需勾选快速登录）
        :param clean_log: 是否在重启时清空酷 Q 的日志数据库（logv1.db）
        :param clean_cache: 是否在重启时清空酷 Q 的缓存数据库（cache.db）
        :param clean_event: 是否在重启时清空酷 Q 的事件数据库（eventv2.db）
        :return: json
        """
        return MsgBuilder.build('set_restart', {
            'clean_log': clean_log,
            'clean_cache': clean_cache,
            'clean_event': clean_event
        })

    @staticmethod
    def set_restart_plugin(delay=0):
        """
        重启 HTTP API 插件
        :param delay: 要延迟的毫秒数，如果默认情况下无法重启，可以尝试设置延迟为 2000 左右
        :return: json
        """
        return MsgBuilder.build('set_restart_plugin', {
            'delay': delay
        })

    @staticmethod
    def clean_data_dir(data_dir):
        """
        清理数据目录
        :param data_dir: 收到清理的目录名，支持 image、record、show、bface
        :return: json
        """
        return MsgBuilder.build('clean_data_dir', {
            'data_dir': data_dir
        })

    @staticmethod
    def clean_plugin_log():
        """
        清理插件日志
        :return:
        """
        return MsgBuilder.build('clean_plugin_log', {})

    """试验性API"""

    @staticmethod
    def get_friend_list(flat=False):
        """
        获取好友列表
        :param flat: 是否获取扁平化的好友数据，即所有好友放在一起、所有分组放在一起，而不是按分组层级
        :return: json
        """
        return MsgBuilder.build('_get_friend_list', {
            'flat': flat
        })

    @staticmethod
    def get_group_info(group_id):
        """
        获取群信息
        :param group_id: group_id
        :return: json
        """
        return MsgBuilder.build('_get_group_info', {
            'group_id': group_id
        })

    @staticmethod
    def get_vip_info(user_id):
        """
        获取会员信息
        :param user_id: 要查询的 QQ 号
        :return: json
        """
        return MsgBuilder.build('_get_vip_info', {
            'user_id': user_id
        })

    """隐藏API"""

    @staticmethod
    def check_update(automatic=False):
        """
        检查更新
        :param automatic: 是否自动进行，如果为 true，将不会弹窗提示，而仅仅输出日志，同时如果 auto_perform_update 为 true，则会自动更新并重启酷 Q
        :return: json
        """
        return MsgBuilder.build('.check_update', {
            'automatic': automatic
        })

    @staticmethod
    def handle_quick_operation(context, operation):
        """
        对事件执行快速操作
        :param context: 事件上报的数据对象
        :param operation: 快速操作对象，例如 {"ban": true, "reply": "请不要说脏话"}
        :return: json
        """
        return MsgBuilder.build('.handle_quick_operation', {
            'context': context,
            'operation': operation
        })


class MsgSender(object):
    @staticmethod
    def send(message):
        """
        消息放到发送队列里
        :param message: 消息内容
        :return: bool
        """
        return Core.SQ.put_nowait(message)


class MsgHandle(object):
    @staticmethod
    def decode(message):
        """
        处理消息
        :param message: 消息内容
        :return: array
        """
