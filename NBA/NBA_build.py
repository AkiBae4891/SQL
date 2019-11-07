import sqlite3
from sqlite3 import Error


def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    try:
        conn = sqlite3.connect('nba_db.sqlite3')
        print(sqlite3.version)
    finally:
        conn.close()

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