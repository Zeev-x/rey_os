# lcd.py
from machine import Pin, I2C
import ssd1306

class LCD:
    def __init__(self, oled):
        self.oled = oled

    def clear(self):
        """Bersihkan layar"""
        self.oled.fill(0)
        self.oled.show()

    def text(self, teks, x, y):
        """Tampilkan teks biasa"""
        self.oled.text(teks, x, y)
        self.oled.show()

    def centered_text(self, teks, y=None):
        """Tampilkan teks di tengah horizontal, opsional posisi Y"""
        #self.oled.fill(0)
        text_width = len(teks) * 8
        text_height = 8
        x = (self.oled.width - text_width) // 2
        if y is None:
            y = (self.oled.height - text_height) // 2
        self.oled.text(teks, x, y)
        self.oled.show()

    def draw_text_big(self, teks, y=None, scale=2):
        """
        Menampilkan teks besar dengan scaling piksel.
        """
        text_width = len(teks) * 8 * scale
        text_height = 8 * scale
        x = (self.oled.width - text_width) // 2
        if y is None:
            y = (self.oled.height - text_height) // 2

        # Render teks ke buffer sementara
        tmp = ssd1306.SSD1306_I2C(self.oled.width, self.oled.height, self.oled.i2c)
        tmp.fill(0)
        tmp.text(teks, 0, 0)

        # Perbesar piksel dari buffer tmp ke layar utama
        #self.oled.fill(0)
        for row in range(8):  # tinggi font default
            for col in range(len(teks) * 8):  # lebar teks default
                if tmp.pixel(col, row):  # cek piksel aktif
                    self.oled.fill_rect(
                        x + col*scale,
                        y + row*scale,
                        scale, scale, 1
                    )
        self.oled.show()

    def box(self, x, y, w, h):
        """Gambar kotak sederhana"""
        for i in range(w):
            self.oled.pixel(x+i, y, 1)
            self.oled.pixel(x+i, y+h-1, 1)
        for j in range(h):
            self.oled.pixel(x, y+j, 1)
            self.oled.pixel(x+w-1, y+j, 1)
        self.oled.show()

    def line(self, x1, y1, x2, y2):
        """Gambar garis sederhana (algoritma Bresenham)"""
        dx = abs(x2 - x1)
        dy = -abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx + dy
        while True:
            self.oled.pixel(x1, y1, 1)
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x1 += sx
            if e2 <= dx:
                err += dx
                y1 += sy
        self.oled.show()

# ===== INIT OLED GLOBAL =====
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
display = LCD(oled)

# ======== HOW TO USE ========
# import lcd
# lcd.display.text("Halo ESP32", 0, 0)
# lcd.display.centered_text("Halo ESP32")
# lcd.display.draw_text_big("HALO", scale=2)
