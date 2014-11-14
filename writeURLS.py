# -*- coding: utf-8 -*-

f = open('urls.py', 'w')

for i in range(1, 80453):
    f.write('\'/caipu' + str(i) + '\',\'urlHandler.caipu' + str(i) + '\',\n')
