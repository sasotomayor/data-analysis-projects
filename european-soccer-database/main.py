from functions.team_information import get_team_basic_information, get_team_players

from data.dataframes import *

# Team's Analysis - KRC Genk

#Columns
print(teams_df.columns.to_list())

#Team + Attributes
print(teams_df[teams_df.team_long_name == 'KRC Genk'].merge(team_attributes_df, on=['team_api_id', 'team_fifa_api_id']))

#
#print(team_df[team_df.team_long_name == 'KRC Genk'].iloc[0]['team_api_id'])
#print(matches_df[matches_df.home_team_api_id == teams_df[teams_df.team_long_name == 'KRC Genk'].iloc[0]['team_api_id']].iloc[0])
print(get_team_basic_information('KRC Genk'))

#print(team_attributes_df.columns.to_list())

#print(matches_df.columns.to_list())
#print(matches_df[matches_df.home_team_api_id == 9987])