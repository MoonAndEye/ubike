# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 15:53:40 2016
"""
import urllib.request
import datetime
import json
import pandas as pd
import gzip


d0 = datetime.datetime.now() #d0 是今天
d0 = d0.strftime("%Y-%m-%d_%H%M%S")



file_name = "test.gz"

url = 'http://data.taipei/youbike'

#urllib.request.urlretrieve(url, file_name)
response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
data = gzip.decompress(data) # data在這一步還是 byte
data = data.decode("utf-8") #到這一步才能把 byte 轉成 string

#print(data)

text1 = json.loads(data)

rawResult = text1["retVal"]

"""
#以下不需要了,直接用 DataFrame.T 行列互換
key01 = rawResult['0001']


rawKeys = []
for each in rawResult.keys():
    rawKeys.append(each)

rawKeys.sort()

csvColVal = [each for each in rawResult[rawKeys[0]].keys()]

csvColVal.sort() #這就是之後寫到csv的item
#csvColVal.append("id") #這一項目不用,dic裡面的"sno"就是停車場id
"""

b4csv = pd.DataFrame(data = rawResult)
b4csv = b4csv.T

file_path = 'C:/1save/ubike/'

csvName = d0 + ".csv"

b4csv.to_csv(file_path + csvName)

"""
b4csv = pd.DataFrame(result)

b4csv["availablecar"]  = b4csv["availablecar"].astype(int)

b4csv = b4csv[b4csv.availablecar != -9]
b4csv = b4csv[b4csv.availablecar != 9999]


b4csv = pd.DataFrame.reset_index(b4csv)

b4csv = b4csv.drop("index", 1)

aftcsv = pd.DataFrame.to_csv(b4csv)



csv_file = open(file_path + str(d0)+'.csv', 'w', encoding = 'utf-8' )

csv_file.write(aftcsv)

csv_file.close()

print ('The ' + str(d0) + ' is done')
"""

"""
aftcsv = pd.DataFrame.to_csv(b4csv)
csv_file = open(file_path + str(d0)+'.csv', 'w', encoding = 'utf-8' )
csv_file.write(aftcsv)
csv_file.close()
print ('The ' + str(d0) + ' is done')
"""
