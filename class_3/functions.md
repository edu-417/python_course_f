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


## SECCIÓN 3: PARÁMETROS AVANZADOS

 ### TEORÍA
 ------
 Python ofrece un sistema de parámetros muy flexible:

  ```python
   def f(pos1, pos2, /, normal, *, kw_only, **kwargs)
       │                │          │
       │                │          └─ solo keyword después de *
       │                └─ posicional o keyword
       └─ solo posicional antes de /
  ```

 Los más usados en la práctica:

   - Valores por defecto:  def f(x, modo="rápido") <br>
     Permiten llamadas simples para el caso común y detalladas cuando
     se necesita.
     > HINT: nunca uses mutables ([], {}) como default.

   - `*args`: captura N argumentos posicionales extra como TUPLA <br>
     Útil cuando no sabes cuántos valores recibirás.

   - `**kwargs`: captura N argumentos por nombre extra como DICCIONARIO <br>
     Útil para opciones de configuración o forwarding de parámetros.

   - Orden obligatorio en la firma: <br>
     > (normales, *args, **kwargs)


## SECCIÓN 4: FUNCIONES LAMBDA


### TEORÍA
 ------
 Las funciones lambda vienen del cálculo lambda (λ-calculus), rama de
 la lógica matemática que
 es la base teórica de la programación funcional.

 SINTAXIS
 --------
  ```
   lambda <parámetros> : <expresión>
   │                     │
   │                     └─ expresión; se evalúa y retorna
   │                        automáticamente (no necesita `return`)
   └─ 0, 1 o más parámetros separados por coma
   ```

 Son EXACTAMENTE equivalentes a un `def`, pero con restricciones:

  ```python

  def cuadrado(x):
      return x ** 2

   EQUIVALENTE A:

   lambda x: x ** 2
  ```

 EXPRESIONES PERMITIDAS dentro de una lambda:
  ```
   ✓ Operaciones aritméticas:   lambda x: x * 2 + 1
   ✓ Operaciones de string:     lambda s: s.strip().lower()
   ✓ Ternario (if inline):      lambda x: "par" if x % 2 == 0 else "impar"
   ✓ Llamadas a funciones:      lambda lst: sorted(lst, reverse=True)
   ✓ Acceso a colecciones:      lambda d: d["precio"] * d["cantidad"]
   ✓ Comprensiones:             lambda lst: [x for x in lst if x > 0]
   ✓ Tuplas como resultado:     lambda x: (x, x**2, x**3)
  ```

 IDENTIDAD Y NOMBRE
 ------------------
 Cuando Python ejecuta `lambda x: x * 2`, crea un objeto función real
 en memoria, igual que con `def`. La diferencia es que ese objeto no
 queda ligado automáticamente a un nombre en el namespace.

 ```python

   f = lambda x: x * 2
   print(f.__name__)       #'<lambda>'  ← sin nombre propio

   def double(x): return x * 2
   print(double.__name__)  #'double'    ← nombre registrado

  ```

 > debugging: si una lambda lanza una excepción,
 el traceback solo dirá `"<lambda>"`, dificultando encontrar el origen.
 Es uno de los motivos por los que PEP 8 desaconseja asignarlas a variables.
