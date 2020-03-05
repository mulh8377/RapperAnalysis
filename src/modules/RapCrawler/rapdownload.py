import urllib.request
import argparse
import threading
import asyncio

import rapquery as rq
import rapfile as rf

async def download_artist_page():
    pass

async def download_artist_songs():
    pass

async def download_artist_picture():
    pass

async def main(file_path="./data/hiphop.txt"):
    print(file_path)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())