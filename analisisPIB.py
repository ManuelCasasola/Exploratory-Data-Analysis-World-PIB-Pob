import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Accedemos al archivo.
url='pib_mundial.xls'
df_pib=pd.read_excel(url)
df_pib.info() # Esta función nos muestra toda la información del archivo.

# Información
print(df_pib.head(10))
print('Cantidad de Filas y columnas:',df_pib.shape)
print('Nombre columnas:',df_pib.columns)

# Ahora, plotearemos una gráfica de barras con el PIB de 2020 y 2021 de todos los países
ax=df_pib.drop(['Country Name'], axis=1)[['2020','2021']].plot(kind='bar')
ax.set_title('PIB 2020-2021')
ax.set_xlabel('Países')
ax.set_ylabel('PIB')
plt.show()

# En este caso, al haber demasiados países la gráfica apenas se puede visualizar
# Probremos a cambiar el tipo de gráfico que nos muestra a un histograma
ax=df_pib.drop(['Country Name'], axis=1)[['2020','2021']].plot(kind='hist')
ax.set_title('PIB 2020-2021')
ax.set_xlabel('Países')
ax.set_ylabel('PIB')
plt.show()

# No parece que mejore el resultado, por lo que filtraremos el dataframe
# por los países que empiecen por la letra F
df_f=df_pib[df_pib['Country Name'].str.startswith('F')]

# Podemos también representar gráficamente de otra manera, como con puntos de dispersión
ax=df_f.plot.scatter(x='2020',y='2021')
ax.set_title('PIB 2020-2021')
ax.set_xlabel('Países')
ax.set_ylabel('PIB')
plt.show()

# Además, podemos añadir funciones de resumen estadístico como la media o la mediana.
media_pib=df_f[['2020','2021']].mean()
mediana_pib=df_f[['2020','2021']].median()
print('Media del PIB en 2020 y 2021:',media_pib)
print('Mediana del PIB en 2020 y 2021:',mediana_pib)

# Editamos las gráficas.
ax=df_f.set_index('Country Name')[['2020','2021']].plot(kind='bar',rot=0,figsize=(30,10),width=0.2, color=['red', 'blue'],logy=True)
ax.set_title("PIB de los países entre los años 2020-2021")
ax.set_xlabel('Países')
ax.set_ylabel('PIB')
ax.grid(axis='y')
plt.show()