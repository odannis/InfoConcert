import artist_fip as fip
import artist_pc as pc
import artist_web as web
import telegram_send
import argparse
import os


def test_name(artist, art):
    if artist in art:
        l_name = art.split()
        l_artist = artist.split()
        for name in l_name:
            if len(name)>3:
                for artist_sub in l_artist:
                    
                    if name == artist_sub:
                        return True
    return False

def artist_in_my_l(artist : str, l_artist : list[str]):
    artist = artist.upper()
    for d_art in l_artist:
        art = d_art["artist"]
        art = art.upper()
        if test_name(artist, art) or test_name(art, artist):
            print("artist web %s found in my artist %s"%(artist, art))
            return True, d_art["info"]
    return False, None

def good_events(l_web_artist, l_artist):
    l = []
    for dict_event in l_web_artist:
        artist = dict_event["artist"]
        if len(artist) > 3:
            test, name_arti = artist_in_my_l(artist, l_artist)
            if test:
                dict_event["my_artist"] = name_arti
                l.append(dict_event)
    return l

def nice_message(d):
    msg = ""
    for dd in d:
        msg += dd["date"] + ":\n    " + dd["my_artist"] + " in " + dd["artist"][:-2]  + " in " + dd["salle"] + "\n"
    return msg

def parse_arguments():
    parser = argparse.ArgumentParser(description="Give your the next concerts in your departement filter with your artists")
    parser.add_argument('--path', type=str, default=None, help="If none try to guess it, else path music file : '/home/andonis/Musique'")
    parser.add_argument('--departement', type=int, default=13, help="Departement concert (Tours 37)")
    parser.add_argument('--maxpage', type=int, default=15, help="Nombre de page web d'InfoConcert")
    parser.add_argument("--fip", action="store_true", help="Use fip webradio instead of my local music")
    parser.add_argument("--telegram", action="store_true", help="Send message with telegram (NEED TO CONFIGURE it before)")
    parser.parse_args()
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_arguments()
    print(args)
    if args.fip:
        l_artist = fip.artists_from_fip()
        print(l_artist)
    else:
        if args.path is None:
            args.path = os.path.expanduser("~") + "/Musique"
        print("Your musique Path used is %s"%args.path)
        l_artist = pc.get_my_artists(args.path)
    l_web_artist = web.find_artist_web_page(departement=args.departement, max_page=args.maxpage)
    d  = good_events(l_web_artist, l_artist)
    print(nice_message(d))
    if args.telegram:
        telegram_send.send(messages=[nice_message(d)])


