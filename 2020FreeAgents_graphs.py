# 2020FreeAgents_graphs.py
# Created on 10/18/2019 by KAC

# import warnings filter and ignore warnings
from warnings import simplefilter
simplefilter(action='ignore', category=Warning)

# Load packages for analysis
import pandas as pd
from SpinRate import SpinRate
import matplotlib.pyplot as plt
import seaborn as sns

# Import player library and create a dictionary for looking up player IDs
data_dir = '/Users/Koby/PycharmProjects/FAPitcherAssessments/Input/'
df_player_names = pd.read_csv(data_dir + 'player_names.csv')
player_dict = dict(zip(df_player_names.mlb_name, df_player_names.mlb_id))

# League average spin rates, previously calculated
FF_league_spin = 2270
CU_league_spin = 2505
FT_league_spin = 2148

FF_league_spin_std = 175
CU_league_spin_std = 295
FT_league_spin_std = 175

# Pitchers to be assessed, broken into groups of 10
# pitcher_names = ['Gerrit Cole', 'Stephen Strasburg', 'Hyun-Jin Ryu', 'Zack Wheeler', 'Jake Odorizzi', 'Jose Quintana',
#                  'Madison Bumgarner', 'Homer Bailey', 'Michael Pineda', 'Yu Darvish']
# pitcher_names = ['Kyle Gibson', 'Cole Hamels', 'Adam Wainwright', 'Tanner Roark', 'Wade Miley', 'Brett Anderson',
#                   'Ivan Nova', 'Martin Perez', 'Andrew Cashner', 'Jason Vargas']
# pitcher_names = ['Rick Porcello', 'Julio Teheran', 'Gio Gonzalez', 'Jake Arrieta', 'Rich Hill', 'Dallas Keuchel',
#                  'Chris Archer', 'Corey Kluber', 'Matt Moore', 'Clay Buchholz']
# pitcher_names = ['Tyson Ross', 'Felix Hernandez', 'Jhoulys Chacin', 'Jeremy Hellickson', 'Michael Wacha', 'Alex Wood',
#                  'Edinson Volquez', 'Marco Estrada', 'Shelby Miller', 'Clayton Richard']
# pitcher_names = ['Drew Smyly', 'Wade LeBlanc', 'Matt Harvey', 'Ervin Santana', 'Trevor Cahill', 'Derek Holland',
#                  'Edwin Jackson', 'Aroldis Chapman', 'Yusmeiro Petit', 'Will Smith']
# pitcher_names = ['Kenley Jansen', 'Will Harris', 'Sergio Romo', 'Chris Martin', 'Jake Diekman', 'Brandon Kintzler',
#                  'Drew Pomeranz', 'Sean Doolittle', 'Brad Brach', 'Yoshihisa Hirano']
# pitcher_names = ['Collin McHugh', 'Juan Nicasio', 'Craig Stammen', 'Fernando Rodney', 'Joe Smith',
#                  'David Hernandez', 'Jeremy Jeffress', 'Tony Sipp', 'Cory Gearrin', 'Steve Cishek']\
# pitcher_names = ['Tommy Hunter', 'Josh Tomlin', 'Dellin Betances', "Darren O'Day", 'David Phelps', 'Luke Gregerson',
#                  'Aaron Loup', 'Matt Albers', 'Mike Dunn', 'Pedro Strop']
# pitcher_names = ['Greg Holland', 'Hector Santiago', 'Nate Jones', 'Tony Barnette', 'Tyler Thornburg', 'Arodys Vizcaino',
#                  'Dan Otero', 'Shawn Kelley', 'Pat Neshek', 'Seunghwan Oh']
# pitcher_names = ['Trevor Rosenthal', 'Tony Watson', 'Wily Peralta', 'Zach Duke', 'Jonny Venters',
#                  'Jared Hughes', 'Anthony Swarzak', 'Cody Allen', 'Adam Warren', 'Hector Rondon']

# Final pitchers identified in 2020FreeAgent_identifier.py code
pitcher_names = ['Rick Porcello', 'Tommy Hunter', 'Edinson Volquez', 'Yu Darvish', 'Jake Arrieta']


# Dates to get last two years of data
start_dates = '2018-03-15'
end_dates = '2019-10-01'

# Data for each pitcher using the SpinRate function
df_analysis = SpinRate(pitcher_names, start_dates, end_dates, player_dict)


# FF plot
sns.factorplot(x='Name', y='FF Spin', kind='bar', data=df_analysis, color='lightblue')
plt.xticks(rotation=90)
plt.axhline(FF_league_spin, color='gray')
plt.axhline(FF_league_spin + FF_league_spin_std, color='gray', linestyle='dotted')
plt.axhline(FF_league_spin - FF_league_spin_std, color='gray', linestyle='dotted')
plt.title('FF Spin Compared to League Average - 2020 Free Agent Pitcher')
plt.subplots_adjust(left=0.08, right=0.9, bottom=0.24, top=0.90)
plt.show()

# CU plot
sns.factorplot(x='Name', y='CU/KC Spin', kind='bar', data=df_analysis, color='lightblue')
plt.xticks(rotation=90)
plt.axhline(CU_league_spin, color='gray')
plt.axhline(CU_league_spin + CU_league_spin_std, color='gray', linestyle='dotted')
plt.axhline(CU_league_spin - CU_league_spin_std, color='gray', linestyle='dotted')
plt.title('CU/KC Spin Compared to League Average - 2020 Free Agent Pitchers')
plt.subplots_adjust(left=0.08, right=0.9, bottom=0.24, top=0.90)
plt.show()

# FT plot
sns.factorplot(x='Name', y='FT/SI Spin', kind='bar', data=df_analysis, color='lightblue')
plt.xticks(rotation=90)
plt.axhline(FT_league_spin, color='gray')
plt.axhline(FT_league_spin + FT_league_spin_std, color='gray', linestyle='dotted')
plt.axhline(FT_league_spin - FT_league_spin_std, color='gray', linestyle='dotted')
plt.title('FT/SI Spin Compared to League Average - 2020 Free Agent Pitchers')
plt.subplots_adjust(left=0.08, right=0.9, bottom=0.24, top=0.90)
plt.show()

# FT use plot
sns.factorplot(x='Name', y='FT/SI Use', kind='bar', data=df_analysis, color='lightblue')
plt.xticks(rotation=90)
plt.title('FT/SI Use - 2020 Free Agent Pitchers')
plt.subplots_adjust(left=0.08, right=0.9, bottom=0.24, top=0.90)
plt.show()

# FT wOBA plot
sns.factorplot(x='Name', y='FT/SI wOBA', kind='bar', data=df_analysis, color='lightblue')
plt.xticks(rotation=90)
plt.title('FT/SI wOBA - 2020 Free Agent Pitchers')
plt.subplots_adjust(left=0.08, right=0.9, bottom=0.24, top=0.90)
plt.show()

# Total wOBA plot
sns.factorplot(x='Name', y='Total wOBA', kind='bar', data=df_analysis, color='lightblue')
plt.xticks(rotation=90)
plt.axhline(0.322, color='gray')
plt.title('Total wOBA - 2020 Free Agent Pitchers')
plt.subplots_adjust(left=0.08, right=0.9, bottom=0.24, top=0.90)
plt.show()





