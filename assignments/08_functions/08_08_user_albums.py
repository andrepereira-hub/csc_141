# Andre Pereira
# Chapter 8
def make_album(artist, title):
    return {"artist": artist, "title": title}

while True:
    artist = input("Enter artist (or 'q' to quit): ")
    if artist == 'q':
        break
    title = input("Enter album title (or 'q' to quit): ")
    if title == 'q':
        break
    print(make_album(artist, title))