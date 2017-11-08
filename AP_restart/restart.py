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
