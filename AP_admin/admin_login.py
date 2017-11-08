# coding=utf8
import os
import sys
import commands
import time
import random

# 부팅 시 맨 처음 자동으로 수행되는 스크립트.
# 3개의 질문을 0.5초의 텀을 두고 랜덤으로 연속해서 던진다.(그러면 사용자는 답 3개를 연속하여 말한다.)
# 사용자가 답한 것을 파일로 저장한다. (-> 음성인식이 어떻게 되는지는 두고봐야 할듯...)

class Login:
	def admin_login(self):
		# random number
		question_number=random.sample(range(1,4),3)
		
		# ask to user
		question_list=[]
		for i in question_number:
			(status1,question)=commands.getstatusoutput("sed -n "+str(i)+"p questions")
			if status1==0:
				question_list.append(question)
		num=1
		for question in question_list:
			os.system("curl -d 'speaker=jinho&speed=0&text="+question+"' 'https://openapi.naver.com/v1/voice/tts.bin' -H 'Content-Type: application/x-www-form-urlencoded' -H 'X-Naver-Client-Id: wY8qYOdN9FzbBBrgtlF3' -H 'X-Naver-Client-Secret: _dblCskdHA' > Q_"+str(num)+".mp3")
			num=num+1
		

		'''
		answer_list=[]
		for i in range(0,3):
			(status2, answer)=commands.getstatusoutput("echo '정답"+str(i)+"'")# 음성인식 수행하여 answer리스트에 넣기
			if status1==0:
				answer_list.append(answer)
			time.sleep(0.5)
		print(answer_list)
		'''
if __name__ == "__main__":
	login=Login()
	login.admin_login()
