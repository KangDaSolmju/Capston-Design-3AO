#!/bin/bash
#echo Recording... *press Ctrl+c to stop 

arecord -D "plughw:1,0" -f S16_LE -t wav -r 16000 -d 4 > test.wav





curl -o "stt.txt" -X Post --data-binary @test.wav --header "Content-Type: audio/116; rate=16000;" "http://www.google.com/speech-api/v2/recognize?output=json&lang=ko&key=AIzaSyAh01vT98fp-5qLrFYFcMVzFK1AwBV7WCo"

cat "stt.txt" 
rm test.wav > /dev/null 2>&1    
