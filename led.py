import RPi.GPIO as GPIO

class LED:
    def __init__(self, pin):
        self.pin = pin

        # Configura el pin GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def encender(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def apagar(self):
        GPIO.output(self.pin, GPIO.LOW)

    def parpadear(self, tiempo_encendido, tiempo_apagado, veces):
        for i in range(veces):
            self.encender()
            time.sleep(tiempo_encendido)
            self.apagar()
            time.sleep(tiempo_apagado)

    def __del__(self):
        GPIO.cleanup()
