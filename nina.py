import json
import requests
from bs4 import BeautifulSoup
code =int(input('room code: '))
req = requests.get('https://api.quizit.online/quizizz/answers', params={'pin':code})
req1 = json.loads(req.text)
print(req)
if req.status_code =200:
	print(req1['message'])
	data = req1["data"]
	answers = data["answers"]
	question_count =len(answers)
	dick ={}
	for i in range(0,question_count):
		print(str(i) +".")
		dick["count"+str(i)]=answers[i]
		a = dict(dick["count"+str(i)])
		b =a['answers']
		c=a['question']
		d =c['text']
		print("question: " +str(d[d.find('<p>')+3 : d.find('</p>')]))
		print("answer: "+ str(a['answers']))
		print("type: "+str(a['type']))
	print("number of questions: "+str(question_count))
else:
	print('Unexpected responce.Room code is not correct or our servers are down')
