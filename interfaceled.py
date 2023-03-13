import  led

class interfaceled():
    
    def __init__(self) :
        self.led=led.LED(18)
    
    
    def opciones(self):
        print("1)Preder")
        print("2)apagar")
        try:
         opcion=int(input("Escoge una opcion: "))
         if opcion==1:
             self.led.encender()
         elif opcion==2:
             self.led.apagar()
        except:
            print("Opcion no valida")