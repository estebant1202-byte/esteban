import json
import os

class Transaccion:
    def __init__(self, id, titular, valor, hora, pais, dispositivo_conocido):
        if not titular:
            raise ValueError("El titular no puede estar vacío")
        if valor <= 0:
            raise ValueError("El valor debe ser mayor que cero")
        if not (0 < hora <= 23):
            raise ValueError("La hora debe estar entre 0 y 23")
        if not pais:
            raise ValueError("El país no puede estar vacío")
        if not isinstance(dispositivo_conocido, bool):
            raise ValueError("dispositivo_conocido debe ser booleano")
        if not isinstance(id, int):
            raise ValueError("El ID debe ser un número entero")
        if not isinstance(hora, int):
            raise ValueError("La hora debe ser un número entero")
        if not isinstance(dispositivo_conocido, bool):
            raise ValueError("dispositivo_conocido debe ser booleano")
        if not isinstance(valor, (int, float)):
            raise ValueError("El valor debe ser numérico")
    
        self.id = id
        self.titular = titular
        self.valor = valor
        self.hora = hora
        self.pais = pais
        self.dispositivo_conocido = dispositivo_conocido
        self.puntaje_riesgo = 0
        self.clasificacion = ""

    def calcular_riesgo(self):
        puntaje = 0
        if self.valor >= 2000000:
            puntaje += 30
        if 0 <= self.hora <= 5:
            puntaje += 20
        if self.pais.strip().lower() != "colombia":
            puntaje += 25
        if not self.dispositivo_conocido:
            puntaje += 30
        self.puntaje_riesgo = puntaje
        return puntaje

    def clasificar(self):
        if self.puntaje_riesgo < 30:
            clasificacion = "NORMAL"
        elif self.puntaje_riesgo < 60:
            clasificacion = "SOSPECHOSA"
        else:
            clasificacion = "ALTO RIESGO"
        self.clasificacion = clasificacion
        return clasificacion

    def to_dict(self):
        return {
            "id": self.id,
            "titular": self.titular,
            "valor": self.valor,
            "hora": self.hora,
            "pais": self.pais,
            "dispositivo_conocido": self.dispositivo_conocido,
            "puntaje_riesgo": self.puntaje_riesgo,
            "clasificacion": self.clasificacion
        }

    @classmethod
    def from_dict(cls, datos):
        transaccion = cls(
            datos["id"],
            datos["titular"],
            datos["valor"],
            datos["hora"],
            datos["pais"],
            datos["dispositivo_conocido"]
        )
        transaccion.puntaje_riesgo = datos["puntaje_riesgo"]
        transaccion.clasificacion = datos["clasificacion"]
        return transaccion


def cargar_transacciones():
    if os.path.exists("transacciones.json"):
        with open("transacciones.json", "r",encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [Transaccion.from_dict(d) for d in datos]
    else:
        return []


def guardar_transacciones(transacciones):
    datos = [t.to_dict() for t in transacciones]
    with open("transacciones.json", "w",encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4,ensure_ascii=False)

def registrar_transaccion(transacciones):
    while True:
        print("="*6, "registrar transaccion", "="*7)

        try:
            if len(transacciones) != 0:
                id_t = len(transacciones)+ 1
            else:
                id_t = 1
            titular = input("Titular: ")
            if titular.strip() == "" or  titular.isdigit():
                print(f"Error titular mal ingresado")
                continue
            valor = float(input("Valor: "))
            if  valor <= 0:
                print(f"Error valor mal ingresada")
                continue
            hora = int(input("Hora (0-23): "))
            if  hora <= 0 or hora > 23:
                print(f"Error hora mal ingresada")
                continue
            pais = input("País: ")
            if pais.strip() == "" or  pais.isdigit():
                print(f"Error pais ml ingresado")
                continue
            dispositivo = input("¿Dispositivo conocido? (s/n): ").lower() 
            if dispositivo == "s":
                dispositivo = True
            elif dispositivo == "n":
                dispositivo = False
            else:
                print("Error ingrese s o n porfavor")
                continue

            t = Transaccion(id_t, titular, valor, hora, pais, dispositivo)
            t.calcular_riesgo()
            t.clasificar()
            transacciones.append(t)
            print(f"Transacción registrada. Puntaje: {t.puntaje_riesgo} | Clasificación: {t.clasificacion}")
            guardar_transacciones(transacciones)
            break
        except ValueError:
            print(f"Error: porfavor ingrese un numero")
    print("="*36)

def ver_transacciones(transacciones):
    print("="*10,"Transacciones","="*11)
    for t in transacciones:
        print(f"ID: {t.id:<5} | Titular: {t.titular:<10} | Puntaje: {t.puntaje_riesgo:<5} | Clasificación: {t.clasificacion:<5}")
    print("="*36)
def main():
    print("cargando datos...")
    transacciones = cargar_transacciones()
    print("exito\n")
    while True:
        
        print("="*15,"menu","="*15)
        print("1. Registrar transacción")
        print("2. Ver transacciones")
        print("3. salir")
        print("="*36)


        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                registrar_transaccion(transacciones)
            case "2":
                ver_transacciones(transacciones)
            case "3":
                print("saliendo...")
                break
            case _:
                print("Opción inválida.") 
main()
