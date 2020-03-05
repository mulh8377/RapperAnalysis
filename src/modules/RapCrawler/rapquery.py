def target_file():
    return ".html"
def target_domain():
    return "https://lyricsmania.com/"
def artist_query(name):
    return target_domain() + str.lower(name) + "_lyrics" + target_file()

if __name__ == "__main__":
    print(artist_query("Lizzo"))