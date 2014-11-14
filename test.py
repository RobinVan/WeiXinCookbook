# -*- coding: utf-8 -*-

import sys, urllib, httplib, time

# 配置
interface_url = '104.131.156.81'
interface_path = '/'
text='''<xml><ToUserName><![CDATA[664587718]]></ToUserName>
<FromUserName><![CDATA[123456789]]></FromUserName>
<CreateTime>1348831860</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
<MsgId>1234567890123456</MsgId>
</xml>'''
def make_post(action):
    conn = httplib.HTTPConnection(interface_url)
    post_data = text % action
    headers = { "Content-type": "text/xml","Content-Length": "%d" % len(post_data)}
    conn.request("POST", interface_path,"", headers)
    print post_data
    conn.send(post_data)
    response = conn.getresponse()
    #print response.status, response.reason
    print response.read()
    conn.close()

def post_event():
    '''模拟订阅'''
    conn = httplib.HTTPConnection(interface_url)
    post_data = '''<xml>
<ToUserName><![CDATA[664587718]]></ToUserName>
<FromUserName><![CDATA[123456789]]></FromUserName>
<CreateTime>1348831855</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[subscribe]]></Event>
</xml>'''
    headers = { "Content-type" : "event","Content-Length": "%d"%len(post_data)}
    conn.request("POST", interface_path,"",headers)
    print "Subscribed!"
    print post_data
    conn.send(post_data)
    response = conn.getresponse()
    print response.read()
    conn.close()

def main(argv):
    post_event()
    while True:
        content=raw_input("Input your test message:\n")
        make_post(content)

main(sys.argv)
