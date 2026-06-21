
from fastapi import FastAPI
from models import PlayerCreate
from database import create_players_table, add_players, get_all_players, get_one_player, delete_player
app = FastAPI()

create_players_table()

@app.get("/players")
def get_players():
    return get_all_players() 

@app.post("/players")
def add_player(player: PlayerCreate):
    return add_players(player)


@app.get("/players/{name}")
def single_player(name: str):
    return get_one_player(name)
    

@app.delete('/players/{name}')
def remove_player(name: str):
    return delete_player(name)
    