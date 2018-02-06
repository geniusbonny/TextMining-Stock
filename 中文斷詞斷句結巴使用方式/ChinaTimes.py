import jieba

#匯入辭庫(將讀取的路徑寫下來)

jieba.load_userdict("C:\\Users\\genio\\TSMC\\WordBank.txt")  

#讀取文章(將讀取的路徑寫下來)

ret = open("C:\\Users\\genio\\TSMC\\TSMC_1001.txt", "r").read()

#結巴段詞斷句

seglist = jieba.cut(ret, cut_all=False)

#算段詞斷句字頻，並輸出成csv檔

import csv

hash = {}

for item in seglist:
    if item in hash:
        hash[item] +=1
    else:
        hash[item] =1

fa = open("count.csv", "w")

for k in hash:
    fa.write("%s,%d\n"%(k,hash[k]))

fa.close()