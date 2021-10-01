# pip install speedtest-cli
# Do not use pip install speedtest
#use pip install speedtest-cli ,happy coding
import speedtest
wifi  = speedtest.Speedtest()
print("Internet Download Speed is", wifi.download(),"bit")
print("Internet Upload Speed is", wifi.upload(),"bit")
