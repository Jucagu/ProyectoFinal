# Definición de los datos

## Origen de los datos

Los datos se obtienen de la pagina oficial de Airbnb

## Especificación de los scripts para la carga de datos

El script utilizado para la adquisicion de los datos es "\scripts\data_acquisition\Adquisicion_Datos.ipynb"

## Referencias a rutas o bases de datos origen y destino

Los datos se encuentran en "\scripts\data_acquisition\listings.csv"

### Rutas de origen de datos

- Los datos se adquieren de la siguiente URL 'http://data.insideairbnb.com/spain/comunidad-de-madrid/madrid/2023-03-15/data/listings.csv.gz'
- Estos vienen estructurados en un gz, por lo cual se craga en python y se realiza una limpieza inicial
- Para la limpieza se eliminan algunos valores nulos y se cambian algunos caracteres para poder realizar los analisis
### Base de datos de destino

- Los datos se guardan en un csv en la ruta anteriormente mencionada
- El archivo csv que se trabajara en este proyecto cuenta con 21 columnas, estas se describen en data_dictionary
- Para el uso de los datos se cargan mediante un jupyter notebook usando pandas.
