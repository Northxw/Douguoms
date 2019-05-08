import requests
import random

def xproxy():
    API = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=a31f8cd494e343d69b51b303859ac446&orderno=YZ2018112517118ojIuo&returnType=2&count=5'
    results = requests.get(url=API).json()['RESULT']
    agents = ["http://{}:{}".format(res['ip'], res['port']) for res in results]
    proxies = {
        "http": random.choice(agents),
        "https": random.choice(agents)
    }
    return proxies

def aproxy():
    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": "http-dyn.abuyun.com",
        "port": "9020",
        "user": "H41U96QG1N0046PD",     # Pass certificate
        "pass": "D504F6AA252E4D30"      # Pass key
    }
    proxies = {
        "http": proxyMeta,
        "https": proxyMeta
    }
    return proxies

if __name__ == '__main__':
    print(aproxy())