#-*-coding:utf-8-*-
import urllib2, json, chardet

def getIDFromName(name):
    APPKEY = '772138d3588d780c86591a4eedf0f634'
    url = 'http://apis.juhe.cn/cook/query?key=' + APPKEY + '&menu=' + name.encode('utf-8') + '&rn=5'
    id_list = []
    try:
        res = urllib2.urlopen(url)
        res_read_uni = res.read().decode("utf-8-sig")
        data = json.loads(res_read_uni)
        reason = data['reason']
        if reason == 'Success':
            result = data['result']['data']
            for caipu in result:
                id_list.append(caipu['id'])
            print 'get ID from tag success'
        else:
            print 'get ID from tag ERROR'
    except urllib2.URLError,e:
        print e.reason
    return id_list
