from functions.team_information import get_team_basic_information

from data.dataframes import *

# Team's Analysis - KRC Genk

#Columns
print(teams_df.columns.to_list())

#Team + Attributes
print(teams_df[teams_df.team_long_name == 'KRC Genk'].merge(team_attributes_df, on=['team_api_id', 'team_fifa_api_id']))

#
#print(team_df[team_df.team_long_name == 'KRC Genk'].iloc[0]['team_api_id'])
#print(matches_df[matches_df.home_team_api_id == teams_df[teams_df.team_long_name == 'KRC Genk'].iloc[0]['team_api_id']].iloc[0])
#print(get_team_basic_information('KRC Genk'))

#print(team_attributes_df.columns.to_list())

#print(matches_df.columns.to_list())
#print(matches_df[matches_df.home_team_api_id == 9987])

print(matches_df.columns.tolist())

team_api_id = teams_df[teams_df.team_long_name == 'KRC Genk'].iloc[0]['team_api_id']
home_matches = matches_df[matches_df.home_team_api_id == team_api_id]
away_matches = matches_df[matches_df.away_team_api_id == team_api_id]
wins = len(home_matches[home_matches['home_team_goal'] > home_matches['away_team_goal']]) + len(away_matches[away_matches['home_team_goal'] < away_matches['away_team_goal']])
loses = len(home_matches[home_matches['home_team_goal'] < home_matches['away_team_goal']]) + len(away_matches[away_matches['home_team_goal'] > away_matches['away_team_goal']])
draws = len(home_matches[home_matches['home_team_goal'] == home_matches['away_team_goal']]) + len(away_matches[away_matches['home_team_goal'] == away_matches['away_team_goal']])
print(len(home_matches) + len(away_matches))
print(wins, loses, draws)

