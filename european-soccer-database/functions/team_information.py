from data.dataframes import *

def get_team_basic_information(team_name):
    team_api_id = teams_df[teams_df.team_long_name == team_name].iloc[0]['team_api_id']

    match = matches_df[matches_df.home_team_api_id == team_api_id].iloc[0]
    team_country_id = match['country_id']
    print(team_country_id)

    team_country = countries_df[countries_df.id == team_country_id].iloc[0]['name']
    team_league = leagues_df[leagues_df.id == team_country_id].iloc[0]['name']

    return team_country, team_league