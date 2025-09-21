# Max/Min Value Extractor
![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Last Updated](https://img.shields.io/github/last-commit/vegacastilloe/max_min_extractor)
![Language](https://img.shields.io/badge/language-español-darkred)

#
---
- 🌟 --- CAN YOU SOLVE THIS - EXCEL CHALLENGE 803 ---
- 🌟 * Author: Excel (Vijay A. Verma) BI
 
    - List the Name and Year for Max and Min amounts.
 
 🔰 Este script Identifica todos los valores máximos y mínimos, convirtiendo los datos a una tabla de formato largo (`Name`, `Year`, `Value`).
 
 🔗 Link to Excel file:
 👉 https://lnkd.in/dw_Z9FkH

**My code in Python** 🐍 **for this challenge**

 🔗 https://github.com/vegacastilloe/Conditionals/blob/main/conditionals.py


# 🧩 Max/Min Value Extractor – pandas + Python

Este script toma un conjunto de grupos con candidatos numéricos y condiciones lógicas entre ellos, genera todas las combinaciones posibles, filtra las que cumplen las condiciones, y compara la solución con una respuesta esperada.

## 📦 Datos

- **Name**: contiene el nombre de los grupos.
- **Conditions**: contiene el modo o instrucciones de las condiciones que se deben cumplir.
- **Candidates**: contiene los números de candidatos que se le han asignado a cada grupo.
- 
---
## 🧠 Lógica del análisis
1. Carga un archivo Excel y limpia columnas vacías.
2. Detecta dinámicamente el tamaño del archivo.
3. Convierte la tabla a formato largo (`Name`, `Year`, `Value`).
4. Identifica todos los valores máximos y mínimos.
5. Construye una tabla con encabezados `'Max'` y `'Min'`, mostrando solo en la primera fila de cada grupo.
6. Ordena los mínimos alfabéticamente por nombre.
7. Compara los resultados con una tabla esperada (`test`) y marca coincidencias.

---
## 📊 Resultado

Una tabla con:
- Category: 'Max', 'Min' o vacío (NaN)
- Name: nombre de la persona
- Year: año del valor extremo
- Comparación con tabla esperada (Match: True / False)

---
## ✨Output:

| |Category|Name|Year|Category|Name|Year|Match1|Match2|Match3|
|-|-|-|-|-|-|-|-|-|-|
|0|Max|  John|2017|Max|  John|2017|True|True|True|
|1|   | Smith|2020|   | Smith|2020|True|True|True|
|2|Min|  Anna|2016|Min|  Anna|2016|True|True|True|
|3|   |  Lucy|2016|   |  Lucy|2016|True|True|True|
|4|   |  Lucy|2021|   |  Lucy|2021|True|True|True|
|5|   |Robert|2022|   |Robert|2022|True|True|True|
|6|   | Smith|2018|   | Smith|2018|True|True|True|
---
## 🛠️ Requisitos

- Python 3.8+
- pandas
- Archivo Excel

---
## 🚀 Ejecución
```bash
pip install pandas openpyxl
```
```python
max_min_extractor.py
```
