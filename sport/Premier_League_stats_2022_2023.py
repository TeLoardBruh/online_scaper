import streamlit as st
import numpy as np
import pandas as pd
import os
import glob

all_files = glob.glob(os.path.join(f'{os.path.dirname(os.path.abspath(__file__))}/data/', "*.csv"))
fnames = []
for fname in all_files:
    pd.read_csv(fname)
    fnames.append(os.path.basename(fname).split('.csv')[0])

st.title("Premier league teams stats")
st.subheader("2022-2023 :flag-england: :soccer:")
st.caption("show relationship of games play, formation")

option = st.selectbox("Choose your team ",fnames)

team_name = option

total_winning_form = f'total_winning_formation_{team_name}'
total_losing_form = f'total_losing_formation_{team_name}'
total_draw_form = f'total_draw_formation_{team_name}'

team_winning_formation_home = f'team_winning_formation_home_{team_name}'
team_losing_formation_home = f'team_losing_formation_home_{team_name}'

team_winning_formation_away_venue = f'team_winning_formation_away_venue_{team_name}'
team_losing_formation_away_venue = f'team_losing_formation_away_venue_{team_name}'

team_draw_formation_home_venue = f'team_draw_formation_home_venue_{team_name}'
team_draw_formation_away_venue = f'team_draw_formation_away_venue_{team_name}'

tab1, tab2 = st.tabs(["Season 2022-2023 Matches |", "Winning And Losing Formation (Home and Away) |"])

total_winning_home_away = 'Total winning (home & away)'
total_losing_home_away = 'Total losing (home & away)'
total_draw_home_away = 'Total draw (home & away)'
total_winning_home = 'Total winnning home'
total_winning_away = 'Total winning away'
total_losing_home= 'Total losing home'
total_losing_away = 'Total losing away'
total_draw_home = 'Total draw home'
total_draw_away = 'Total draw away'
def read_csv_from_path(team_name):
    return pd.read_csv(f"{os.path.dirname(os.path.abspath(__file__))}/data/{team_name}.csv")

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
    team_draw_formation = get_formation_win_lose(team_name, 'D')

    team_winning_formation_home_venue = get_formation_win_lose_venue(team_name, 'W', 'Home')
    team_losing_formation_home_venue = get_formation_win_lose_venue(team_name,'L', 'Home')

    team_winning_formation_away_venue = get_formation_win_lose_venue(team_name,'W', 'Away')
    team_losing_formation_away_venue =  get_formation_win_lose_venue(team_name,'L', 'Away')

    team_draw_formation_home_venue = get_formation_win_lose_venue(team_name,'D', 'Home')
    team_draw_formation_away_venue =  get_formation_win_lose_venue(team_name,'D', 'Away')

    return {
        f'total_winning_formation_{team_name}': team_winning_formation, 
        f'total_losing_formation_{team_name}': team_losing_formation, 
        f'total_draw_formation_{team_name}': team_draw_formation, 
        f'team_winning_formation_home_{team_name}': team_winning_formation_home_venue, 
        f'team_losing_formation_home_{team_name}': team_losing_formation_home_venue,
        f'team_winning_formation_away_venue_{team_name}': team_winning_formation_away_venue,
        f'team_losing_formation_away_venue_{team_name}': team_losing_formation_away_venue,
        f'team_draw_formation_home_venue_{team_name}': team_draw_formation_home_venue,
        f'team_draw_formation_away_venue_{team_name}': team_draw_formation_away_venue,
        }


st.divider()

with tab1:
   df = read_csv_from_path(team_name)
   
   col1, col2, col3, col4 = st.columns(4)
   total_win = df['Result'].value_counts().to_list()[0]
   total_lose = df['Result'].value_counts().to_list()[1]
   total_draw = df['Result'].value_counts().to_list()[2]

   col1.metric("Total game played", f"{len(df)}")
   col2.metric("Total winning", f"{total_win}")
   col3.metric("Total Losing", f"{total_lose}")
   col4.metric("Total Draw", f"{total_draw}")
   
   st.subheader(f'All competition stats {team_name}')
   df

with tab2:
    select_stats_formation = st.selectbox("Select which stats you want to see.",[total_winning_home_away, total_losing_home_away ,total_winning_home, total_winning_away, total_losing_home, total_losing_away])

    if select_stats_formation == total_winning_home_away:
        st.subheader("Team total winning game both home and away and the formation 🏆")
        col1, col2, col3, col4 = st.columns(4)
        df = read_csv_from_path(team_name)
   
        col1, col2, col3, col4 = st.columns(4)
        total_win = df['Result'].value_counts().to_list()[0]
        total_winning_home_stats = df[(df['Result'] == 'W') & (df['Venue']== 'Home')].value_counts().value_counts().to_list()[0]

        total_winning_away_stats =df[(df['Result'] == 'W') & (df['Venue']== 'Away')].value_counts().value_counts().to_list()[0]

        col1.metric("Total game played", f"{len(df)}")
        col2.metric("Total winning", f"{total_win}")
        col3.metric("Total winning home", f"{total_winning_home_stats}")
        col4.metric("Total winning away", f"{total_winning_away_stats}")
        
        st.bar_chart(relation_dataframe(team_name)[total_winning_form])

    if select_stats_formation == total_losing_home_away:
        st.subheader("Team total losing game both home and away and the formation 🌧️")
        st.bar_chart(relation_dataframe(team_name)[total_losing_form])

    if select_stats_formation == total_draw_home_away:
        st.subheader("Team total draw game at away ground and the formation 🌧️")
        st.bar_chart(relation_dataframe(team_name)[total_draw_form])

    if select_stats_formation == total_winning_home:
        st.subheader("Team total winning game at home and the formation 🏆")
        st.bar_chart(relation_dataframe(team_name)[team_winning_formation_home])

    if select_stats_formation == total_winning_away:
        st.subheader("Team total winning game at away ground and the formation 🏆")
        st.bar_chart(relation_dataframe(team_name)
        [team_winning_formation_away_venue])

    if select_stats_formation == total_losing_home:
        st.subheader("Team total losing game at home and the formation 🌧️")
        st.bar_chart(relation_dataframe(team_name)[team_losing_formation_home])

    if select_stats_formation == total_losing_away:
        st.subheader("Team total losing game at away ground and the formation 🌧️")
        st.bar_chart(relation_dataframe(team_name)[team_losing_formation_away_venue])
    
    if select_stats_formation == total_draw_home:
        st.subheader("Team total draw game at home ground and the formation 🟰")
        st.bar_chart(relation_dataframe(team_name)[team_draw_formation_home_venue])

    if select_stats_formation == total_draw_away:
        st.subheader("Team total draw game at away ground and the formation 🟰")
        st.bar_chart(relation_dataframe(team_name)[team_draw_formation_away_venue])

