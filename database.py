import sqlite3 
from models import PlayerCreate


def create_players_table() -> None: 
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PLAYERS(
                   ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                   NAME TEXT NOT NULL, 
                   POSITION TEXT NOT NULL, 
                   PHONE TEXT NOT NULL)
    ''')
    conn.commit()
    conn.close()

def add_players(player: PlayerCreate) -> str: 
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO PLAYERS (NAME, POSITION, PHONE)
        VALUES (?, ?, ?)
    ''', (player.name, player.position, player.phone))

    conn.commit()
    conn.close()
    return 'player added to the database'

def get_all_players() -> list:

    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    players_list = []

    cursor.execute('SELECT * FROM PLAYERS')
    all_players = cursor.fetchall()

    for player in all_players:
        players_list.append(PlayerCreate(name = player[1], position = player[2], phone = player[3]))
    
    conn.close()

    return players_list


def get_one_player(name: str)-> str:
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM PLAYERS WHERE NAME = ?', (name,))
    player = cursor.fetchone()
    conn.close()

    if player:
        return PlayerCreate(name = player[1], position = player[2], phone = player[3])
    else:
        return "Player not found"
    

def delete_player(name: str) -> str:
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM PLAYERS WHERE NAME = ?
    ''', (name,))
    conn.commit()
    conn.close()
    return f'{name} has been deleted!'