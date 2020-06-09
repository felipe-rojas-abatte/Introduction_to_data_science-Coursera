# Assignment 2 from coursera
import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
print(df.head())

#############################################################################################
##Question 0
# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
print(answer_zero() )

#############################################################################################
##Question 1
# Which country has won the most gold medals in summer games?
# This function should return a single string value.
def answer_one():
    # I find the max number of gold medals
    max_summer_gold_medals = max(df['Gold'])
    # with this number we create a condition to find the more winning country
    condition_of_winner = (df['Gold'] == max_summer_gold_medals)
    # I applied the condition into the DataFrame and store the value
    country_more_winning = df[condition_of_winner]['ID'].index[0]
    return country_more_winning
print(answer_one())

#############################################################################################
#Question 2
# Which country had the biggest difference between their summer and winter gold medal counts?
# This function should return a single string value.

def answer_two():
    # I create a column with the difference of summer gold medals and winter gold medals
    df['diff_between_medals'] = df['Gold'] - df['Gold.1']
    # I find the max difference in diff_between_medals column
    max_diff_between_medals = max(df['diff_between_medals'])
    # I create a condition to find the country with more difference between summer and winter
    condition_for_country = (df['diff_between_medals'] == max_diff_between_medals)
    # Applied the condition into the DataFrame and store the value
    country_more_diff = df[condition_for_country]['ID'].index[0]
    return country_more_diff
print(answer_two())

#############################################################################################
#Question 3
# Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count? Only include countries that have won at least 1 gold in both summer and winter.
# This function should return a single string value.

def answer_three():
    # Condition for coutries that have won at least 1 gold medal in both summer and winter
    at_least_1_gold_summer = (df['Gold'] > 0)
    at_least_1_gold_winter = (df['Gold.1'] > 0)
    condition_gold = (at_least_1_gold_summer & at_least_1_gold_winter)
    # I create a column with the difference of summer gold and winter gold medals relative to total gold medals
    df['relative_diff_between_medals'] = abs((df['Gold'] - df['Gold.1'])/df['Gold.2'])
    # I applied the condition_gold to the DataFrame
    relative_diff_country = df[condition_gold]['relative_diff_between_medals']
    # find the maximum relative difference
    max_relative_diff = max(relative_diff_country)
    # I create a condition to find the country with more difference between summer and winter relative to total gold models
    condition_for_country = (df['relative_diff_between_medals'] == max_relative_diff)
    # Applied the condition into the DataFrame and store the value
    country_more_relative_diff = df[condition_for_country]['ID'].index[0]
    return country_more_relative_diff
print(answer_three())

#############################################################################################
#Question 4
#Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. The function should return only the column (a Series object) which you created, with the country names as indices.
#This function should return a Series named Points of length 146

def answer_four():
    # I assign the points for each number of medals
    gold_points = df['Gold.2']*3
    silver_points = df['Silver.2']*2
    bronze_points = df['Bronze.2']
    # I create a new columns called Points where I stored the total number of points
    df['Points'] = gold_points + silver_points + bronze_points
    points = df['Points']
    print(points.count())
    return points
print(answer_four())

#############################################################################################
## second part
#############################################################################################
census_df = pd.read_csv('census.csv')
print(census_df.head())

#############################################################################################
#Question 5
# Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
# This function should return a single string value.

def answer_five():
    #I work only with counties
    city_name_county = (census_df['SUMLEV'] == 50)
    df = census_df[city_name_county]
    # I see how many unique states exist and I store the list on states
    states = df['STNAME'].unique()
    # Change the original index to STANME and CTYNAME
    df = df.set_index(['STNAME','CTYNAME'])
    # define the maximun number of counties per state
    max_num_counties = 0
    # run a loop over all states
    for state in states:
      # I count the number os counties per state
      num_counties = len(df.loc[state])
      # I find the state with most counties
      max_num_counties = max(num_counties, max_num_counties)
      if (max_num_counties == num_counties): 
         win_state = state
    return win_state 
print(answer_five())

#############################################################################################
#Question 6
#Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)? Use CENSUS2010POP.
#This function should return a list of string values.
def answer_six():
    columns_to_keep = ['STNAME','CTYNAME','CENSUS2010POP']
    city_name_county = (census_df['SUMLEV'] == 50)
    df = census_df[city_name_county]
    df = df[columns_to_keep]
    states = df['STNAME'].unique()
    df = df.set_index(['STNAME'])
    select_df = pd.DataFrame()#columns = ['SUMA'] , index = ['STNAME'])
    answer = []
    for state in states:
       counties = df.loc[state]
       if(state == 'District of Columbia'): continue
       counties = counties.sort_values(by='CENSUS2010POP', ascending=False)
       counties = counties[:3]
       sum_pop = counties['CENSUS2010POP'].sum()
       row_serie = pd.Series(data={'SUMA': sum_pop}, name=(state))
       select_df = select_df.append(row_serie)
    select_df = select_df.sort_values(by='SUMA', ascending=False)
    select_df = select_df[:3]
    selected_states = select_df.index.unique()
    for s in selected_states:
       answer.append(s)
    return answer

print(answer_six())

#############################################################################################
#Question 7
#Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
# e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
# This function should return a single string value.

def answer_seven():
    columns_to_keep = ['CTYNAME','POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
    city_name_county = (census_df['SUMLEV'] == 50)
    df = census_df[city_name_county]
    df = df[columns_to_keep]
    df = df.set_index(['CTYNAME'])
    for i in range(0,6,1):
        for j in range (i,6,1):
            if(i==j): continue
            else:
                df['201'+str(i)+'-201'+str(j)] = abs(df['POPESTIMATE201'+str(i)] - df['POPESTIMATE201'+str(j)])
    df['max_pop'] = df[['2010-2011', '2010-2012', '2010-2013', '2010-2014', '2010-2015', '2011-2012', '2011-2013', '2011-2014', '2011-2015', '2012-2013', '2012-2014', '2012-2015', '2013-2014', '2013-2015', '2014-2015']].max(axis=1) 
    #print(df.head())
    county_max_change_pop = max(df['max_pop'])
    cond = (df['max_pop'] == county_max_change_pop)
    answer = df[cond]['max_pop'].index[0]
    return answer

print(answer_seven())

#############################################################################################
#Question 8
# In this datafile, the United States is broken up into four regions using the "REGION" column.
# Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE2014.
# This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).

def answer_eight():
    columns_to_keep = ['STNAME','CTYNAME','REGION','POPESTIMATE2014','POPESTIMATE2015']
    city_name_county = (census_df['SUMLEV'] == 50)
    df = census_df[city_name_county]
    df = df[columns_to_keep]
    belong_to_R1 = (df['REGION'] == 1)
    belong_to_R2 = (df['REGION'] == 2)
    condition_for_region = (belong_to_R1 | belong_to_R2)
    condition_for_pop = (df['POPESTIMATE2015'] > df['POPESTIMATE2014'])
    condition_for_ctyname = (df['CTYNAME'].str.startswith('Washington'))
    all_conditions = condition_for_region & condition_for_ctyname & condition_for_pop
    answer = df[all_conditions][['STNAME','CTYNAME','REGION','POPESTIMATE2014','POPESTIMATE2015']]
    return answer 
print(answer_eight())

