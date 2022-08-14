from ytmusicapi import YTMusic
import asyncio


ytmusic = YTMusic()


async def test():
    print(await ytmusic.search("Staying Alive", "songs"))


asyncio.run(test())
