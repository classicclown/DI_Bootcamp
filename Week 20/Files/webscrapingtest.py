import asyncio
import aiohttp
import csv
import json
import ssl
import certifi
from typing import List, Dict
from datetime import datetime

LIMIT = 500

API_CLIENT_ID = "tp727tqv2zbm7mwh8e51dkz69suiz7"
API_ACCESS_TOKEN = "ns8jc9nu4ihapg0ly980q70dn2wwhh"

ssl_context = ssl.create_default_context(cafile=certifi.where())

async def fetch_data(session: aiohttp.ClientSession, endpoint: str, options: str) -> Dict:
    url = f"https://api.igdb.com/v4/{endpoint}"
    headers = {
        'Client-ID': API_CLIENT_ID,
        'Authorization': f'Bearer {API_ACCESS_TOKEN}'
    }
    async with session.post(url, headers=headers, data=options, ssl=ssl_context) as response:
        return await response.json()

async def get_games_batch(session: aiohttp.ClientSession, offset: int) -> List[Dict]:
    options = f'fields id, name, rating, rating_count, aggregated_rating, aggregated_rating_count, first_release_date; sort rating desc; where aggregated_rating_count > 0; limit {LIMIT}; offset {offset};'
    return await fetch_data(session, 'games', options)


# def unix_to_year(unix_timestamp):
#     if unix_timestamp is None:
#         return 'NA'
#     try:
#         return datetime.utcfromtimestamp(unix_timestamp).year
#     except (ValueError, OverflowError):
#         return 'NA'

async def process_games(total_games: int = 10000):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for offset in range(0, total_games, LIMIT):
            tasks.append(get_games_batch(session, offset))
        
        all_games = await asyncio.gather(*tasks)
    
    flattened_games = [game for batch in all_games for game in batch]
    
    with open('game_titles2.csv', 'w', newline='', encoding='utf-8') as myfile:
        column_headers = ['ID', 'Name', 'Release Year', 'User Rating', 'Num of Ratings', 'Critic Rating', 'Num of Critic Ratings']
        wr = csv.DictWriter(myfile, fieldnames=column_headers)
        wr.writeheader()

        for item in flattened_games:
            release_year = (item.get('first_release_date'))

            wr.writerow({
                'ID': item.get('id', 'N/A'),
                'Name': item.get('name', 'N/A'),
                'Release Year': release_year,
                'User Rating': round(item.get('rating', 'N/A'), 2) if item.get('rating') is not None else 'N/A',
                'Num of Ratings': item.get('rating_count', 'N/A'),
                'Critic Rating': round(item.get('aggregated_rating', 'N/A'), 2) if item.get('aggregated_rating') is not None else 'N/A',
                'Num of Critic Ratings': item.get('aggregated_rating_count', 'N/A')
            })

    print("Games saved to 'game_titles.csv'")

asyncio.run(process_games(10000))