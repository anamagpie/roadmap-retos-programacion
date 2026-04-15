from enum import Enum 

'''
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 '''
#Para crear un anum hay que crear una clase
class DiasSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def imp_dia(num: int):
    print(DiasSemana(num).name)

imp_dia(1) #Imprime el Lunes
imp_dia(4) #Imprime el Jueves

'''
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
'''

class EstadoPedido(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Pedido:

    estado = EstadoPedido.PENDIENTE # Estado por defecto: Pendiente

    def __init__(self, id) -> None:
        self.id = id
    
    def enviado(self):
        if self.estado == EstadoPedido.PENDIENTE:
            self.estado = EstadoPedido.ENVIADO
            self.mostrar_estado()
        else:
            print("El pedido ha sido cancelado o y ase encuentra fuera de nuestras instalaciones.")

    def entregado(self):
        if self.estado == EstadoPedido.ENVIADO:
            self.estado = EstadoPedido.ENTREGADO
            self.mostrar_estado()
        else:
            print("El pedido aún no ha sido enviado.")

    def cancelado(self):
        if self.estado == EstadoPedido.ENTREGADO:
            self.estado = EstadoPedido.CANCELADO
            self.mostrar_estado()
        else:
            print("No es posible cancelar el pedido. El pedido ya ha sido entregado.")        

    def mostrar_estado(self):
        print(f"El pedido con número {self.id} ha sido {self.estado.name}")

pedido_1 = Pedido(1)

pedido_1.mostrar_estado()
pedido_1.enviado()
pedido_1.entregado()
pedido_1.cancelado()