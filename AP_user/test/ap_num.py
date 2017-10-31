# coding=utf8
import re
import os
import sys
import command

# 사용자 수를 구하는 클래스이다.
# 사용자가 '사용자 수가 뭐야?'라는 질문을 던지면 이 파일이 실행된다.
# 그리고 이 파일은 user json파일을 만들어서 맥주소와 admin, guest를 구분한다.
# --> 확실하진 않음....
def UserNum:
	# 밑에서 부터 DHCPACK를 찾으면 해당 행을 공백으로 쪼개서 리스트로 만든다.
	def make_dhcp_list(self):
		dhcpack_list=[]
		(line_status,lines)=commands.getstatusoutput("cat user.log | wc -l")
		for line in range(lines,0,-1):
			(status,dhcpack)=commands.getstatusoutput("cat test/user.log | sed -n "+str(line)+"p")
			dhcp_ack=re.split(" ",dhcpack)
			dhcpack_list.append(dhcp_ack)
		return dhcpack_list
	

	# 커다란 리스트를 돌면서 맥주소 중복이 있다면 가장 최근 라인 넘버만 남기고 나머지는 삭제한다.
	# user.log에서 disassociated에 해당하는 행의 맥주소와 dhcpack_list[][7]와 비교하면서 같은 것이 있으면 dhcpack_list에서 삭제한다.
	# 최종 dhcpack_list가 실제 공유기 사용자들 리스트이다.
	def make_real_userlist(self, dhcpack_list):
				

if __name__=="__main__":
	dhcpack_list=[]
	un=UserNum()
	dhcpack_list=un.make_dhcp_list()
	un.make_real_userlist(dhcpack_list)
