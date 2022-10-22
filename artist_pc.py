import numpy as np
import mutagen
import os


def get_artist(path_file):
    audio : dict = mutagen.File(path_file, easy=True)
    l = []
    if "TPE1" in audio.keys():
        l_audio = audio["TPE1"].text
    else:
        l_audio = audio["artist"]
    for art in l_audio:
        d = {"artist" : art.upper(),
            "info" : str(l_audio)}
        l.append(d)
    return l

def look_musique_in_dir(directory):
    l_artist = []
    try:
        l_musique = os.listdir(directory)
    except NotADirectoryError:
        pass
        return []
    
    for musique in l_musique:
        path_tot = directory +"/"+ musique
        try:
            l_artist.extend(get_artist(path_tot))
        except Exception as e:
            e = str(e)
            if "directory" in e:
                l_artist.extend(look_musique_in_dir(path_tot))
            else:
                e = str(e)
                if "NoneType" not in e and "jpg" not in e and ".log" not in e and ".cue" not in e and "nfo" not in e:
                    print("error %s %s"%(e, path_tot))
    return l_artist

def get_my_artists(directory, l_artist_to_forget = ["JAMES", "JOYCE", "CHRISTOPHE", "LE COMTE", "LE LIVRE DE LA JUNGLE", "BLACK M"] ):
    l_artist = look_musique_in_dir(directory)
    mask = np.unique([d["artist"] for d in l_artist], return_index=True)
    l_artist = [l_artist[i] for i in mask[1]]
    for artist_to_forget in l_artist_to_forget:
        l  = [d["artist"] for d in l_artist]
        if artist_to_forget in l:
            index_pop = l.index(artist_to_forget)
            print(l_artist.pop(index_pop))
    return l_artist
