import time
import RPi.GPIO as io
io.setmode(io.BCM)

pir_pin = 18
led_pin = 23

io.setup(pir_pin, io.IN)
io.setup(led_pin, io.OUT)

while True:
  if io.input(pir_pin):
    io.output(led_pin, True)
  else:
    io.output(led_pin, False)
    
