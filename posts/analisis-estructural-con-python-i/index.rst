.. title: Análisis estructural con Python I
.. slug: analisis-estructural-con-python-i
.. date: 2016-10-18 10:19:56 UTC-05:00
.. tags: numpy, structural analysis, fea, mathjax, draft
.. category: 
.. link: 
.. description: 
.. type: text

El análisis estructural es uno de los aspectos elementales para aquellos 
que nos dedicamos al diseño mecánico o cuestiones similares. En los cursos 
universitarios de resistencia de materiales se enseñan algunos métodos 
analíticos que permiten obtener soluciones rápidas para componentes mecánicos 
simples. No obstante, cuando las geometrías se complican se hace necesario 
utilizar el enfoque numérico e implementar una metodología de solución utilizando 
el método de los elementos finitos, el cual proporciona una solución aproximada 
que será adecuada en medida de ciertos criterios, tales como el tamaño y tipo de 
elementos, la física del problema, entre otros.

El propósito del presente minicurso es introducir al lector en el uso de las 
herramientas numéricas que proporciona Python para la solución de problemas de 
análisis estructural utilizando el MEF.

Como pequeño recordatorio, sabemos que el método de los elementos finitos consiste 
en la discretización de un continuo en pequeños elementos, con la finalidad de 
establecer un sistema de ecuaciones que describa de manera aproximada el comportamiento 
individual y global del sistema, pasando por la inclusión de las condiciones de frontera y todas 
las consideraciones físicas que deriven en la simplificación del problema. 

En análisis numérico estructural el método de los desplazamientos o de la rigidez, asume 
que los desplazamientos nodales son las variables desconocidas y comúnmente se debe resolver 
una ecuación algebraica del tipo:

$$ F = K U $$

Donde F es el vector de fuerzas nodales, K la matriz global de rigidez y U el vector 
de desplazamientos nodales.

Dado que normalmente los desplazamientos son las incógnitas, se tiene que:

$$ U = K^{-1} F $$


Un caso muy simple: elementos resorte
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vamos a comenzar con un ejemplo muy simple del sistema de resortes que se muestra en la 
figura siguiente. 

.. image:: /structural-analysis/spring_01.png


El elemento resorte es el elemento más sencillo, sólo tiene un grado de libertad (por cada nodo): en 
dirección axial. La matriz de rigidez para un elemento viene dada por:

.. math::

    k^{(e)} = 
    \begin{bmatrix}
    k_e & - k_e \\
    - k_e & k_e \\
    \end{bmatrix}


.. code:: python

    # -*- coding: utf8 -*-
    import numpy as np
    import numpy.linalg as la

    # Datos iniciales
    k1 = 1000.0
    k2 = 2000.0
    k3 = 3000.0
    P = 5000.0

    # Matrices por elemento
    K1 = np.array([[k1,-k1],[-k1,k1]])
    K2 = np.array([[k2,-k2],[-k2,k2]])
    K3 = np.array([[k3,-k3],[-k3,k3]])

    # Matriz global 
    K = np.array([[  K1[0,0],        0,           K1[0,1],                0],
                   [      0 ,  K3[0,0],                 0,          K3[0,1]],
                   [ K1[1,0],        0,   K1[1,1]+K2[0,0],          K2[0,1]],
                   [       0,  K3[1,0],           K2[1,0],  K2[1,1]+K3[1,1]]])
                   
    F = np.array([0, 0, 0, P])

    # Condiciones de frontera
    # Nodos 1 y 2 conocidos -> UX = 0
    KS = K[2:,2:]
    FS = F[2:]

    # Resolviendo
    USOL = la.solve(KS, FS)

    # Vector de desplazamientos
    USOL = np.concatenate(([0,0],USOL))

    # Obteniendo las fuerzas nodales
    NF = np.dot(K,USOL)

    # Presentando los resultados
    for nodo in range(4):
        print("%g  UX = %-8.4f    FX = %-8.4f"%(nodo+1, USOL[nodo], NF[nodo]))

