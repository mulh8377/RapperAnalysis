import urllib.request
import argparse
import concurrent.futures
import asyncio

import rapquery as rq
import rapfile as rf

def read_hiphop_txt(file_path):
    print(file_path)

async def check_artist_presence(update: int):
    if update:
        print("update artist page")
    else:
        print("do nothing here.")

async def download_artist_page(url: str, name: str, dir="./data/html/"):
    tag = dir + name + ".html"
    urllib.request.urlretrieve(url, tag)
    return tag

async def download_artist_songs():
    pass

async def download_artist_picture():
    pass

async def main(file_path="./data/hiphop.txt"):
    #read_hiphop_txt(file_path)
    tag = await download_artist_page(url="https://www.lyricsmania.com/lizzo_lyrics.html", name="Lizzo")
    print(tag)
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())