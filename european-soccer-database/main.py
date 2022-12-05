import numpy as np
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

from functions.read_database_table import read_database_table

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

# Establish connection with the database
database_path = "/Users/ssotomayorba/Documents/Personal/projects/data-analysis-projects/european-soccer-database/data/database.sqlite"
conn = sqlite3.connect(database_path)

# Read the different available tables
tables = read_database_table('sqlite_master', conn, "WHERE type='table'")

for index, row in tables.iterrows():
    print(row.tbl_name)

countries_df = read_database_table('Country', conn)

print(countries_df.size)