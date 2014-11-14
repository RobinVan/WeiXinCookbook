# -*- coding: utf-8 -*-

f = open('urlHandler.py', 'w')

for i in range(1, 80453):
    f.write('class caipu' + str(i) + ':\n')
    f.write('    def GET(self):\n')
    f.write('        return render.caipu' + str(i) + '()\n')
