#-*-coding:utf-8-*-
import urllib2, json, chardet, appKey

APPKEY = appKey.APPKEY
url = 'http://apis.juhe.cn/cook/category?key=' + APPKEY
try:
    res = urllib2.urlopen(url)
    res_read_uni = res.read().decode("utf-8-sig")
    data = json.loads(res_read_uni)
    information = data['result']
    f = open('tags.py', 'w')
    f.write('tags = {\n')
    for parentID in information:
        tagInformation = parentID['list']
        for tag in tagInformation:
            f.write(unicode.encode('u"' + tag['name'] + '":"' + tag['id'] + '",\n', 'utf-8'))
    f.write('}\n')
    f.close()
except urllib2.URLError,e:
    print e.reason
