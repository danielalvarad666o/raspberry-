class interfasMenu:
    
    def MostrarMenu(self):
     try:
        print("[------------Seleccion----------]")
        print("1)led")
        print("2)Mostrar sensores")
        print("3)Salir")
       
        option=int(input("Escoge una option: "))
        return option
     except:
         return "Opcion no valida"