
from fastapi import FastAPI
from models import PlayerCreate

app = FastAPI()

players = []

@app.get("/players")
def get_players():
    return players

@app.post("/players")
def add_player(player: PlayerCreate):
    players.append(player.model_dump())
    return {"message": f"{player.name} has been added!"}


@app.get("/players/{name}")
def single_player(name: str):
    for player in players:
        if player['name'] == name:
            return player  
    return f'no player was found with the name {name}'


@app.delete('/players/{name}')
def delete_player(name: str):
    for player in players:
        if player['name'] == name:
            players.remove(player) 
            return f"{name} has been deleted!"
    return f"{name} was not found."