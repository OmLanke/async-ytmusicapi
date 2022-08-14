from ytmusicapi import YTMusic
import asyncio
import aiohttp
import orjson


async def test():
    async with aiohttp.ClientSession(json_serialize=orjson.dumps) as session:
        ytmusic = YTMusic(client_session=session)
        print(await ytmusic.search("Staying Alive", "songs"))


asyncio.run(test())
