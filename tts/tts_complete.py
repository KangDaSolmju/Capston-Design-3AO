# coding=utf8
import sys
import os

# 2017.11.10 complete
os.system("curl -d 'speaker=jinho&speed=0&text=안녕하세요 저는 강다솔입니다.' 'https://openapi.naver.com/v1/voice/tts.bin' -H 'Content-Type: application/x-www-form-urlencoded' -H 'X-Naver-Client-Id: wY8qYOdN9FzbBBrgtlF3' -H 'X-Naver-Client-Secret: _dblCskdHA' > tts.wav")
