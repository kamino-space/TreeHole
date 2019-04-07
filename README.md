# TreeHole
一个不会说话的QQ机器人

## 功能介绍
- 记录下你发给它的消息
- web端可以查看它记录的消息

## 使用方法
#### 下载酷Q机器人
地址: https://cqp.cc/
#### 下载安装coolq-http-api插件
地址: https://github.com/richardchien/coolq-http-api/releases  
下载[io.github.richardchien.coolqhttpapi.cpk](https://github.com/richardchien/coolq-http-api/releases/download/v4.8.0/io.github.richardchien.coolqhttpapi.cpk),放入酷Q app文件夹  
#### 登录机器人,修改配置文件
插件配置文件在 酷Q Air\data\app\io.github.richardchien.coolqhttpapi\config\机器人QQ号.json
修改下面几个参数
```json
{
    "ws_reverse_api_url": "ws://127.0.0.1:8000/api",
    "ws_reverse_event_url": "ws://127.0.0.1:8000/event",
    "use_ws_reverse": true
}
```
重启插件
#### 启动服务端
```bash
git clone https://github.com/kamino-space/TreeHole.git
cd TreeHole
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8000
```

## 隐私策略
数据使用AES加密保存，使用SSL加密传输，安全得很。

## 协议
MIT