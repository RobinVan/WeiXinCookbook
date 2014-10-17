# -*- coding: utf-8 -*-
import hashlib
import web
import time
import os
import urllib2,json
import chardet
import tags, getCaipu, getIDFromTag, getIDFromName, urls, urlHandler
from wechat_sdk import WechatBasic

urls = urls.urls

token='babalaile'
signature = 'f24649c76c3f3d81b23c033da95a7a30cb7629cc'  # Request 中 GET 参数 signature
timestamp = '1406799650'  # Request 中 GET 参数 timestamp
nonce = '1505845280'  # Request 中 GET 参数 nonce
# 实例化 wechat
wechat = WechatBasic(token=token)

class WeixinInterface:

    def GET(self):
        global data, signature, nonce, echostr
        data = web.input()
        signature = data['signature']
        timestamp = data['timestamp']
        nonce = data['nonce']
        echostr = data['echostr']

    def POST(self):
        body_text = web.data()
        # 对签名进行校验
        #if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
        # 对 XML 数据进行解析 (必要, 否则不可执行 response_text, response_image 等操作)
        wechat.parse_data(body_text)
        # 获得解析结果, message 为 WechatMessage 对象 (wechat_sdk.messages中定义)
        message = wechat.get_message()
        #print message.content
        #print chardet.detect(message.content)
        response = None
        id_list = []
        if message.type == 'text':
            if message.content in tags.tags.keys():
                #response = wechat.response_text(tags.tags[message.content])
                id_list = getIDFromTag.getIDFromTag(tags.tags[message.content])
            else:
                id_list = getIDFromName.getIDFromName(message.content)
        if id_list:
            news_list = []
            for id in id_list:
                caipu = getCaipu.getCaipu(id)
                news_map = {
                    'title': caipu['title'],
                    'description': caipu['description'],
                    'picurl': caipu['picurl'],
                    'url': caipu['url']
                }
                news_list.append(news_map)
            response = wechat.response_news(news_list)
        else:
            response = wechat.response_text(u'不能识别')
        # 现在直接将 response 变量内容直接作为 HTTP Response 响应微信服务器即可，此处为了演示返回内容，直接将响应进行输出
        #print response
        return response
        #else:
        #print 'error'

if __name__ == '__main__':
    app = web.application(urls , globals())
    app.run()
