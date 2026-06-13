# Clase Mascota

class Mascota:

    # Constructor
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    # Método para mostrar la información
    def mostrar_informacion(self):
        print("\n================================")
        print("   INFORMACIÓN DE LA MASCOTA")
        print("================================")
        print("Nombre  :", self.nombre)
        print("Especie :", self.especie)
        print("Edad    :", self.edad, "años")
        print("================================")

    # Método para emitir un sonido
    def hacer_sonido(self):
        if self.especie.lower() == "perro":
            print(self.nombre, "dice: ¡Guau Guau!")
        elif self.especie.lower() == "gato":
            print(self.nombre, "dice: ¡Miau Miau!")
        else:
            print(self.nombre, "emite un sonido.")
            