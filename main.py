import menu
import interfaceled
import RPi.GPIO as GPIO

interface=menu.interfasMenu()
interfaceleds=interfaceled.interfaceled()

option=0



while option!=3:
    option=interface.MostrarMenu()
    
    if option==1:
        interfaceleds.opciones()