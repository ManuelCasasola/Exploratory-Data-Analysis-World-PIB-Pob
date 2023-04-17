import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu

# Accedemos a los archivos correspondientes
url_pob='pob_mundial.xls'
df_pob=pd.read_excel(url_pob)

url_pib='pib_mundial.xls'
df_pib=pd.read_excel(url_pib)

# Información
print(df_pob.head(10))
print('Cantidad de Filas y columnas:',df_pob.shape)
print('Nombre columnas:',df_pob.columns)
print(df_pib.head(10))
print('Cantidad de Filas y columnas:',df_pib.shape)
print('Nombre columnas:',df_pib.columns)

# Realizamos un merge de los dos Dataframes seleccionando la columna 'Country Name'
df_merged=pd.merge(df_pob,df_pib,on='Country Name')

# Calculamos la correlación entre la población y el PIB de cada país
correlacion=df_merged[['2000_x','2021_x','2000_y','2021_y']].corr()
print(correlacion)

# Vamos a representarlo en un Scatter Plot para cada año
plt.scatter(df_merged['2000_x'],df_merged['2000_y'])
plt.xlabel('Población (2000)')
plt.ylabel('PIB(2000)')
plt.show()

plt.scatter(df_merged['2021_x'],df_merged['2021_y'])
plt.xlabel('Población (2021)')
plt.ylabel('PIB(2021)')
plt.show()

# Resumen estadístico comparativo

# Media población/PIB en 2020
media_pob_2000=df_merged['2000_x'].mean()
media_pib_2000=df_merged['2000_y'].mean()
print('Media poblacional 2000: ',media_pob_2000)
print('Media PIB 2000: ',media_pib_2000)

# Media población/PIB en 2021
media_pob_2021=df_merged['2021_x'].mean()
media_pib_2021=df_merged['2021_y'].mean()
print('Media poblacional 2021: ',media_pob_2021)
print('Media PIB 2021: ',media_pib_2021)

# Mediana población/PIB en 2020
mediana_pob_2000=df_merged['2000_x'].median()
mediana_pib_2000=df_merged['2000_y'].median()
print('Mediana poblacional 2000: ',mediana_pob_2000)
print('Mediana PIB 2000: ',mediana_pib_2000)

# Mediana población/PIB en 2021
mediana_pob_2021=df_merged['2021_x'].median()
mediana_pib_2021=df_merged['2021_y'].median()
print('Mediana poblacional 2020: ',mediana_pob_2021)
print('Mediana PIB 2021: ',mediana_pib_2021)

# Cambios en la población y PIB con el paso del tiempo
# Población
df_merged.plot(x='Country Name',y=['2000_x','2021_x'])
plt.title('Población Comparativa 2000-2021')
plt.xlabel('Países')
plt.ylabel('Población')
plt.show()

# PIB
df_merged.plot(x='Country Name',y=['2000_y','2021_y'])
plt.title('PIB Comparativo 2000-2021')
plt.xlabel('Países')
plt.ylabel('PIB')
plt.show()

# Gráfica BoxPlot
df_boxplot=df_pob[['Country Name','2000','2021']].melt(id_vars=['Country Name'],var_name='Año',value_name='Población')
sns.boxplot(x='Año',y='Población',data=df_boxplot)
plt.show()

# Gráfica ViolinPlot
df_violinplot=df_pob[['Country Name','2000','2021']].melt(id_vars=['Country Name'],var_name='Año',value_name='Población')
sns.violinplot(x='Año',y='Población',data=df_violinplot)
plt.show()

#Gráfica JointPlot
sns.jointplot(x='2000_x',y='2000_y',data=df_merged)
plt.show()

# Prueba t de Student
# Extraemos las columnas que queremos comparar
pob_2000=df_pob['2000']
pob_2021=df_pob['2021']
# Realizamos la prueba t de Student
t_stat,p_value=ttest_ind(pob_2000,pob_2021)
print('Estadística-t',t_stat)
print('Valor-p',p_value)

#Prueba Mann-Whitney
u_stat,valor_p=mannwhitneyu(pob_2000,pob_2021)
print('Estadística-U',u_stat)
print('Valor-p',valor_p)
