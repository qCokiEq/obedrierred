import gd

client = gd.Client()


async def test():
    try:
        song = await client.get_song(1)
        print(song.name)
    except gd.errors.SongRestrictedForUsage:
        print("L")
client.run(test())

# OUTPUT: Random Song 01
