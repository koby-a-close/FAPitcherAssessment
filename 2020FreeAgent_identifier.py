# 2020FreeAgents_identifier.py

# import warnings filter and ignore warnings
from warnings import simplefilter
simplefilter(action='ignore', category=Warning)

# Load packages for analysis
import pandas as pd
from SpinRate import SpinRate

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

# Pitchers to be assessed
# FREE AGENT START PITCHER NAMES
pitcher_names = ['Gerrit Cole', 'Stephen Strasburg', 'Hyun-Jin Ryu', 'Zack Wheeler', 'Jake Odorizzi', 'Jose Quintana',
                 'Madison Bumgarner', 'Homer Bailey', 'Michael Pineda', 'Yu Darvish', 'Kyle Gibson', 'Cole Hamels',
                 'Adam Wainwright', 'Tanner Roark', 'Wade Miley', 'Brett Anderson', 'Ivan Nova', 'Martin Perez',
                 'Andrew Cashner', 'Jason Vargas', 'Rick Porcello', 'Julio Teheran', 'Gio Gonzalez', 'Jake Arrieta',
                 'Rich Hill', 'Dallas Keuchel', 'Chris Archer', 'Corey Kluber', 'Matt Moore', 'Clay Buchholz',
                 'Tyson Ross', 'Felix Hernandez', 'Jhoulys Chacin', 'Jeremy Hellickson', 'Michael Wacha', 'Alex Wood',
                 'Edinson Volquez', 'Marco Estrada', 'Shelby Miller', 'Clayton Richard', 'Drew Smyly', 'Wade LeBlanc',
                 'Matt Harvey', 'Ervin Santana', 'Trevor Cahill', 'Derek Holland', 'Edwin Jackson', 'Aroldis Chapman',
                 'Yusmeiro Petit', 'Will Smith', 'Kenley Jansen', 'Will Harris', 'Sergio Romo', 'Chris Martin',
                 'Jake Diekman', 'Brandon Kintzler', 'Drew Pomeranz', 'Sean Doolittle', 'Brad Brach',
                 'Yoshihisa Hirano', 'Collin McHugh', 'Juan Nicasio', 'Craig Stammen', 'Fernando Rodney', 'Joe Smith',
                 'David Hernandez', 'Jeremy Jeffress', 'Tony Sipp', 'Cory Gearrin', 'Steve Cishek', 'Tommy Hunter',
                 'Josh Tomlin', 'Dellin Betances', "Darren O'Day", 'David Phelps', 'Luke Gregerson', 'Aaron Loup',
                 'Matt Albers', 'Mike Dunn', 'Pedro Strop', 'Greg Holland', 'Hector Santiago', 'Nate Jones',
                 'Tony Barnette', 'Tyler Thornburg', 'Arodys Vizcaino', 'Dan Otero', 'Shawn Kelley', 'Pat Neshek',
                 'Seunghwan Oh', 'Trevor Rosenthal', 'Tony Watson', 'Wily Peralta', 'Zach Duke', 'Jonny Venters',
                 'Jared Hughes', 'Anthony Swarzak', 'Cody Allen', 'Adam Warren', 'Hector Rondon']

# Dates to get last two years of data
start_dates = '2018-03-15'
end_dates = '2019-10-01'

# Data for each Astros pitcher before and after joining team
df_analysis = SpinRate(pitcher_names, start_dates, end_dates, player_dict)
df_analysis = df_analysis.reset_index()

ID_count = 0

for i in range(len(df_analysis)):
    if ((df_analysis['FF Spin'][i] > 2388 or df_analysis['CU/KC Spin'][i] > 2704)
            and df_analysis['FT/SI Spin'][i] > FT_league_spin
            and df_analysis['FT/SI Use'][i] > 0.10
            and df_analysis['FT/SI wOBA'][i] > 0.30):
        print(df_analysis['Name'][i])
        ID_count += 1

print("{} pitchers were identified".format(ID_count))

