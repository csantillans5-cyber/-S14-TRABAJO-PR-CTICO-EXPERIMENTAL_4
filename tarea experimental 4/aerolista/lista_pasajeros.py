from pasajero import Pasajero


class Nodo:
    """Un vagón del tren: lleva un pasajero (data) y el enganche al siguiente (next)."""

    def __init__(self, data):
        self.data = data          # el Pasajero que viaja en este vagón
        self.next = None          # al nacer no está enganchado a nadie


class ListaPasajeros:
    """Lista enlazada simple con todas las reservas del vuelo."""

    def __init__(self):
        self.head = None          # la cabeza: el primer nodo (None = avión vacío)
        self.cantidad = 0         # cuántas reservas (nodos) hay

    def ingresar(self, pasajero):
        nuevo = Nodo(pasajero)                # 1. creo el vagón con el pasajero

        if self.head is None:                 # 2a. Lista vacía:
            self.head = nuevo                 #     el nuevo es la cabeza
        else:                                 # 2b. Lista con nodos:
            actual = self.head                #     pongo el dedo en la cabeza
            while actual.next is not None:    #     mientras NO sea el último...
                actual = actual.next          #     ...avanzo un vagón
            actual.next = nuevo               #     el último ahora apunta al nuevo

        self.cantidad = self.cantidad + 1     # 3. hay una reserva más
        return True

    def esta_vacia(self):
        """Retorna True si no hay ninguna reserva; False si hay al menos una.
        Pista: mira self.head."""
        return self.head is None

    def longitud(self):
        """Retorna cuántas reservas hay.
        Pista: no recorras nada, ya tienes self.cantidad."""
        return self.cantidad

    def listar(self):
        """Retorna una list de Python con TODOS los Pasajero, en orden:
        desde head hasta el último. Si está vacía retorna [].
        ⚠ Guarda el pasajero (actual.data), no el nodo.
        👉 Cuando funcione, ¡el avión se pinta con los asientos ocupados!"""
        resultado = []
        actual = self.head
        while actual is not None:
            resultado.append(actual.data)
            actual = actual.next
        return resultado

    def buscar(self, numero):
        """Búsqueda lineal por número de reserva (int).
        Retorna el Pasajero encontrado o None si no existe."""
        actual = self.head
        while actual is not None:
            if actual.data.numero == int(numero):
                return actual.data
            actual = actual.next
        return None

    def buscar_por_asiento(self, asiento):
        """Retorna el Pasajero sentado en ese asiento ("7D") o None si está libre.
        👉 Flask lo usa al hacer clic en un asiento rojo y para no
           vender dos veces el mismo asiento."""
        asiento = str(asiento).strip().upper()
        actual = self.head
        while actual is not None:
            if actual.data.asiento == asiento:
                return actual.data
            actual = actual.next
        return None

    def buscar_por_cedula(self, cedula):
        """Retorna el Pasajero con esa cédula (str) o None.
        👉 Flask lo usa para que una persona no reserve dos asientos."""
        cedula = str(cedula).strip()
        actual = self.head
        while actual is not None:
            if actual.data.cedula == cedula:
                return actual.data
            actual = actual.next
        return None

    def modificar(self, numero, nuevo_nombre, nueva_edad, nuevo_asiento):
        """Cambia nombre, edad y asiento del pasajero con ese número.
        Usa buscar(). El nodo NO cambia de lugar en la lista: solo cambia su carga.
        Retorna True si lo modificó, False si no existe."""
        pasajero = self.buscar(numero)
        if pasajero is None:
            return False
        pasajero.nombre = nuevo_nombre
        pasajero.edad = int(nueva_edad)
        pasajero.asiento = str(nuevo_asiento).strip().upper()
        return True

    def eliminar(self, numero):
        """Cancela la reserva: desengancha el nodo que tiene ese número.
        Piensa en los casos: lista vacía · es la cabeza · está en medio o al
        final · no existe. ¡No olvides restar self.cantidad!
        Retorna el Pasajero eliminado, o None si no existía."""
        numero = int(numero)

        # Caso 1: lista vacía
        if self.head is None:
            return None

        # Caso 2: el que se elimina es la cabeza (head)
        if self.head.data.numero == numero:
            eliminado = self.head.data
            self.head = self.head.next
            self.cantidad -= 1
            return eliminado

        # Caso 3: está en medio o al final
        anterior = self.head
        actual = self.head.next
        while actual is not None:
            if actual.data.numero == numero:
                eliminado = actual.data
                anterior.next = actual.next
                self.cantidad -= 1
                return eliminado
            anterior = actual
            actual = actual.next

        # Caso 4: no existe
        return None

    def filtrar_por_clase(self, clase):
        """Retorna una list con los pasajeros de esa clase ("Ejecutiva" o
        "Económica"), en el mismo orden de la lista.
        Pista: cada pasajero sabe su clase con  pasajero.clase()"""
        resultado = []
        actual = self.head
        while actual is not None:
            if actual.data.clase() == clase:
                resultado.append(actual.data)
            actual = actual.next
        return resultado
