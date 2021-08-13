import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
crimes = pd.read_csv('/Users/username/Downloads/archive/crime.csv', delimiter=',', encoding="ISO-8859-1")

#ASSASSINATOS POR HORA
crime111 = crimes['OFFENSE_CODE'] == 111
crime_assassinato = crimes[crime111]
sns.countplot(data=crime_assassinato, x='HOUR')
plt.xlabel('Hora do dia')
plt.ylabel('Número de Assassinatos')
plt.yticks(np.arange(0, 20, step=1))
plt.title('Quantidade de Assassinatos por Hora do Dia')
plt.show()

#ASSASSINATOS POR DIA DA SEMANA
crime111 = crimes['OFFENSE_CODE'] == 111
crime_assassinato = crimes[crime111]
sns.countplot(data=crime_assassinato, x='DAY_OF_WEEK', order=['Monday','Thursday','Wednesday','Tuesday','Friday','Saturday','Sunday'])
plt.xlabel('Dia da Semana')
plt.ylabel('Número de Assassinatos')
plt.yticks(np.arange(0, 36, step=2))
plt.title('Quantidade de Assassinatos por Dia da Semana')
plt.show()

#LAT,LONG - ASSASSINATOS
crime111 = crimes['OFFENSE_CODE'] == 111
crime_assassinato = crimes[crime111]
crime_assassinato_lat = crime_assassinato.query('Lat>5')
crime_assassinato_long = crime_assassinato_lat.query('Long<-5')
sns.scatterplot(data=crime_assassinato_long, x='Long', y='Lat', hue='DISTRICT')
plt.title('Local dos Assassinatos')
plt.show()

#ASSASSINATOS POR ANO
Anos = ['2015', '2016', '2017', '2018']
NAssi = [27, 47, 54, 33]
plt.plot(Anos, NAssi, label='Assassinatos', marker='o')
plt.title('Série Temporal do crime de Assassinato')
plt.grid()
plt.legend()
plt.show()

#ASSASSINATOS POR ANO PARA CADA DISTRITO
crime111 = crimes['OFFENSE_CODE'] == 111
crime_assassinato = crimes[crime111]

dfassas = crime_assassinato['DISTRICT']=='B2'
dfassasb2 = crime_assassinato[dfassas]
dfassasb2['YEAR'].value_counts()

dfassas2 = crime_assassinato['DISTRICT']=='B3'
dfassasB3 = crime_assassinato[dfassas2]
dfassasB3['YEAR'].value_counts()

dfassas1 = crime_assassinato['DISTRICT']=='C11'
dfassasC11 = crime_assassinato[dfassas1]
dfassasC11['YEAR'].value_counts()

Anos = [2015, 2016, 2017, 2018]
AB2 = [8, 15, 14, 11]
AC11 = [2, 10, 16, 4]
AB3 = [4, 10, 10, 7]
plt.plot(Anos, AB2, marker='o', label='B2')
plt.plot(Anos, AC11, marker='o', label='C11')
plt.plot(Anos, AB3, marker='o', label='B3')
plt.title('Série Temporal do crime de Assassinato para os distritos mais violentos')
plt.xlabel('Anos')
plt.ylabel('Número de Assassinatos')
plt.grid()
plt.legend()
plt.show()

#FURTOS POR HORA
crime619 = crimes['OFFENSE_CODE_GROUP'] == 'Larceny'
crime_furto = crimes[crime619]
sns.countplot(data=crime_furto, x='HOUR')
plt.xlabel('Hora do dia')
plt.ylabel('Número de Furtos')
plt.yticks(np.arange(0, 2100, step=100))
plt.title('Quantidade de Furtos por Hora do Dia')
plt.show()

#FURTOS POR DIA DA SEMANA
crime619 = crimes['OFFENSE_CODE_GROUP'] == 'Larceny'
crime_furto = crimes[crime619]
sns.countplot(data=crime_furto, x= 'DAY_OF_WEEK', order= ['Monday','Thursday','Wednesday','Tuesday','Friday','Saturday','Sunday'])
plt.xlabel('Dia da Semana')
plt.ylabel('Número de Furtos')
plt.yticks(np.arange(0, 4200, step=200))
plt.title('Quantidade de Furtos por Dia da Semana')
plt.show()

#LAT,LONG - FURTO
crimes = pd.read_csv('/Users/giovanebrunonardari/Downloads/archive/crime.csv', delimiter=',', encoding="ISO-8859-1")
crime619 = crimes['OFFENSE_CODE_GROUP'] == 'Larceny'
crime_furto = crimes[crime619]
crime_furto_lat = crime_furto.query('Lat>=0')
crime_furto_long = crime_furto_lat.query('Long<=0')
sns.scatterplot(data=crime_furto_long, x='Long', y='Lat', hue='DISTRICT')
plt.title('Local dos Furtos')
plt.show()

#FURTOS POR ANO
Anos = ['2015', '2016', '2017', '2018']
NFurto = [5006, 7902, 7807, 5220]
plt.plot(Anos, NFurto, label='Furto', marker='o')
plt.title('Série Temporal do crime de Furto')
plt.grid()
plt.legend()
plt.show()

#FURTOS POR ANO PARA CADA DISTRITO
crime619 = crimes['OFFENSE_CODE_GROUP'] == 'Larceny'
crime_furto = crimes[crime619]

dffurto1 = crime_furto['DISTRICT']=='B2'
dffurto2= crime_furto[dffurto1]
dffurto2['YEAR'].value_counts()

dffurtod4 = crime_furto['DISTRICT']=='D4'
dffurtod41= crime_furto[dffurtod4]
dffurtod41['YEAR'].value_counts()

dffurtoA1 = crime_furto['DISTRICT']=='A1'
dffurtoA2= crime_furto[dffurtoA1]
dffurtoA2['YEAR'].value_counts()

Anos = [2015, 2016, 2017, 2018]
FB2 = [608, 890, 891, 482]
FD4 = [1373, 2268, 2157, 1515]
FA1 = [914, 1403, 1402, 985]
plt.plot(Anos, FB2, label='B2', marker='o')
plt.plot(Anos, FD4, label='D4', marker='o')
plt.plot(Anos, FA1, label='A1', marker='o')
plt.title('Série Temporal do crime de Furto para os distritos mais violentos')
plt.xlabel('Anos')
plt.ylabel('Número de Assassinatos')
plt.grid()
plt.legend()
plt.show()

#DROGAS POR HORA
crime1843 = crimes['OFFENSE_CODE_GROUP'] == 'Drug Violation'
crime_drug = crimes[crime1843]
sns.countplot(data=crime_drug, x='HOUR')
plt.title('Apreensão de Drogas por Hora do Dia')
plt.xlabel('Hora do Dia')
plt.ylabel('Quantidade de Apreensões')
plt.yticks(np.arange(0, 2600, step=100))
plt.show()

#DROGAS POR DIA DA SEMANA
crime1843 = crimes['OFFENSE_CODE_GROUP'] == 'Drug Violation'
crime_drug = crimes[crime1843]
sns.countplot(data=crime_drug, x= 'DAY_OF_WEEK', order= ['Monday','Thursday','Wednesday','Tuesday','Friday','Saturday','Sunday'])
plt.title('Apreensão de Drogas por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Quantidade de Apreensões de Drogas')
plt.yticks(np.arange(0, 3150, step=150))
plt.show()

#LAT,LONG - DROGAS
crime1843 = crimes['OFFENSE_CODE_GROUP'] == 'Drug Violation'
crime_drug = crimes[crime1843]
crime_drug_lat = crime_drug.query('Lat>=0')
crime_drug_long = crime_drug_lat.query('Long<=0')
sns.scatterplot(data=crime_drug_long, x='Long', y='Lat', hue='DISTRICT')
plt.title('Local das Apreensões de Drogas')
plt.show()

#DROGAS POR ANO
Anos = ['2015', '2016', '2017', '2018']
NDroga = [3300, 5284, 4759, 3205]
plt.plot(Anos, NDroga, label='Drogas', marker='o')
plt.yticks(np.arange(0, 7000, step=1000))
plt.title('Série Temporal do crime de Drogas')
plt.grid()
plt.legend()
plt.show()

#DROGAS POR ANO PARA CADA DISTRITO
crime1843 = crimes['OFFENSE_CODE_GROUP'] == 'Drug Violation'
crime_drug = crimes[crime1843]

dfdrogab2 = crime_drug['DISTRICT']=='B2'
dfdrogab2 = crime_drug[dfdrogab2]
dfdrogab2['YEAR'].value_counts()

dfdrogac11 = crime_drug['DISTRICT']=='C11'
dfdrogac11 = crime_drug[dfdrogac11]
dfdrogac11['YEAR'].value_counts()

dfdroga1 = crime_drug['DISTRICT']=='A1'
dfdroga1 = crime_drug[dfdroga1]
dfdroga1['YEAR'].value_counts()
Anos = [2015, 2016, 2017, 2018]
NB2 = [452, 685, 628, 504]
NC11 = [527, 784, 593, 305]
NA1 = [423, 719, 577, 357]
plt.plot(Anos, NB2, label='B2', marker='o')
plt.plot(Anos, NC11, label='C11', marker='o')
plt.plot(Anos, NA1, label='A1', marker='o')
plt.title('Série Temporal do crime de Drogas para os distritos mais "violentos"')
plt.xlabel('Anos')
plt.ylabel('Número de Apreensões')
plt.grid()
plt.legend()
plt.show()



