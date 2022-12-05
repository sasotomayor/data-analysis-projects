import pandas as pd

def read_database_table(table_name, connection, condition=''):
    query = 'SELECT * FROM ' + table_name + " " + condition
    return pd.read_sql(query, connection)