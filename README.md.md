# Parcial — Detector de Transmisiones Sospechosas

Nombre:  Esteban Tamayo
Código:  Sistema Antifraude
Grupo:  4-E

## 1. ¿Qué debe hacer el programa?

Escriba en máximo 3 o 4 líneas cuál es el objetivo del programa.

Respuesta:

El prorgama debera leer diferente trasacciones y analizar el nivel de riesgo de cada una
a su vez debera darle un puntaje a cada transaccion segun las condiciones establecidad
todo esto usando jsons y clases

## 2. Clase `Transmision`

La clase tendrá los siguientes atributos:

- `id`: Es el identificador unico de cada transaccion
- `origen`: El pais donde se origino la transaccion
- `titular`: El nombre de la persona que haces la transaccion
- `hora`: la hora segun el pais que realiza la transaccion
- `puntaje`: el valor entero del riesgo de la transaccion y sus condiciones
- `clasificacion`: la clasificaion depende del valor del puntaje y representa su nivel de riesgo
- `dispositivo conocido`: es boliano que represnta si el dispositivo es reconocido por la entidad
- `valor`: La cantidad de dinero que se usa en la transaccion

Escriba brevemente qué representa cada uno.

---

## 3. Métodos

### `calcular_riesgo()`

Responsabilidad: Calcula y devuelve el puntaje

### `clasificar()`

Responsabilidad: con el puntaje clasifica la transaccion

### `to_dict()`

Responsabilidad: pasa un objeto a un diccionario 

### `from_dict()`

Responsabilidad: pasa un diccionario dentro de un json a un objeto

---

## 4. Algoritmo de análisis

Complete el siguiente pseudocódigo:

```text
puntaje = 0

SI el mensaje contiene _________Valor mayor o igual a $2.000.000_________
    sumar ___+30___ puntos

SI el mensaje contiene ______Hora entre 0 y 5____________
    sumar __+20____ puntos

SI el mensaje contiene ________País diferente de Colombia__________
    sumar ____+25__ puntos

SI el mensaje contiene ______Dispositivo NO conocido____________
    sumar __+30____ puntos

```

---

## 5. Persistencia

Explique brevemente qué ocurre al iniciar el programa: se lee el json, se saca la lista de diccionarios y se pasan a objetos

```text
JSON
 ↓
__lista de diccionarios_________________
 ↓
___objeto/ from_dict()________________
```

Explique qué ocurre al guardar: Se leen los objetos de la clase y usando el metodo to_Dcit() se pasan a un json

```text
Objetos
 ↓
__to_dict()__________________
 ↓
JSON
```

---

## 6. Menú

Indique qué debe hacer cada opción:

### Opción 1 — Registrar transmisión

1.  pide el nombre,valor,titular,hora,pais,dispositivo_conocido
2.  se le asigna el id
3.  se guarda en la clase

### Opción 2 — Listar transmisiones

1.  muestra las transacciones
2.  muestra el puntaje y clasificacion de cada una

### Opción 3 — Salir

Acción: salir del programa

---

## Nota

Este archivo debe completarse durante los primeros 15 minutos del parcial, antes de comenzar la implementación.