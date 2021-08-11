from machine import Pin

#Configura o LED Build in como saída
p2 = Pin(2, Pin.OUT)

#Coloca o pino em nível baixo
p2.on()
