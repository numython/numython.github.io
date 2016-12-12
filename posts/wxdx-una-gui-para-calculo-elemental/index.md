<!-- 
.. title: wxdx, una GUI para cálculo elemental
.. slug: wxdx-una-gui-para-calculo-elemental
.. date: 2016-12-12 16:25:00 UTC-06:00
.. tags: wxPython, MiniApps
.. category: 
.. link: 
.. description: 
.. type: text
-->

En este blog ya hemos tratado algunas veces cómo desarrollar interfaces gráficas utilizando wxPython 
(véase [aquí](https://numython.github.io/categories/wxpython/)). En este post vamos a presentar el 
desarrollo de una mini-aplicación que calcula límites, derivadas e integrales utilizando SymPy como 
motor de cálculo simbólico.

En la siguiente imagen se muestra la interfaz gráfica resultante:

![](/img/wxdx.PNG) 

Ahora vamos a describir un poco el diseño y funcionamiento de la aplicación. Como puede notarse 
la aplicación está basada en la clase [`wxNotebook`](http://docs.wxwidgets.org/3.1/classwx_notebook.html), 
teniéndose cuatro páginas: Límites, Derivadas, Integrales indefinidas y Ayuda. Cada página del 
Notebook contiene un instancia heredada de `wxPanel`, misma que contiene todos los controles 
necesarios en cada uno de los casos.

El proceso de cálculo es básicamente como sigue: se lee una función $f(x)$ introducida en los 
`wxTextCtrl` correspondientes y se hace un preprocesamiento mínimo, enseguida se transforma 
el string leído en una expresión de SymPy, para luego llevar a cabo la operación 
requerida. El resultado de la operación dado por SymPy se muestra en un canvas de Matplotlib, 
en el cual se renderiza la expresión LaTeX del resultado obtenido.

El código de la aplicación completa se adjunta a continuación.

.. gist:: a6962f0bf47aded8280642ff85b42da8
