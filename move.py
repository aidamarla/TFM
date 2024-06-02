""" # Importamos los paquetes necesarios
import RPi.GPIO as GPIO #Para controlar pines de la tarj$
import spidev #Para implementar comunicación SPI
import time

GPIO.setmode(GPIO.BCM) #Definimos el modo para referirnos a los pines de la Raspberry Pi

spi = spidev.SpiDev() #Creamos el objeto spi
spi.open(1,2) #Abrimos el puerto SPI - Módulo 0, Dispositivo 0
spi.max_speed_hz = 5000 #Establecemos la velocidad máxima -->muy importante<--
try:
    while True:
        comando = input("Ingresar comando (Forward/Backward/Left/Right/Stop): ") #Solicitamos ingresar comando
        comando = comando + "\n" #Agregamos salto de línea al final del comando ingresado
        comando = comando.encode() #Convertimos el comando a un arreglo de bytes
        spi.xfer(comando) #Mandamos el comando
        time.sleep(0.25) #Esperamos 0.25

except KeyboardInterrupt:
    # Ctrl+C
    print ("Interrupción por teclado")
finally:
    spi.close()
    GPIO.cleanup()
    print ("GPIO.cleanup() y spi.close() ejecutados ") """

#  Raspberry Pi Master for Arduino Slave
#  i2c_master_pi.py
#  Connects to Arduino via I2C
  
#  DroneBot Workshop 2019
#  https://dronebotworkshop.com

#  Raspberry Pi Master for Arduino Slave
#  i2c_master_pi.py
#  Connects to Arduino via I2C
  
#  DroneBot Workshop 2019
#  https://dronebotworkshop.com

from smbus import SMBus

addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1

numb = 1

print ("Menu:")
print ("Enter w for Advance")
print ("Enter s for Backward")
print ("Enter a for Left")
print ("Enter d for Right")
print ("Enter e for Stop")

while numb == 1:

	direction = input(">>>>   ")

	if direction == "w":
		bus.write_byte(addr, 0x1) # advance
	elif direction == "s":
		bus.write_byte(addr, 0x2) # backwards
	elif direction == "d":
		bus.write_byte(addr, 0x3) # left
	elif direction == "a":
		bus.write_byte(addr, 0x4) # right
	elif direction == "e":
		bus.write_byte(addr, 0x0) # stop
	else:
		numb = 0