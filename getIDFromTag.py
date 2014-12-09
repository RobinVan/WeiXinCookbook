#-*-coding:utf-8-*-
import urllib2, json, appKey, MySQLdb

def getIDFromTag(tag):
    APPKEY = APPKEY = appKey.APPKEY
    url = 'http://apis.juhe.cn/cook/index?key=' + APPKEY + '&cid=' + tag + '&rn=5'
    id_list = []
    db = MySQLdb.connect(host='localhost',user='root',passwd='lxb',db='caipu',charset='utf8')
    cursor = db.cursor()
    count = cursor.execute("""select * from getIDByTag where tag = %s""",(tag,))
    if count == 0 :
        try:
            res = urllib2.urlopen(url)
            res_read_uni = res.read().decode("utf-8-sig")
            data = json.loads(res_read_uni)
            reason = data['reason']
            if reason == 'Success':
                result = data['result']['data']
                for caipu in result:
                    id_list.append(caipu['id'])
                    cursor.execute("""insert into getIDByTag values(%s,%d)""",(tag, caipu['id']))
                db.commit()
                print 'get ID from tag success'
            else:
                print 'get ID from tag ERROR'
        except urllib2.URLError,e:
            print e.reason
    else:
        id_all = cursor.fetchall()
        for id in id_all:
            id_list.append(id[1])
    cursor.close()
    db.close()
    return id_list
