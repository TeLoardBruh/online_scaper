import streamlit as st
import numpy as np
import pandas as pd
import os
import glob


path = "./data/"

def read_csv_from_path(team_name):
    return pd.read_csv(os.path.join(path, f"{team_name}.csv"))

def explore_team_formation(team_name):
    team = read_csv_from_path(team_name)
    team_formation = team['Formation'].str.replace('◆','').str.replace('Formation', ' ').value_counts()
    return team_formation



def get_formation_win_lose(team_name, result):
    team = read_csv_from_path(team_name)
    return team[(team['Result'] == result)]['Formation'].str.replace('◆','').str.replace('Formation', ' ').value_counts()
   

def get_formation_win_lose_venue(team_name, result, venue):
    team = read_csv_from_path(team_name)
    return team[(team['Result'] == result) & (team['Venue'] == venue)]['Formation'].str.replace('◆','').str.replace('Formation', ' ').value_counts()    

def relation_dataframe(team_name):

    team_winning_formation = get_formation_win_lose(team_name, 'W')
    team_losing_formation = get_formation_win_lose(team_name, 'L')

    team_winning_formation_home_venue = get_formation_win_lose_venue(team_name, 'W', 'Home')    
    team_losing_formation_home_venue = get_formation_win_lose_venue(team_name,'L', 'Home')    

    team_winning_formation_away_venue = get_formation_win_lose_venue(team_name,'W', 'Away')
    team_losing_formation_away_venue =  get_formation_win_lose_venue(team_name,'L', 'Away')

    return {
        f'total_winning_formation_{team_name}': team_winning_formation, 
        f'total_losing_formation_{team_name}': team_losing_formation, 
        f'team_winning_formation_home_{team_name}': team_winning_formation_home_venue, 
        f'team_losing_formation_home_{team_name}': team_losing_formation_home_venue,
        f'team_winning_formation_away_venue_{team_name}': team_winning_formation_away_venue,
        f'team_losing_formation_away_venue_{team_name}': team_losing_formation_away_venue
        }



all_files = glob.glob(os.path.join(path, "*.csv"))
fnames = []
for fname in all_files:
    pd.read_csv(fname)
    fnames.append(os.path.basename(fname).split('.csv')[0])

st.markdown("# Premier league stats 2022-2023")
st.markdown("#### show relationship of games play, formation")



option = st.selectbox("Choose your team ",fnames)

team_name = option
total_winning_form = f'total_winning_formation_{team_name}'
total_losing_form = f'total_losing_formation_{team_name}'
team_winning_formation_home = f'team_winning_formation_home_{team_name}'
team_losing_formation_home = f'team_losing_formation_home_{team_name}'
team_winning_formation_away_venue = f'team_winning_formation_away_venue_{team_name}'
team_losing_formation_away_venue = f'team_losing_formation_away_venue_{team_name}'

st.markdown("### Team total winning game both home and away and the formation 🏆")
st.bar_chart(relation_dataframe(team_name)[total_winning_form])
st.markdown("### Team total losing game both home and away and the formation 🌧️")
st.bar_chart(relation_dataframe(team_name)[total_losing_form])
st.markdown("###Team total winning game at home and the formation 🏆")
st.bar_chart(relation_dataframe(team_name)[team_winning_formation_home])
st.markdown("### Team total losing game at home and the formation 🌧️")
st.bar_chart(relation_dataframe(team_name)[team_losing_formation_home])
st.markdown("### Team total winning game at away ground and the formation 🏆")
st.bar_chart(relation_dataframe(team_name)[team_winning_formation_away_venue])
st.markdown("### Team total losing game at away ground and the formation 🌧️")
st.bar_chart(relation_dataframe(team_name)[team_losing_formation_away_venue])
