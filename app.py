import time

def alarm():
    print('zaman doldu!')
while True:
    
    saat = (time.strftime("%X"))
    print(saat)
    time.sleep(1)
    
    if saat == "21:27:00":
        alarm()
        break
#yeni satır