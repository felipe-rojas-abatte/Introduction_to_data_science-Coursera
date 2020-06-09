# Assignment 3 from coursera
import pandas as pd
import numpy as np
#from scipy.stats import ttest_ind
import re

#This assignment requires more individual learning than previous assignments - you are encouraged to check out the pandas documentation to find functions or methods you might not have used yet, or ask questions on Stack Overflow and tag them as pandas and python related. And of course, the discussion forums are open for interaction with your peers and the course staff.

#Definitions:

#A quarter is a specific three month period, Q1 is January through March, Q2 is April through June, Q3 is July through September, Q4 is October through December.
#A recession is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
#A recession bottom is the quarter within a recession which had the lowest GDP.
#A university town is a city which has a high percentage of university students compared to the total population of the city.
#Hypothesis: University towns have their mean housing prices less effected by recessions. Run a t-test to compare the ratio of the mean price of houses in university towns the quarter before the recession starts compared to the recession bottom. (price_ratio=quarter_before_recession/recession_bottom)

#The following data files are available for this assignment:

#From the Zillow research data site there is housing data for the United States. In particular the datafile for all homes at a city level, City_Zhvi_AllHomes.csv, has median home sale prices at a fine grained level.
#From the Wikipedia page on college towns is a list of university towns in the United States which has been copy and pasted into the file university_towns.txt.
#From Bureau of Economic Analysis, US Department of Commerce, the GDP over time of the United States in current dollars (use the chained value in 2009 dollars), in quarterly intervals, in the file gdplev.xls. For this assignment, only look at GDP data from the first quarter of 2000 onward.
#Each function in this assignment below is worth 10%, with the exception of run_ttest(), which is worth 50%.

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

#################################################################################################
##Question 1:
    #'''Returns a DataFrame of towns and the states they are in from the
    #university_towns.txt list. The format of the DataFrame should be:
    #DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ],
    #columns=["State", "RegionName"]  )

    #The following cleaning needs to be done:
    #1. For "State", removing characters from "[" to the end.
    #2. For "RegionName", when applicable, removing every character from " (" to the end.
    #3. Depending on how you read the data, you may need to remove newline character '\n'. '''

#df = pd.read_csv('university_towns_download.txt', header=-1, names=["States & Towns"])
#df = pd.read_excel('gdplev.xls')
#df = pd.read_csv('City_Zhvi_AllHomes.csv')

def get_list_of_university_towns():
    import re
    university_file = open('university_towns.txt', "r")
    lines = university_file.readlines()
    university_file.close()
    new_lines = []
    for l in lines:
        #print(l)
        if not re.match(r'^\s*$', l):
            new_lines.append(l)
    lines = new_lines.copy()

    for i, line in enumerate(lines):
        lines[i] = line.strip()

    df = pd.DataFrame(columns=('State', 'RegionName'))
    i = 0  # contador por cada linea en el data frame
    state_str = ""  # state_str inicial
    region_str = ""  # state_str inicial
    for l in lines:
        if '[edit]' in l:
            state_str = l.replace('[edit]', "")
        else:
            region_str = re.sub(r' \(.*', "", l)
            df.loc[i] = [state_str, region_str]
            i += 1
    return df
print(get_list_of_university_towns())

#################################################################################################
#Question 2:
#'''Returns the year and quarter of the recession start time as a
#string value in a format such as 2005q3'''

def get_recession_start():
    df = pd.read_excel('gdplev.xlsx', header = 5)
    df = df.reset_index()
    columns_to_keep = ['Unnamed: 3','GDP in billions of current dollars.1']
    df = (df[columns_to_keep].rename(columns={'Unnamed: 3':'YearQ','GDP in billions of current dollars.1':'GDP'})
                             .dropna())
    df['Year'] = df['YearQ'].str.split('Q').str[0]
    df['Quarter'] = df['YearQ'].str.split('Q').str[1]
    df['Year'] = pd.to_numeric(df['Year'])
    cond_2000 = (df['Year']>=2000)
    df = df[cond_2000]
    df = df.set_index('YearQ')
    GDP = df['GDP']
    for i in range(1,len(GDP)-2):
        if(GDP[i-1] < GDP[i] and GDP[i] > GDP[i+1] and GDP[i+1] > GDP[i+2]):# and GDP[i+2] > GDP[i+3]):
            recession = df[(df['GDP']==GDP[i])].index[0]
    return recession
print(get_recession_start())

#################################################################################################
#Question 3:
 #'''Returns the year and quarter of the recession end time as a
 #   string value in a format such as 2005q3'''
def get_recession_end():
    df = pd.read_excel('gdplev.xlsx', header = 5)
    df = df.reset_index()
    columns_to_keep = ['Unnamed: 3','GDP in billions of current dollars.1']
    df = (df[columns_to_keep].rename(columns={'Unnamed: 3':'YearQ','GDP in billions of current dollars.1':'GDP'})
                             .dropna())
    df['Year'] = df['YearQ'].str.split('Q').str[0]
    df['Quarter'] = df['YearQ'].str.split('Q').str[1]
    df['Year'] = pd.to_numeric(df['Year'])
    cond_2000 = (df['Year']>=2000)
    df = df[cond_2000]
    df = df.set_index('YearQ')
    GDP = df['GDP']
    for i in range(1,len(GDP)-2):
        if(GDP[i-1] < GDP[i] and GDP[i] > GDP[i+1] and GDP[i+1] > GDP[i+2]):
            id_recession = i
    for i in range(id_recession,len(GDP)-2):
        if(GDP[i-1] > GDP[i] and GDP[i] < GDP[i+1] and GDP[i+1] < GDP[i+2]):
            end_recession = df[(df['GDP']==GDP[i+2])].index[0]
    return end_recession
print(get_recession_end())

#################################################################################################
#Question 4:
#'''Returns the year and quarter of the recession bottom time as a
#    string value in a format such as 2005q3'''
def get_recession_bottom():
    df = pd.read_excel('gdplev.xlsx', header = 5)
    df = df.reset_index()
    columns_to_keep = ['Unnamed: 3','GDP in billions of current dollars.1']
    df = (df[columns_to_keep].rename(columns={'Unnamed: 3':'YearQ','GDP in billions of current dollars.1':'GDP'})
                             .dropna())
    df['Year'] = df['YearQ'].str.split('Q').str[0]
    df['Quarter'] = df['YearQ'].str.split('Q').str[1]
    df['Year'] = pd.to_numeric(df['Year'])
    cond_2000 = (df['Year']>=2000)
    df = df[cond_2000]
    df = df.set_index('YearQ')
    GDP = df['GDP']
    for i in range(1,len(GDP)-2):
        if(GDP[i-1] < GDP[i] and GDP[i] > GDP[i+1] and GDP[i+1] > GDP[i+2]):
            id_recession = i
    for i in range(id_recession,len(GDP)-2):
        if(GDP[i-1] > GDP[i] and GDP[i] < GDP[i+1]):
            recession_bottom = df[(df['GDP']==GDP[i])].index[0]
    return recession_bottom
print(get_recession_bottom())

#################################################################################################
#Question 5:
#'''Converts the housing data to quarters and returns it as mean
#values in a dataframe. This dataframe should be a dataframe with
# columns for 2000q1 through 2016q3, and should have a multi-index
# in the shape of ["State","RegionName"].
# Note: Quarters are defined in the assignment description, they are
# not arbitrary three month periods.
# The resulting dataframe should have 67 columns, and 10,730 rows.
def convert_housing_data_to_quarters():
    df = pd.read_csv('City_Zhvi_AllHomes.csv')
    df = df.replace('',np.nan)
    quarter = 0
    columns_to_keep = []
    for c in range(8,len(df.columns),3):
        year = df.columns[c][0:4]
        month = int(df.columns[c][5:7])
        if(month == 1):
            quarter = 'Q1'
            df[year+quarter] = (df[df.columns[c]]+df[df.columns[c+1]]+df[df.columns[c+2]])/3
        if(month == 4):
            quarter = 'Q2'
            df[year+quarter] = (df[df.columns[c]]+df[df.columns[c+1]]+df[df.columns[c+2]])/3
        if(month == 7):
            quarter = 'Q3'
            df[year+quarter] = (df[df.columns[c]]+df[df.columns[c+1]]+df[df.columns[c+2]])/3
        if(month == 10):
            quarter = 'Q4'
            df[year+quarter] = (df[df.columns[c]]+df[df.columns[c+1]]+df[df.columns[c+2]])/3
        if(int(year)>=2000 and int(year)<=2016): columns_to_keep.append(year+quarter)
    columns_to_keep = columns_to_keep[:-1]
    df = df.set_index(['State','RegionName'])
    df = df[columns_to_keep].dropna()
    return df.head()
print(convert_housing_data_to_quarters())

#################################################################################################
#Question 6:
#'''First creates new data showing the decline or growth of housing prices
#between the recession start and the recession bottom. Then runs a ttest
#comparing the university town values to the non-university towns values,
#return whether the alternative hypothesis (that the two groups are the same)
#is true or not as well as the p-value of the confidence.

#Return the tuple (different, p, better) where different=True if the t-test is
#True at a p<0.01 (we reject the null hypothesis), or different=False if
#otherwise (we cannot reject the null hypothesis). The variable p should
#be equal to the exact p value returned from scipy.stats.ttest_ind(). The
#value for better should be either "university town" or "non-university town"
#depending on which has a lower mean price ratio (which is equivilent to a
#reduced market loss).'''
def run_ttest():
    from scipy import stats
    list_university_towns_df = get_list_of_university_towns()
    housing_df = convert_housing_data_to_quarters()
    recession_start = get_recession_start()
    recession_end = get_recession_end()
    recession_bottom = get_recession_bottom()
    columns = housing_df.columns
    for c in range(1,len(columns)):
        if(columns[c] == recession_start):
            quarter_before_recession = columns[c-1]

    housing_df['Price Ratio'] = housing_df[recession_bottom] - housing_df[quarter_before_recession]
    housing_df = housing_df.dropna()

    housing_df = housing_df.reset_index()
    housing_df = housing_df.set_index(['State','RegionName'])

    list_university_towns_df['Class'] = 'University town'
    list_university_towns_df = list_university_towns_df.set_index(['State','RegionName'])

    df = pd.merge(housing_df, list_university_towns_df, how='outer', left_index=True, right_index=True)
    df['Class'] = df['Class'].replace(np.NaN, 'non University town', regex=True)
    columns_to_keep = ['Class', quarter_before_recession, recession_start, 'Price Ratio' ]
    df = df[columns_to_keep].dropna()
    non_university = df[df['Class'] == 'non University town']
    university = df[df['Class'] == 'University town']

    T_test = stats.ttest_ind(non_university['Price Ratio'], university['Price Ratio'])
    print(T_test)

    test, pvalue = stats.ttest_ind(non_university['Price Ratio'],university['Price Ratio'])
    print(test)

    if pvalue < 0.01: different = True
    else: different = False

    better = ""
    if university['Price Ratio'].mean() > non_university['Price Ratio'].mean():
        better = "university town"
    else:
        better = "non-university town"

    return (different, pvalue, better)
print(run_ttest())
