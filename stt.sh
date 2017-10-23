#!/bin/bash
echo Recording... *press Ctrl+c to stop 
arecord -D "plughw:1,0" -t wav -r 16000 -d 4 > test.wav

