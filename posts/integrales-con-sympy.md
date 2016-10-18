.. title: Integrales con SymPy
.. slug: integrales-con-sympy
.. date: 2016-10-18 11:30:03 UTC-05:00
.. tags: mathjax, sympy, cálculo,
.. category: 
.. link: 
.. description: 
.. type: text

Las integrales son uno de los conceptos básicos en la formación matemática de un ingeniero, es en términos básicos la 
operación inversa de la derivación. Pero, además del concepto puramente matemático, las integrales tienen múltiples 
interpretaciones geométricas y físicas.

En un curso ordinario de cálculo se nos enseñan métodos para resolver de forma analítica funciones que sean integrables. 
Por ejemplo todos sabemos que la integral de una función constante será:

$$ \int a\,dx = ax + C $$

Y lo sabemos porque nos hemos aprendido reglas básicas de integración y por supuesto a indentificar el tipo 
de función. Actualmente existen paquetes de álgebra simbólica que son capaces de realizar esta tarea: identificar 
el caso que se tiene y aplicar métodos computacionales, hasta cierto grado complejos, para determinar la solución.

Y claro, SymPy es uno de esos sistemas de álgebra computacional (CAS), en el que solo necesitamos escribir 
nuestra función a integrar, utilizar por ahí alguna rutina y obtener un resultado rápidamente. Pero claro, 
para ello debemos aprender mínimamente la sintaxis y eso es justo lo que veremos enseguida.

### Integrales simples

Vamos a ver cómo resolver integrales simples indefinidas, si, de esas que vemos en un primer curso. Para resolverlas 
tendremos que utilizar la función `ìntegrate`. Por ejemplo se tiene la siguiente función \\(f(x)=x^2-3x+2 \\).

Como primer paso debemos importar lo que necesitaremos del paquete SymPy:

```python
>>> from sympy.abc import x
>>> from sympy import integrate
```

Del módulo `abc` importamos la variable simbólica `x` e `ìntegrate` para resolver nuestra integral. Ahora, podemos 
*guardar* la función a integrar en una variable o bien pasarla directamente como argumento:

    >>> f=x**2-3*x+2
    >>> integrate(f)
    x**3/3 - 3*x**2/2 + 2*x

En este caso no hemos tenido incovenientes, porque en la expresión a integrar sólo existe una variable simbólica, pero 
si la expresión tuviese más de una, habría que especificar de manera explícita la variable respecto a la cual se integra:

    >>> from sympy.abc import x,a,b,c
    >>> from sympy import integrate
    >>> f=a*x**2+b*x+c
    >>> integrate(f)

    Traceback (most recent call last):
      File "<pyshell#14>", line 1, in <module>
        integrate(f)
      File "C:\Python27\lib\site-packages\sympy\utilities\decorator.py", line 35, in threaded_func
        return func(expr, *args, **kwargs)
      File "C:\Python27\lib\site-packages\sympy\integrals\integrals.py", line 1228, in integrate
        integral = Integral(*args, **kwargs)
      File "C:\Python27\lib\site-packages\sympy\integrals\integrals.py", line 79, in __new__
        obj = AddWithLimits.__new__(cls, function, *symbols, **assumptions)
      File "C:\Python27\lib\site-packages\sympy\concrete\expr_with_limits.py", line 362, in __new__
        % function)
    ValueError:  specify dummy variables for a*x**2 + b*x + c. If the integrand contains more than 
    one free symbol, an integration variable should be supplied explicitly e.g., integrate(f(x, y), x)

Pues eso, si intentamos integrar la función \\(f(x)=ax^2+bx+c\\) sin especificar la variable de integración, Python nos mandará un 
error que es bastante sugerente al respecto. Así, lo correcto sería:

    >>> integrate(f,x)
    a*x**3/3 + b*x**2/2 + c*x

### Integrales definidas


    >>> from sympy.abc import x
    >>> from sympy import cos,pi,integrate
    >>> integrate(cos(x),(x,0,pi/2.0))
    1

