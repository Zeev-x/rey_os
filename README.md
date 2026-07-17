# rey_os
MicroPython os

## How to use
Ubah boot.py menjadi seperti ini:

```python
import network
import time
import urequests

SSID = "YOUR_SSID"
PASSWORD = "YOUR_PASSWORD"

def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    print("Connecting to:", SSID)
    wlan.connect(SSID, PASSWORD)

    timeout = 10
    while not wlan.isconnected() and timeout > 0:
        time.sleep(1)
        timeout -= 1

    if wlan.isconnected():
        print("WiFi Connected:", wlan.ifconfig())
        return True
    else:
        print("WiFi Failed")
        return False

def worker(url, file_name, retries=3):
    """Download file dengan chunking + retry"""
    for attempt in range(retries):
        res = None
        try:
            print(f"Downloading {file_name} (attempt {attempt+1})...")
            res = urequests.get(url)
            with open(file_name, "w") as f:
                while True:
                    chunk = res.raw.read(512)  # baca 512 byte
                    if not chunk:
                        break
                    f.write(chunk.decode())
            print(f"File berhasil disimpan ke {file_name}")
            return True
        except Exception as e:
            print("Error:", e)
            time.sleep(2)  # tunggu sebelum retry
        finally:
            if res:
                res.close()
    print(f"Gagal download {file_name} setelah {retries} percobaan.")
    return False

def main():
    files = [
        ("https://zeev-x.github.io/rey_os/ap.py", "/ap.py"),
        ("https://zeev-x.github.io/rey_os/ble.py", "/ble.py"),
        ("https://zeev-x.github.io/rey_os/lcd.py", "/lcd.py"),
        ("https://zeev-x.github.io/rey_os/sdcard.py", "/sdcard.py"),
        ("https://zeev-x.github.io/rey_os/ssd1306.py", "/ssd1306.py"),
        ("https://zeev-x.github.io/rey_os/wifi.py", "/wifi.py"),
        ("https://zeev-x.github.io/rey_os/boot.py", "/boot.py"),
    ]

    for url, path in files:
        worker(url, path)

if wifi_connect():
    try:
        main()
    except Exception as e:
        print("Main error:", e)
```

jangan lupa ubah kofigurasi ini ya:

```python
SSID = "YOUR_SSID" # ubah ke nama wifi kamu
PASSWORD = "YOUR_PASSWORD" # ubah ke password wifi kamu
```
