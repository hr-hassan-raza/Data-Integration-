import pandas as pd
import csv
import petl as etl
df = pd.read_csv (r'G:\Data Integration\owid-covid-data.csv', index_col = "location")
countries = ["Australia", "India" , "Pakistan", "China", "Iran" ,"Belgium","Brazil","Canada","Liberia","United States Virgin Islands",
             "United States", "Tanzania", "Austria","Afghanistan","Turkey" ]
countries_data = []
for i in range (15):
    countries_data.append(df.loc[countries[i]])
mean_new_cases = []
mean_new_deaths = []
std_new_cases = []
std_new_deaths = []
for i in range(15):
    mean_new_cases.append(countries_data[i]['new_cases'].mean())
    std_new_cases.append(countries_data[i]['new_cases'].std())
    mean_new_deaths.append(countries_data[i]['new_deaths'].mean())
    std_new_deaths.append(countries_data[i]['new_deaths'].std())
row_list = [["Country", "Total Cases" , "Total Deaths" , "Mean of new cases", "Mean of new deaths", "Std of new cases", "Std of new deaths"]]
for i in range (15):
    row_list.append(['Name: '+ str(countries[i]), 'Total Cases: '+ str((df.loc[countries[i],'total_cases']).max()),'Total Deaths: '+str((df.loc[countries[i],'total_deaths']).max()),
                 'Mean new cases: '+str( mean_new_cases[i]), 'Mean new deaths: '+ str(mean_new_deaths[i]),'Std new cases: '+str(std_new_cases[i]),'Std new deaths: '+str(std_new_deaths[i])])
with open('new.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=' ')
    writer.writerows(row_list)
table2 = etl.fromcsv('new.csv')
print(table2)