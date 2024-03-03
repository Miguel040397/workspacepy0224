#Lista de Ejercicios nro3

#1.Una tienda de autopartes necesita un programa para catalogar sus productos,crear la clase catalogo
# y producto, realizar un objeto dentro de un catalgo de productos el cual debe tener un metodo para agregar
# productos el cual debe tener un metodo para agregar productos y otra para mostrar toda la lista de productos.

""" class catalogo:
    producto:None
    modelo:None
    color:None
    
    def __init__(self,producto,modelo):
        self.producto=producto
        self.modelo=modelo
        self.color=[]
        print("se registro producto",self.producto)
    
    def agregarproducto(self,producto):
        self.producto.append(producto)

    def verproducto(self):
        for item in self.producto:
            print(item)

    def __str__(self):
        return f"producto {self.producto} con modelo {self.modelo}" """
    

#2. Realizar un programa que tenga una clase producto el cual solo tiene los atributos de nombre y codigo
# el codigo tiene la siguiente estructura PAIS-LOTE-AÑO ejemplo:PERU-00001-2024 crear un metodo que imprima el objeto de forma 
# literal (__str__) y que permita identificar el pais de origen y nro de lote
    

""" class Producto:

    def __init__(self, pais, lote, año):

        self.pais = pais
        self.lote = lote
        self.año = año

    def describe_restaurant(self):
        print(f'codigo es: {self.pais} - {self.lote} - {self.año}')
        pass
 """
#3. Del siguiente texto :

my_string ="Lorem Ipsum is simply dummy text of the printing and typesetting industry"
# realizar al menos 4 funciones de string 

print(my_string)
len(my_string)
print(my_string[0]) 
print(my_string[-1]) 



#4. crear un archivo nuevo y realizar una funcion que permita dividir 2 numeros, importar esta funcion
# ponerlo en un bucle while True , y al ser llamada la importacion ponerlo dentro de un try except 
# ejecutar la funcion hasta que realice correctamente la division luego de eso romper el bucle