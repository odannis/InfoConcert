import requests
import time
import tqdm


def artists_from_out(out: list):
    l_artist = []
    for l_info in out["songs"]:
        d = {
            "artist" : l_info["firstLine"],
            "info" : l_info["secondLine"] + " of " + l_info["firstLine"] 
        }
        l_artist.append(d)
    return l_artist

def artists_from_fip(l_web_radio=["fip", "fip_rock", "fip_nouveautes", "fip_electro", "fip_groove", "fip_jazz"]):
    l_art = []
    for web_radio in tqdm.tqdm(l_web_radio):
        print("webradio %s"%web_radio)
        timestamp = int(time.time() - 10*24*60*60)
        url = "https://www.radiofrance.fr/api/v1.9/stations/fip/webradios/%s/songs?timestamp=%s"%(web_radio, timestamp)

        re = requests.get(url=url)
        out = re.json()
        l_art.extend(artists_from_out(out))

        while True:
            if out["next"] is None:
                break
            url = "https://www.radiofrance.fr/api/v1.9/stations/fip/webradios/%s/songs?pageCursor=%s&timestamp=%s"%(web_radio, out["next"], timestamp)
            re = requests.get(url=url)
            out = re.json()
            l_art.extend(artists_from_out(out))
        
    return l_art


