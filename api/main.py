import os
from dotenv import load_dotenv
import json 
import httpx
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
api = os.getenv("API_KEY")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",  
        "https://raptors-tracker.vercel.app/"  
    ],      
    allow_credentials=True,   
    allow_methods=["GET"],      
    allow_headers=["*"],
)

headers = {'Authorization':  api}
params = {'seasons[]': '2025', 'team_ids[]': '28'}
provider = "https://api.balldontlie.io/v1/games" 

async def raptors_games():
    try: 
        async with httpx.AsyncClient() as client:
            response = await client.get(provider, headers=headers, params=params)
            return response.json() 
    except Exception as e:
        print(f"An error occurred: {e}")   

@app.get("/games")
async def parse_games():
    raw_data = await raptors_games()
    cleaned_games = []

    for item in raw_data.get("data", []):
        game_info = {
            "date": item.get("date"),
            "home": item["home_team"]["full_name"],
            "home_score": item.get("home_team_score"),
            "visitor": item["visitor_team"]["full_name"],
            "visitor_score": item.get("visitor_team_score"),
        }
        cleaned_games.append(game_info)

    return cleaned_games

