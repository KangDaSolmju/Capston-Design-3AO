# coding=utf8

import os
import sys
class Block:
	def block_mac(self):
		print("block mac")

if __name__=="__main__":
	try:
		if sys.argv[1]=="1":
			block=Block()
			block.block_mac()	
	except:
		#os.system("omxplayer please_admin.mp3")
		sys.exit(1)
