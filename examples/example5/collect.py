import esp32
import time

counter = 1

with open("out.csv", "w") as f:
    while True:
        print(counter, esp32.hall_sensor(), file=f, sep=",")        
        print(counter, esp32.hall_sensor())
        counter += 1
        time.sleep(0.2)
