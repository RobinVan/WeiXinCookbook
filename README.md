##功能

这是查看菜谱微信号后台程序，运行效果如下：

![](/files/01.png)

功能为用户输入食材名，如“牛肉”，“西瓜”，“黄瓜”，或菜谱的特点，如“清凉”，“辣”，公众号可返回符合用户要求的菜谱，点即可查看。

数据是通过[聚合数据](http://www.juhe.cn/)的API接口得到，第一次得到数据后储存在数据库中，下次请求直接从数据库获得数据即可。

##使用方法

关注公共号lufooo，输入菜名即可。扫二维码也可关注：

![](/files/02.jpg)

##运行环境

将所有代码托管到服务器上，设定好微信公共号的服务器地址，服务器要求有以下python库：wechat_sdk，chardet，MySQLdb。将appKey.py里的APPKEY替换为你在[聚合数据](http://www.juhe.cn/)申请的APPKEY。执行下面语句:

	sudo python webApp.py 80

即可在你的微信公共号里查询菜谱。

本项目提供API接口，运行：

	python api.py 8000(任意未被占用的端口号)

访问服务器的域名+端口号，得到JSON格式数据。

如果想用数据库存储菜谱信息，请参考getCaipu.py，getIDFromTag.py，getIDFromName.py里操作数据库的语句，在服务器上创建对应的数据库，如果使用数据库时遇到关于编码的问题，可以参考[我的博客](http://lufo816.github.io/2014/12/01/PythonMySQL.html)。
