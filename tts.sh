curl "https://openapi.naver.com/v1/voice/tts.bin" \
	-d "speaker=mijin&speed=0&text=안녕!" \
	-H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
	-H "X-Naver-Client-Id: {aCK77tlt3QgmepTETONi}" \
	-H "X-Naver-Client-Secret: {7kA9fpuTAw}" -v \
		> out.mp3
