import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "https://www.enjoyalgorithms.com"
    data = await fetch_data(url)
    print(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
