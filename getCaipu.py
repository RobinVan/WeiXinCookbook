#-*-coding:utf-8-*-
import urllib2, json, chardet, os, MySQLdb, appKey

def getCaipu(id):
    APPKEY = APPKEY = appKey.APPKEY
    url = 'http://apis.juhe.cn/cook/queryid?key=' + APPKEY + '&id='
    db = MySQLdb.connect(host='localhost',user='root',passwd='lxb',db='caipu',charset='utf8')
    cursor = db.cursor()
    '''
    db.set_character_set('utf8')

    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')
    '''
    count = cursor.execute("""select * from caipu where id = %s""",(id,))
    caipu_information = {}
    #if not(os.path.isfile('json/' + 'caipu' + str(id) + '.json')) :
    if count == 0 :
        try:
            res = urllib2.urlopen(url + str(id))
            res_read_uni = res.read().decode("utf-8-sig")
            #unicode.encode(res_read_uni, "utf-8")
            #print chardet.detect(res_read_uni)
            #jsonFile = open('json/' + 'caipu' + str(id) + '.json', 'w')
            #jsonFile.write(unicode.encode(res_read_uni, 'utf-8'))
            data = json.loads(res_read_uni)
            reason = data['reason']
            if reason == 'Success':
                result = data['result']['data']
                caipu = result[0]
                url = 'http://104.131.156.81/' + 'caipu' + str(id)
                #print chardet.detect(caipu['title'])
                #print chardet.detect(caipu['title'].decode("ascii"))
                #cursor.execute("""insert into caipu values(%s,%s,%s,%s,%s)""",(id, caipu['title'].decode("utf-8"), caipu['imtro'].decode("utf-8"), caipu['albums'][0], url,))
                #cursor.execute("""insert into caipu values(%s,%s,%s,%s,%s)""",(id, '', '', caipu['albums'][0], url,))
                cursor.execute("""insert into caipu values(%s,%s,%s,%s,%s)""",(id, caipu['title'], caipu['imtro'], caipu['albums'][0], url,))
                db.commit()
                f = open('templates/' + 'caipu' + str(id) + '.html', 'w')
                f.write(unicode.encode(u'<meta http-equiv="Content-Type" content="width=device-width, initial-scale=1, charset=utf-8"/>\n', 'utf-8'))
                f.write(unicode.encode('<center><h2>' + caipu['title'] + '</h2></center>\n', 'utf-8'))
                #caipu_information['title'] = caipu['title']
                f.write(unicode.encode('<p>' + caipu['imtro'] + '</p>\n', 'utf-8'))
                #caipu_information['description'] = caipu['imtro']
                f.write(unicode.encode(u'主料' + '<p>' + caipu['ingredients'] + '</p>\n', 'utf-8'))
                f.write(unicode.encode(u'配料' + '<p>' + caipu['burden'] + '</p>\n', 'utf-8'))
                f.write(unicode.encode(u'<p>\n', 'utf-8'))
                for image in caipu['albums']:
                    f.write(unicode.encode('<img src = ' + '"' + image + '"' + '/>\n', 'utf-8'))
                f.write(unicode.encode(u'</p>\n', 'utf-8'))
                f.write(unicode.encode(u'<p>\n', 'utf-8'))
                for step in caipu['steps']:
                    f.write(unicode.encode('<img src = ' + '"' + step['img'] + '"' + '/>\n', 'utf-8'))
                    f.write(unicode.encode(u'<br>\n', 'utf-8'))
                    f.write(unicode.encode(step['step'] + '\n', 'utf-8'))
                    f.write(unicode.encode(u'<br>\n', 'utf-8'))
                f.write(unicode.encode(u'</p>\n', 'utf-8'))
                f.close()
                caipu_information['title'] = caipu['title']
                caipu_information['description'] = caipu['imtro']
                #caipu_information['picurl'] = 'null'
                caipu_information['picurl'] = caipu['albums'][0]
                caipu_information['url'] = url
                print 'get caipu Success'
            else:
                print 'get caipu ERROR'
        except urllib2.URLError,e:
            print e.reason
    else:
        #jsonFile = file('json/' + 'caipu' + str(id) + '.json')
        #data = json.load(jsonFile)
        #result = data['result']['data']
        #caipu = result[0]
        #print count
        #caipu_all = cursor.fetchall()
        #print caipu_all
        #for caipu in caipu_all:
        caipu = cursor.fetchone()
        caipu_information['title'] = caipu[1]
        caipu_information['description'] = caipu[2]
        #caipu_information['picurl'] = 'null'
        caipu_information['picurl'] = caipu[3]
        caipu_information['url'] = caipu[4]
    cursor.close()
    db.close()

    return caipu_information
