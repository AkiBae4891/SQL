import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from sqlite3 import Error

# Creating SQLite DB for NBA draft Data


df = pd.read_csv('https://query.data.world/s/rfugrlxorfagiv2cxyac6rujtzz6fw')
print("Shape of DF:", df.shape)
print(df.head())



conn = sqlite3.connect('nba_db.sqlite3')
curs = conn.cursor()


    for player in range(len(df)):
        # loop for players to add to db
        sequence = (tuple(df.loc[player].values))
        insert_player = """
        INSERT INTO nba_db
        ('Unnamed: 0', 'Player', 'All_NBA', 'All.Star', 'Draft_Yr', 'Pk', 'Team',
           'College', 'Yrs', 'Games', 'Minutes.Played', 'PTS', 'TRB', 'AST',
           'FG_Percentage', 'TP_Percentage', 'FT_Percentage', 'Minutes.per.Game',
           'Points.per.Game', 'TRB.per.game', 'Assits.per.Game', 'Win.Share',
           'WS_per_game', 'BPM', 'VORP', 'Executive', 'Tenure', 'Exec_ID',
           'Exec_draft_exp', 'attend_college', 'first_year', 'second_year',
           'third_year', 'fourth_year', 'fifth_year')
           VALUES """ + str(sequence) + ';'
        curs.execute(insert_player)

if __name__ == '__main__':
    create_connection()
