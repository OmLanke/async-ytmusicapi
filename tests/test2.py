from time import time
from ytmusicapi import YTMusic
import asyncio
import aiohttp


async def test():
    time_now = time()
    async with aiohttp.ClientSession() as session:
        ytmusic = YTMusic(client_session=session)

        async def func():
            await ytmusic.search("Staying Alive", "songs")

        await asyncio.gather(*[func() for i in range(1000)])
    print(time() - time_now)


asyncio.run(test())
