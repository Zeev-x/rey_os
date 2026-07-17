# wifi.py
import network
import time

wlan = network.WLAN(network.STA_IF)

def connect(ssid, password, ip=None, gateway=None, subnet=None, dns=None):
    wlan.active(False)
    time.sleep(0.5)
    wlan.active(True)

    print("Connecting:", ssid)
    wlan.connect(ssid, password)

    timeout = 20
    while not wlan.isconnected() and timeout > 0:
        #print("Waiting WiFi...")
        time.sleep(1)
        timeout -= 1

    if wlan.isconnected():
        if ip and subnet and gateway and dns:
            try:
                wlan.ifconfig((ip, subnet, gateway, dns))
            except Exception as e:
                print("Static IP failed:", e)
        print("WiFi Connected")
        print("IP:", wlan.ifconfig()[0])
        return True

    print("WiFi Failed")
    return False

def ip():
    return wlan.ifconfig()[0] if wlan.isconnected() else None

def status():
    return wlan.isconnected()

def disconnect():
    wlan.disconnect()
    wlan.active(False)
