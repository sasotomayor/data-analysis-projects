from data.dataframes import *

def get_team_basic_information(team_name):
    team_api_id = teams_df[teams_df.team_long_name == team_name].iloc[0]['team_api_id']

    match = matches_df[matches_df.home_team_api_id == team_api_id].iloc[0]
    team_country_id = match['country_id']

    team_country = countries_df[countries_df.id == team_country_id].iloc[0]['name']
    team_league = leagues_df[leagues_df.id == team_country_id].iloc[0]['name']

    return team_country, team_league

def get_team_results(team_name):
    team_api_id = teams_df[teams_df.team_long_name == team_name].iloc[0]['team_api_id']
    
    home_matches = matches_df[matches_df.home_team_api_id == team_api_id]
    away_matches = matches_df[matches_df.away_team_api_id == team_api_id]

    draws = len(home_matches[home_matches['home_team_goal'] == home_matches['away_team_goal']]) + len(away_matches[away_matches['home_team_goal'] == away_matches['away_team_goal']])
    wins = len(home_matches[home_matches['home_team_goal'] > home_matches['away_team_goal']]) + len(away_matches[away_matches['home_team_goal'] < away_matches['away_team_goal']])
    defeats = len(home_matches[home_matches['home_team_goal'] < home_matches['away_team_goal']]) + len(away_matches[away_matches['home_team_goal'] > away_matches['away_team_goal']])

    return wins, draws, defeats