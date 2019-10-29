import requests as req
from bs4 import BeautifulSoup
import time
import urllib3.request
from contextlib import closing


def resp_okay(response):
  content_type = response.headers['Content-Type'].lower()
  return (response.status_code == 200 and content_type is not None and content_type.find('html') > -1)

def get_safe(url):
  content = None
  with closing(req.get(url, stream=True)) as response:
    if resp_okay(response):
      # response.encoding = 'utf-8'
      content = response.content
  return content

teams_tr = {"BTCTürkYeniMalatyaspor" : "malatya", \
            "DemirGrupSivasspor": "sivas", \
            "YukatelDenizlispor": "denizli",\
            "Fenerbahçe": "fenerbahce",\
            "Galatasaray": "galatasaray",\
            "Göztepe": "goztepe",\
            "İttifakHoldingKonyaspor": "konya",\
            "Kasımpaşa" : "kasimpasa",\
            "Gençlerbirliği" :"genclerbirligi",\
            "MKEAnkaragücü" : "ankaragucu",\
            "AytemizAlanyaspor": "alanya",\
            "DGSivasspor" :"sivas",\
            "Trabzonspor": "trabzon",\
            "GaziantepFK" : "gaziantep",\
            "MedipolBaşakşehir": "basaksehir",\
            "Antalyaspor": "antalya",\
            "İstikbalMobilyaKayserispor": "kayseri",\
            "Beşiktaş" : "besiktas",\
            "ÇaykurRizespor": "rize"}

url = "http://istatistik.nesine.com/FixtureResult/Index.aspx?sportId=1&countryId=12&tournamentId=1&languageId=1"
raw_html = get_safe(url)
if raw_html is not None:
  html = BeautifulSoup(raw_html, 'html.parser')
  matches = html.find_all('div', {"class": "fixtureMatch_football"})
  i = 0
  for match in matches:
    home_team = match.find("div", {"class": "homeTeam"})
    away_team = match.find("div", {"class": "awayTeam"})
    ms_res = match.find("div", {"class": "score"})
    fh_res = match.find("div", {"class": "halfTimeScore"})
    prety_home_name = teams_tr[home_team.text.rstrip().lstrip().replace(" ", "")]
    prety_away_name = teams_tr[away_team.text.rstrip().lstrip().replace(" ", "")]
    print(prety_home_name + " "+prety_away_name  + " " + fh_res.text.rstrip().lstrip().replace("-", " ")+ " "+ ms_res.text.rstrip().lstrip().replace("-", " "))

