# Reporte del Modelo Final

los modelos y pruebas se encuantran en "\scripts\preprocessing\Preprocesamiento.ipynb"

## Resumen Ejecutivo

Para este proyecto se eligio el modelo de Random Forest, el cual fue el que presento el mejor rendimiento a la hora de realizar las predicciones

## Descripción del Problema

El problema inicial a resolver era la prediccion de precios de alojamiento a partir de caracteristicas especificas, para esto primero se opto por un modelo inicial de regresion lineal, el cual es un modelo sencillo e interpretable, sin embargo al haber tabtas caracteristicas a la hora de asignar el preciso de los alojamientos se opto por probar modelos basados en arboles de decision, por lo cual se opto por los medelos de XGBoost y Random Forest. Estos dos modelos lograron mejores resultados quer el modelo baseline, por lo cual se continuo a una etapa de fine tuning de ambos, donde se utilizaron tecnicas como RandomizedSearchCV para encontrar los mejores parametros. Despues de tener la mejor version de cada modelo se termino escogiendo el modelo de Random Forest dado su rendimiento.

## Descripción del Modelo

Tal como se comento anteriormente el modelo escogido fue uno basado en arboles de desicion como lo es el Random Forest,el cual es un método versátil de aprendizaje automático capaz de realizar tanto tareas de regresión como de clasificación. También lleva a cabo métodos de reducción dimensional, trata valores perdidos, valores atípicos y otros pasos esenciales de exploración de datos. Es un tipo de método de aprendizaje por conjuntos, donde un grupo de modelos débiles se combinan para formar un modelo poderoso.
## Evaluación del Modelo

El modelo Final tuvo un buen rendimiento, el cual se ve reflejado en la siguientes metricas:

Training r2: 0.82
Validation r2: 0.57


## Conclusiones y Recomendaciones

El modelo presenta un mejor rendimiento que el de baseline, sin embargo al estar entrenando el modelo, me percate que estaba sufriendo de overfitting, lo cual no es lo idela dado que queremos que no se sesgue a los datos, por otra parte, el modelo con el cual se estaba comparando tambien tuvo rendimiento parecido, sin embargo a la hora de entrenarlo este si tuvo un overfitting mas notorio. PAra finalizar se recomienda que a la hora de utilizar el modelo se haga el debido preprocesamiento a los datos, como por ejemplo el onehot encoder y la eliminacion de parametros no utilizados a la hora de la prediccion

## Referencias

Las referencias y el codigo con las metricas se encuatran en el notebook.
