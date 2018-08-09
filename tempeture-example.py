import dht
import machine
import time

print("Starting DHT22.")
d = dht.DHT11(machine.Pin(16))

while True:
    print("Measuring.")
    
    retry = 0
    while retry < 3:
        try:
            d.measure()
            break
        except Exception as e:
            print(e)
            retry = retry + 1
            print(".", end = "")

    print("")

    if retry < 3:
        math = int(d.temperature()) * 9/5 + 32
        
        print("Temperature: %3.1f °C" % d.temperature())
        print("Temperature: %3.1f °f" % math)
        
        print("   Humidity: %3.1f %% RH" % d.humidity())

    time.sleep(5)
