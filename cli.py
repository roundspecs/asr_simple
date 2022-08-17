import json
from typing import List
import typer

app = typer.Typer()

def get_db():
    with open('db.json', 'r') as f:
        return json.load(f)

@app.command()
def start(name: str):
    db: List = get_db()
    db.append()
    with open('db.json', 'w') as f:
        pass