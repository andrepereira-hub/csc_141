# Andre Pereira
# Chapter 8
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

print(make_album("Artist One", "Album A"))
print(make_album("Artist Two", "Album B"))
print(make_album("Artist Three", "Album C", 12))