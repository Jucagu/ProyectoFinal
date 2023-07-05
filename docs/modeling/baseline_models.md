# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline. los modelos y pruebas e encuantran en "\scripts\preprocessing\Preprocesamiento.ipynb"

## Descripción del modelo

El baseline sera el modelo de regresion lineal multiple, el cual nos servira como referencia para los demas modelos

## Variables de entrada

ingresan las variables previamente seleccionadas, ademas de algunas despues de aplicar one hot encoding, en total serian 10 variables

## Variable objetivo

La variable objetivo del modelo seria la variable price

## Evaluación del modelo

### Métricas de evaluación

Para este modelo se usaran las metricas MAE, MSE, RMSE y R2, estas estan descritas en una funcion dentro del notebook

### Resultados de evaluación

Los resultados del modelo fueron los siguientes MAE:0.1 MSE:0.02 RMSE:0.15 y R2_test 0.47

## Análisis de los resultados

El resultado del modelo fue pobre, sin embargo nos sirve como base para comparar con los modelos posteriores. Una de las ventajas de este es su facil entendimiendo e interpretacion dado que al ser una regresion lineal multiple basta con tener los coeficientes para ver la correlacion de las variables con la prediccion.

## Conclusiones

El rendimiento de este modelo es lo esperado dado su complejidad, sin embargo podria mejorarse si se seleccionan caracteristicas de una forma mas rigurosa (a pesar que se esta usando KFold)

## Referencias

La informacion sobre el modelo y el codigo usado para su evaluacion se encuentra en el notebook respectivo.

## Comparacion con modelo baseline
Para este proyecto se utilizaron dos modelos adicionales, los cuales son Random Forest y XGBoost, despues de ejecutar las mismas pruebas y utilizar tecnicas para fine tuning se decide proseguir con el modelo de xgboost, toda la informacion con respecto a evaluaciones y fine tuning se encuentra en el notebook.
