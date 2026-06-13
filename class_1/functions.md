# MÓDULO 4 — FUNCIONES:

Una función es un bloque de código reutilizable que realiza una tarea
específica. Son la base del principio DRY (Don't Repeat Yourself): en vez
de copiar y pegar lógica, la encapsulas una vez y la llamas cuantas veces
necesites.

Ventajas:
  - Reutilización: escribe una vez, usa muchas veces
  - Legibilidad: un buen nombre de función documenta qué hace el código
  - Mantenimiento: corriges un bug en un solo lugar
  - Testing: puedes probar cada función de forma aislada
 
 
## SECCIÓN 1: def, return, parámetros y argumentos

### TEORÍA
 ------
 - `def` declara la función. El bloque indentado es su cuerpo.
 - Los PARÁMETROS son las variables que define la función en su firma.
 - Los ARGUMENTOS son los valores concretos que le pasas al llamarla.
 - `return` termina la función y entrega un valor al llamador.
   Sin `return` explícito, Python devuelve `None` automáticamente.
 - Una función puede retornar MÚLTIPLES valores: Python los empaqueta
   como tupla transparentemente.

 Anatomía:
 ```python
   def nombre_funcion(param1, param2):   ← parámetros
        cuerpo
       return valor                      ← resultado

   resultado = nombre_funcion(arg1, arg2)  ← argumentos
```

## SECCIÓN 2: SCOPE — Variables locales vs globales

 TEORÍA
 ------
 El SCOPE (alcance) define desde dónde es visible una variable.
 Python sigue la regla LEGB para buscar un nombre:

> -   L — Local:     dentro de la función actual
> -   E — Enclosing: funciones externas que la contienen (closures)
> -   G — Global:    nivel del módulo/script
> -   B — Built-in:  nombres reservados de Python (len, print, range...)

 Python busca en ese orden y se detiene en el primero que encuentre.

 Reglas clave:
   - Puedes LEER variables globales desde una función.
   - Para MODIFICAR una global desde una función, necesitas `global`.
   - Para modificar una variable de la función contenedora, `nonlocal`.
   - Modificar globales es considerado mala práctica; preferir parámetros
     y returns para que las funciones sean predecibles y testeables.