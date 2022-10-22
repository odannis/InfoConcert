import requests
from bs4 import BeautifulSoup


def get_date(panel):
    a = ""
    for tag in panel.find(class_="date").find_all("span"):
        a += tag.contents[0] + " " 
    return a

def find_artist_web_page(departement=13, max_page=20):

    l_event = []
    for id_page in range(1, max_page+1):
        url = "https://www.infoconcert.com/concerts/concerts-par-departement-%s.html?departement_id=%s"%(id_page, departement)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        panels = soup.find_all(class_="panel-body")
        for panel in panels:
            d_info = {}
            try:
                d_info["city"] = panel.find(class_="ville-dpt").find("span").contents[0]
                d_info["salle"] = panel.find(class_="salle").find("span").contents[0]
                d_info["date"] = get_date(panel)
            except:
                pass
            l = panel.find_all(class_='spectacle')
            for div in l:
                tags = div.find_all('a')
                name_artist = ""
                for tag in tags:
                    for artist in tag.contents:
                        name_artist += artist + " "
                    name_artist = name_artist + "/ "
                d_info_art = d_info.copy()
                d_info_art["artist"] = name_artist[:-1]
                l_event.append(d_info_art)
    return l_event

