"""


import requests
import urllib.parse
pa1={
    'tid':442148395,
    'user_input':'["$abc$","$123abc$"]'
}
pa2={
    'tid':442194757,
    'user_input':'["$\\angle ABC$","$\\angle ABC$"]'
}

url1 = 'http://192.168.14.211:8211?' + urllib.parse.urlencode(pa1)

url2 = 'http://192.168.14.211:8211?' + urllib.parse.urlencode(pa2)

r1=requests.get(url1)
r2=requests.get(url2)

print(r1.status_code)
print(r2.status_code)
"""


def abc(number):
    if number<=0:
        return 0
    elif number==1:
        return 1
    elif number==2:
        return 2
    else:
        return abc(number-1)+abc(number-2)

if __name__=='__main__':
    print(abc(4.5))