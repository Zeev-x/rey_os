import ubluetooth

ble = ubluetooth.BLE()
ble.active(True)

def init(name="ESP32-BLE"):
    ble.config(gap_name=name)

def advertise(interval_us=100000):
    name = ble.config('gap_name')
    if isinstance(name, bytes):
        name_bytes = name
    else:
        name_bytes = name.encode('utf-8')

    adv_data = bytes([
        0x02, 0x01, 0x06,
        len(name_bytes) + 1, 0x09
    ]) + name_bytes

    ble.gap_advertise(interval_us, adv_data)
    print("Advertising as:", name)

def stop():
    ble.gap_advertise(None)
    print("Advertising stopped")

def status():
    return ble.active()
