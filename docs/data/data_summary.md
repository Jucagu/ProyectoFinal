# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos. Ver "\eda\EDA.ipynb" para mas informacion

## Resumen general de los datos

El dataset contiene un total aproximadamente 15660 registros de alojamientos de la ciudad de Madrid. Cada registro tiene 21 variables, las cuales se dividen en 1o categoricas y 11 numericas. En la carga de los datos se realizo un primer filtro de datos falktantes, sin embargo todavia hay por lo menos 6196 registros con datos nulos, en el notebook anteriormente mencionado, se pued encontrar algunas distribuciones de la variables del dataset, cabe destacar que la distribucion de los precios es un poco desequilibrada.


## Resumen de calidad de los datos
Los datos no poseen una muy buena calidad, dado que son datos reales de la aplicacion sin ninguna liempieza previa a parte de eliminacion de datos nulos, por lo cual procedemos a mejorar la calidad de nuestros datos de interes, para comenzar se mira las distribucion de la variable price, la cual es fundamental para nuestro objetivo de predecir los precios. Podemos ver como la distribucion de precios contiene demasiado outliers, por lo cual se decide establecer un intervalo entre 5 y 300, lo cual nos ayudara con nuestro objetivo.

## Variable objetivo

Como se menciono anteriormente nuestra variable objetivo es price, la cual se le dio el tratamiento de utilizar los valores donde mas se concentraba acumulada, por otra parte en el notebook se puede consultar su histograma y boxplot

## Variables individuales

Una vez definido el intervalo de precio, se seleccionan las variables finales para realizar el modelo de regresion, estas varables son principalmente las numericas, posteriormente se realiza un mapa de calor para ver cuales influyen mas en el precio


## Ranking de variables

Las tres variables mas importantes despues de realizar el EDA fueron:

-accommodates
-bedrooms
-beds

## Relación entre variables explicativas y variable objetivo

Como se comento anteriormente la correlacion de las variables se puede apreciar en el mapa de calor que se encuentra en el notebook. por otra parte se encuentra logico que estas sean las que mas influyen en el precio dado que influyen directamente en el numero de personas que se podrian hospedar.

