# ap.py
import network

def start_ap(ssid="ESP32-AP", password="12345678"):
    # Buat interface WiFi Access Point
    ap = network.WLAN(network.AP_IF)
    ap.active(True)

    # Konfigurasi SSID dan password
    ap.config(essid=ssid, password=password)

    print("Access Point aktif")
    print("SSID:", ssid)
    print("Password:", password)
    print("IP:", ap.ifconfig()[0])

    return ap

def stop_ap(ap):
    ap.active(False)
    print("Access Point stopped")

# ===== Cara pakai =====
# import ap
# ap_instance = ap.start_ap("MyESP32", "mypassword")
# lalu connect HP ke SSID "MyESP32"
