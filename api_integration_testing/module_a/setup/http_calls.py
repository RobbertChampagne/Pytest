import httpx
import asyncio

async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.status_code, response.json()['data']