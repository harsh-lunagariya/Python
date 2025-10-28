import requests
import time

# r = requests.get('https://xkcd.com/353/')

# res = r.text

# # print(help(r))

# r = requests.get('https://imgs.xkcd.com/comics/python.png')

# # with open('comic.png','wb') as f:
# #     f.write(r.content)

# print(r.status_code)
# print(r.ok)
# print(r.headers)

# payload = {'page':2,'count':25}

# r = requests.get("http://httpbin.org/get",params=payload)

# print(r.text)
# print(r.url)

# payload = {'username':'harsh', 'password': 'testing'}

# r = requests.post("http://httpbin.org/post",data=payload)

# print(r.json())


# r = requests.get("https://httpbin.org/basic-auth/corey/test",auth=('corey','test2'))

# print(r.text)
# print(r.status_code)

s=time.time()
r = requests.get('https://httpbin.org/delay/1',timeout=12)

e=time.time()
print(r.text,e-s)