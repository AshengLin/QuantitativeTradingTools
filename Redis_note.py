'''
WSL > Docker > Redis
In-memory方式儲存資料，適合短時間資料操作，當快取cache使用
'''

import redis
#建立連線，port指定剛才在Docker中所設定的port，並將decode_responses設為True，讓取得資料時自動decode
r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
r.set('myName', 'Mike') #存入key及value
r.set('中文的key', '中文的value') #存入資料，key可以是中文
print(r)
print(r.get('myName')) #輸入key值來取得剛
print(r.get('中文的key'))