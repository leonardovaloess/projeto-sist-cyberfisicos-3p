'''
Teste do sensor DHT22 realizados no Wokwi
https://wokwi.com/projects/429084734293321729
'''


import dht
from machine import Pin
import time

sensor = dht.DHT22(Pin(21))

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperatura: ", temp, "°C")
        print("Umidade: ", hum, "%")
    except Exception as e:
        print("Erro ao ler sensor:", e)

    time.sleep(2)