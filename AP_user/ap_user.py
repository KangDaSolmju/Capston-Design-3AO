# coding=utf8
import os 
import sys
import commands
import time
# userlist를 만든다. userlist는 DHCP를 할당받거나 disassociated한 기록이 담겨 있다. userlist에서 사용자의 맥주소를 알 수 있음
class Daemon:
	def check_line(self): 
		(line_status, lines)=commands.getstatusoutput("cat /var/log/daemon.log|wc -l")
		while(1):
			(line_status2, lines2)=commands.getstatusoutput("cat /var/log/daemon.log|wc -l")
			if int(lines)<int(lines2):
				print('different')
				line_num=int(lines2)-int(lines) #추가된 라인 수
				os.system("tail -"+str(line_num)+" /var/log/daemon.log | grep -w 'DHCPACK\|IEEE 802.11: disassociated' > ./userlist.dat")
				lines=lines2
			time.sleep(1)
			
if __name__ == "__main__":
	d=Daemon()
	d.check_line()
