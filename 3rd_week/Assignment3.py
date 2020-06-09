# Assignment 3 from coursera
import pandas as pd
import numpy as np

#################################################################################################
## Question 1:
#Load the energy data from the file Energy Indicators.xls, which is a list of indicators of energy supply and renewable electricity production from the United Nations for the year 2013, and should be put into a DataFrame with the variable name of energy.
#Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:
#['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
#Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule). For all countries which have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.
#Rename the following list of countries (for use in later questions):
#"Republic of Korea": "South Korea",
#"United States of America": "United States",
#"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
#"China, Hong Kong Special Administrative Region": "Hong Kong"
#There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these, e.g.
#'Bolivia (Plurinational State of)' should be 'Bolivia',
#'Switzerland17' should be 'Switzerland'.
#Next, load the GDP data from the file world_bank.csv, which is a csv containing countries' GDP from 1960 to 2015 from World Bank. Call this DataFrame GDP.
#Make sure to skip the header, and rename the following list of countries:
#"Korea, Rep.": "South Korea",
#Iran, Islamic Rep.": "Iran",
#Hong Kong SAR, China": "Hong Kong"
#Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file scimagojr-3.xlsx, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame ScimEn.
#Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).
#The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
#This function should return a DataFrame with 20 columns and 15 entries.

def answer_one():
    ##### Energy Indicators DataFrame
    energy = pd.read_excel('Energy_Indicators.xls', header=15, skipfooter=38)
    columns_to_keep = ['Unnamed: 2', 'Energy Supply', 'Energy Supply per capita', 'Renewable Electricity Production']
    energy = energy[columns_to_keep]
    energy = (energy.rename(columns={'Unnamed: 2':'Country','Energy Supply per capita':'Energy Supply per Capita','Renewable Electricity Production':'% Renewable'})
                    .drop(energy.index[0]) # Eliminando la primera columna
                    .replace('...', np.nan)) # Reemplazamos ... por np.nan
    for country in energy['Country'].unique():
        new_country_name = ''.join([i for i in str(country) if not i.isdigit()])
        energy = energy.replace(country, new_country_name)
    ## Change the name of some countries
    energy = (energy.replace('Republic of Korea', 'South Korea')
                    .replace('United States of America', 'United States')
                    .replace('United Kingdom of Great Britain and Northern Ireland', 'United Kingdom')
                    .replace('China, Hong Kong Special Administrative Region', 'Hong Kong')
                    .replace('Australia1', 'Australia')
                    .replace('Bolivia (Plurinational State of)', 'Bolivia')
                    .replace('Falkland Islands (Malvinas)', 'Falkland Islands')
                    .replace('Iran (Islamic Republic of)', 'Iran')
                    .replace('Micronesia (Federated States of)', 'Micronesia')
                    .replace('Sint Maarten (Dutch part)', 'Sint Maarten')
                    .replace('Venezuela (Bolivarian Republic of)', 'Venezuela'))
    #Converting Energy Supply from petajoules to gigajoules
    energy['Energy Supply'] *=1000000
    energy = energy.set_index('Country')

    ##### world_bank DataFrame
    GDP = pd.read_csv('world_bank.csv', header=2)
    GDP = (GDP.rename(columns={'Country Name':'Country'})
              .replace('Korea, Rep.', 'South Korea')
              .replace('Iran, Islamic Rep.', 'Iran')
              .replace('Hong Kong SAR, China', 'Hong Kong'))
    columns_to_keep = ['Country','2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013','2014', '2015']
    GDP = GDP[columns_to_keep]
    GDP = GDP.set_index('Country')

    ##### scimagojr DataFrame
    ScimEn = pd.read_excel('scimagojr.xlsx')
    rank_to_keep = (ScimEn['Rank']<=15)
    ScimEn = ScimEn[rank_to_keep]
    ScimEn = ScimEn.set_index('Country')

    df1 = pd.merge(ScimEn, energy, how='inner', left_index=True, right_index=True)
    #print(df1)
    df = pd.merge(df1,GDP, how='inner', left_index=True, right_index=True)
    return df
print(answer_one())

#################################################################################################
#Question 2:
#The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
#This function should return a single number.
def answer_two():
    df1_union = pd.merge(GDP, energy, how='outer', left_index=True, right_index=True)
    df_union = pd.merge(df1_union, GDP, how='outer', left_index=True, right_index=True)
    answer2 = len(df_union.index)-len(df.index)
    return answer2
print(answer_two())

#################################################################################################
#Question 3:
#What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
#This function should return a Series named avgGDP with 15 countries and their average GDP sorted in descending order.
def answer_three():
    df['avgGDP'] = (df['2006']+df['2007']+df['2008']+df['2009']+df['2010']+df['2011']+df['2012']+df['2013']+df['2014']+df['2015'])/10
    df_ave = df.sort_values(by='avgGDP', ascending=False)
    df_ave = df_ave['avgGDP']
    return df_ave
print(answer_three())

#################################################################################################
#Question 4:
#By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
#This function should return a single number.
def answer_four():
    df['avgGDP'] = (df['2006']+df['2007']+df['2008']+df['2009']+df['2010']+df['2011']+df['2012']+df['2013']+df['2014']+df['2015'])/10
    df_que6 = df.sort_values(by='avgGDP', ascending=False)
    country_6th = df_que6.index[5:6][0]
    #print(country_6th)
    GDP2006 = df_que6.loc[country_6th]['2006']
    GDP2015 = df_que6.loc[country_6th]['2015']
    diff = GDP2015 - GDP2006
    return diff    
print(answer_four())

#################################################################################################
#Qustion 5:
#What is the mean Energy Supply per Capita?
#This function should return a single number.
def answer_five():
    mean = df['Energy Supply per Capita'].mean()
    return mean
print(answer_five())

#################################################################################################
#Question 6:
#What country has the maximum % Renewable and what is the percentage?
#This function should return a tuple with the name of the country and the percentage.
def answer_six():
    max_rene = df['% Renewable'].max()
    for country in df.index:
        if df.loc[country]['% Renewable'] == max_rene:
            tupla = (country,max_rene)
    return tupla
print(answer_six())

#################################################################################################
#Question 7:
#Create a new column that is the ratio of Self-Citations to Total Citations. What is the maximum value for this new column, and what country has the highest ratio?
#This function should return a tuple with the name of the country and the ratio.
def answer_seven():
    df['ratio'] = df['Self-citations']/df['Citations']
    max_ratio = df['ratio'].max()
    for country in df.index:
        if df.loc[country]['ratio'] == max_ratio:
            tupla2 = (country, max_ratio)
    return tupla2
print(answer_seven())

#################################################################################################
#Quetion 8:
#Create a column that estimates the population using Energy Supply and Energy Supply per capita. What is the third most populous country according to this estimate?
def answer_eight():
    df['population'] = df['Energy Supply']/df['Energy Supply per Capita']
    df_que8 = df.sort_values(by='population', ascending=False)
    #print(df_que8['population'])
    answer8 = df_que8.index[2:3][0]
    return answer8
print(answer_eight())

#################################################################################################
#Question 9:
#Create a column that estimates the number of citable documents per person. What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the .corr() method, (Pearson's correlation).
#This function should return a single number.
#(Optional: Use the built-in function plot9() to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)
#print(df.head())
def answer_nine():
    df['Citable documents per Capita'] = df['Citable documents']/df['population']
    df_to_correlate = df[['Energy Supply per Capita','Citable documents per Capita']]
    corr = df_to_correlate.corr(method = 'pearson')
    answer9 = corr['Citable documents per Capita']['Energy Supply per Capita']
    return answer9
print(answer_nine())

#################################################################################################
#Question10:
#Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
#This function should return a series named HighRenew whose index is the country name sorted in ascending order of rank.
def answer_ten():
    median_renewable = df['% Renewable'].median()
    df_rank = df.sort_values(by='Rank', ascending=True)
    HighRenew = pd.Series()
    for country in df_rank.index:
        if df_rank.loc[country]['% Renewable'] >= median_renewable:
            HighRenew = HighRenew.append(pd.Series({country:1}))
        else:
            HighRenew = HighRenew.append(pd.Series({country:0}))
    return HighRenew
print(answer_ten())

#################################################################################################
#Question 11:
#Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.
ContinentDict  = {'China':'Asia', 'United States':'North America', 'Japan':'Asia', 'United Kingdom':'Europe', 'Russian Federation':'Europe', 'Canada':'North America', 'Germany':'Europe', 'India':'Asia', 'France':'Europe', 'South Korea':'Asia', 'Italy':'Europe', 'Spain':'Europe', 'Iran':'Asia', 'Australia':'Australia', 'Brazil':'South America'}
#This function should return a DataFrame with index named Continent ['Asia', 'Australia', 'Europe', 'North America', 'South America'] and columns ['size', 'sum', 'mean', 'std']
def answer_eleven():
    df = df.reset_index()
    df['Continent'] = df['Country'].map(ContinentDict)
    continent = df.groupby('Continent')['population'].agg({'size':len,'sum':np.sum, 'mean':np.mean, 'std':np.std})
    return continent
print(answer_eleven())

#################################################################################################
#Question 12:
#Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?
#This function should return a Series with a MultiIndex of Continent, then the bins for % Renewable. Do not include groups with no countries.
def answer_twelve():
    df_new_renewable = df
    df_new_renewable['% Renewable'] = pd.cut(df_new_renewable['% Renewable'],5)
    new_df = df.groupby(['Continent','% Renewable'])['Country'].agg({'num':len})
    return new_df
print(answer_twelve())

#################################################################################################
#Question 13:
def answer_therteen():
    df = df.set_index('Country')
    pop_est = pd.Series()
    for country in df.index:
        pop = df.loc[country]['population']
        split_pop = str(pop).split('.')
        if len(split_pop[0]) == 8:
            num = split_pop[0][0:2]+','+split_pop[0][2:5]+','+split_pop[0][5:9]+'.'+split_pop[1]
            pop_est = pop_est.append(pd.Series({country:num}))
        if len(split_pop[0]) == 9:
            num = split_pop[0][0:3]+','+split_pop[0][3:6]+','+split_pop[0][6:10]+'.'+split_pop[1]
            pop_est = pop_est.append(pd.Series({country:num}))
        if len(split_pop[0]) == 10:
            num = split_pop[0][0:1]+','+split_pop[0][1:4]+','+split_pop[0][4:7]+','+split_pop[0][7:10]+'.'+split_pop[1]
            pop_est = pop_est.append(pd.Series({country:num}))
    return pop_est
print(answer_therteen())
