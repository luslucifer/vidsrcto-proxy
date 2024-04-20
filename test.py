import re

url = 'http://127.0.0.1:5000/fetch?url=https://gamn.v44381c4b81.site/_v2-pvzv/12a3c523f9105800ed8c394685aeeb0bc22eaf5c15bbbded021e7baea93ece832257df1a4b6125fcfa38c35da05dee86aad28d46d73fc4e9d4e5a23a5271f0d631c612e30918b40914c3f4ee3f107d122631832f445560c69b8dbc08c7e06cd23e0fe14d5636ea56bcea6611b65b0296ea2a/h/list;15a38634f803584ba8926411d7bee906856cab0654b5bfb3.m3u8'
pattern = r'\/h\/list'

splited = url.split('a')

for i,word in enumerate(splited):

    print(f'index{i} and word = {word}')