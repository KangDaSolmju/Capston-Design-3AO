import os
import sys

# 2017.10.30 complete
# stop
os.system("service hostapd stop")
os.system("service dnsmasq stop")

# start
# ifdown ifup
os.system("ifdown wlan0; sudo ifup wlan0")

# restart dnsmasq
os.system("service dnsmasq start")

# restart hostapd
os.system("service hostapd start")


os.system("curl -d 'speaker=jinho&speed=0&text=restart가 정상적으로 이루어졌습니다.' 'https://openapi.naver.com/v1/voice/tts.bin' -H 'Content-Type: application/x-www-form-urlencoded' -H 'X-Naver-Client-Id: wY8qYOdN9FzbBBrgtlF3' -H 'X-Naver-Client-Secret: _dblCskdHA' > restart_result.mp3")
