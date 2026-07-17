# boot.py
from machine import Pin, SPI
import lcd, os, time, sdcard

lcd.display.clear()

def erase_text(y, h):
    lcd.display.oled.fill_rect(0, y, lcd.display.oled.width, h, 0)
    lcd.display.oled.show()


def clear():
    lcd.display.clear()

def center(teks="Reyette", y=None):
    lcd.display.centered_text(teks, y=y)
    
def big(teks="Reyette", y=None, scale=2):
    lcd.display.draw_text_big(teks, y=y, scale=scale)


text = "ReyOs"
    
center("Reyette Atelier", 4)
center("Reyette os v3", 50)

for i in range(1, len(text)+1):
    erase_text(24, 24)
    big(text[:i], 24, 2)
    time.sleep(0.2)

time.sleep(2)

spi = SPI(2, baudrate=1000000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(23), miso=Pin(19))

try:
    sd = sdcard.SDCard(spi, Pin(5))
    os.mount(sd, "/rey_sd")
    clear()
    center("SD OK")
    time.sleep(1)
    clear()
    print("SD Mounted")
except Exception as e:
    clear()
    center("SD ERR")
    print("SD error:", e)

# --- try run SD boot file ---
try:
    if "reyette.py" in os.listdir("/rey_sd"):
        exec(open("/rey_sd/reyette.py").read())
    else:
        center("No reyette.py")
        print("File reyette.py tidak ditemukan")
except Exception as e:
    print("Exec error:", e)
    clear()
    center("Exec ERR")
