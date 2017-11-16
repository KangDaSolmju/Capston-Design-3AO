#!/bin/bash
#echo "Recording... 4[sec] Press Ctrl+C to Stop."

arecord -D "plughw:1,0" -f S16_LE -t wav -r 16000 -d 4 > test.wav

curl -o newstt.txt -X POST --data-binary @test.wav --header "Content-Type: audio/116; rate=16000;" "https://www.google.com/speech-api/v2/recognize?output=json&lang=ko&key=AIzaSyC0SpDwgok-dLZrQtiAbdx1bA3p4_TCWNk"

#cat newstt.txt | cut -d$'\n' -f2 | cut -d : -f4 | cut -d , -f1 | cut -d \" -f2
#rm test.wav > /dev/null 2>&1
