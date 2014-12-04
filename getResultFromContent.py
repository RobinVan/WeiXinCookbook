from wechat_sdk import WechatBasic

def getResult(content):
    if content in tags.tags.keys():
        #response = wechat.response_text(tags.tags[content])
        id_list = getIDFromTag.getIDFromTag(tags.tags[content])
    else:
        id_list = getIDFromName.getIDFromName(content)
    if id_list:
        news_list = []
        for id in id_list:
            caipu = getCaipu.getCaipu(id)
            news_map = {
                'title': caipu['title'],
                'description': caipu['description'],
                'picurl': caipu['picurl'],
                #'url':'http://104.131.156.81/test'
                'url': caipu['url']
            }
        news_list.append(news_map)
    response = wechat.response_news(news_list)
    return response
