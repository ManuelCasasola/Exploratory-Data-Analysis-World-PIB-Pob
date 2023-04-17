import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Accedemos al archivo.
url='pob_mundial.xls'
df_pob=pd.read_excel(url)
df_pob.info()# Esta función nos muestra toda la información del archivo.

#Información
print(df_pob.head(10))
print('Cantidad de Filas y columnas:',df_pob.shape)
print('Nombre columnas:',df_pob.columns)

# Ahora, plotearemos una gráfica de barras con la población de 2020 y 2021 de todos los países.
ax=df_pob.drop(['Country Name'], axis=1)[['2020','2021']].plot(kind='bar')
ax.set_title('Población 2020-2021')
ax.set_xlabel('Países')
ax.set_ylabel('Población')
plt.show()

# Filtraremos los países, en este caso por la letra M.
df_m=df_pob[df_pob['Country Name'].str.startswith('M')]

# Podemos también representar gráficamente de otra manera, como con puntos de dispersión.
ax=df_m.plot.scatter(x='2020',y='2021')
ax.set_title('Población 2020-2021')
ax.set_xlabel('Países')
ax.set_ylabel('Población')
plt.show()

# Además, podemos añadir funciones de resumen estadístico como la media o la mediana.
media_pob=df_m[['2020','2021']].mean()
mediana_pob=df_m[['2020','2021']].median()
print('Media poblacional en 2020 y 2021:',media_pob)
print('Mediana poblacional en 2020 y 2021:',mediana_pob)

#Editamos la gráfica
ax=df_m.set_index('Country Name')[['2020','2021']].plot(kind='bar',rot=0,figsize=(30,10),width=0.2, color=['red', 'blue'])
ax.set_title('Población mundial entre los años 2020 y 2021')
ax.set_xlabel("Países")
ax.set_ylabel('Población')
ax.grid(axis='y')

plt.show()