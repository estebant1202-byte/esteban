import json
import os

class Transaccion:
    def __init__(self, id, titular, valor, hora, pais, dispositivo_conocido):
        if not titular:
            raise ValueError("El titular no puede estar vacío")
        if valor <= 0:
            raise ValueError("El valor debe ser mayor que cero")
        if not (0 <= hora <= 23):
            raise ValueError("La hora debe estar entre 0 y 23")
        if not pais:
            raise ValueError("El país no puede estar vacío")
        if not isinstance(dispositivo_conocido, bool):
            raise ValueError("dispositivo_conocido debe ser booleano")

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


def main():
    transacciones = cargar_transacciones()

    t1 = Transaccion(1, "Laura Gómez", 3500000, 2, "Colombia", False)
    t2 = Transaccion(2, "Carlos Pérez", 500000, 14, "Colombia", True)
    t3 = Transaccion(3, "Ana Torres", 2500000, 10, "Perú", True)

    for t in [t1, t2, t3]:
        t.calcular_riesgo()
        t.clasificar()
        transacciones.append(t)
        print(f"ID: {t.id} | Titular: {t.titular} | Puntaje: {t.puntaje_riesgo} | Clasificación: {t.clasificacion}")

    guardar_transacciones(transacciones)
    
main()
