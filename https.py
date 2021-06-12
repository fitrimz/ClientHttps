import requests


##request connection
s = requests.Session()
s.verify = '/home/nial/httpsClient/cert.pem'

req = requests.get('https://192.168.1.22:4443'
		, verify='/home/nial/httpsClient/cert.pem')

print(req)

z = input('\n Data Retrived!! Please name it: ')
with open (z,'w') as f:
	f.write(req.text)





s.close()
