import re; import urllib.request

url = urllib.request.urlopen('https://sites.google.com/site/gruposcoutsanbruno1/principal/noticias/lista-actualizada-mails')
data = str(url.read())

p = re.compile(r'[\w\,\;\.\:\-\_]+[@]\w+[.]\w+')
m = p.finditer(data)
for d in m: print(d.group())