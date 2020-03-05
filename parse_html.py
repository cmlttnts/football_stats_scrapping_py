from bs4 import BeautifulSoup

teams_tr = {"BTCTürkYeniMalatyaspor" : "malatya", \
"DemirGrupSivasspor": "sivas", \
"YukatelDenizlispor": "denizli",\
"Fenerbahçe": "fenerbahce",\
"Galatasaray": "galatasaray",\
"Göztepe": "goztepe",\
"İttifakHoldingKonyaspor": "konya",\
"Kasımpaşa" : "kasimpasa",\
"Gençlerbirliği" :"gencler",\
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

teams_ger = { "HerthaBSCBerlin" : "hberlin", \
"FortunaDüsseldorf": "dusseldorf", \
"BayernMünih": "bmunih", \
"TSG1899Hoffenheim": "hoffenheim", \
"BayerLeverkusen": "leverkusen", \
"WerderBremen": "bremen", \
"UnionBerlin": "uberlin",\
"Mainz05": "mainz", \
"FCKöln": "koln", \
"Freiburg": "freiburg", \
"RBLeipzig": "leipzig", \
"Schalke04": "schalke", \
"BorussiaDortmund": "dortmund", \
"VflWolfsburg": "wolfsburg", \
"Augsburg": "augsburg", \
"M'gladbach": "mgladbach", \
"EintrachtFrankfurt": "frankfurt", \
"Paderborn07": "paderborn"}

teams_eng = { "Everton" : "everton", \
"WestHamUnited": "westham", \
"AFCBournemouth": "bournemouth", \
"NorwichCity": "norwich", \
"AstonVilla": "aston", \
"Brighton&HoveAlbion": "brighton", \
"Chelsea": "chelsea",\
"NewcastleUnited": "newcastle", \
"LeicesterCity": "leicester", \
"Burnley": "burnley", \
"TottenhamHotspur": "tottenham", \
"Watford": "watford", \
"Wolverhampton": "wolves", \
"Southampton": "southampton", \
"CrystalPalace": "palace", \
"ManchesterCity": "mancity", \
"ManchesterUnited": "manutd", \
"Liverpool": "liverpool",\
"SheffieldUnited": "sheffield",\
"Arsenal" : "arsenal"}

teams_ita = { "Juventus" : "juventus", \
"Lazio": "lazio", \
"Atalanta": "atalanta", \
"Napoli": "napoli", \
"HellasVerona": "hellas", \
"Bologna": "bologna", \
"Sassuolo": "sassuolo",\
"Inter": "inter", \
"Cagliari": "cagliari", \
"Spal": "spal", \
"Sampdoria": "sampdoria", \
"Roma": "roma", \
"Udinese": "udinese", \
"Torino": "torino", \
"Parma": "parma", \
"Genoa": "genoa", \
"Milan": "milan", \
"Lecce": "lecce",\
"Brescia": "brescia",\
"Fiorentina" : "fiorentina"}

teams_sp = { "Granada" : "granada", \
"Osasuna": "osasuna", \
"Eibar": "eibar", \
"Barcelona": "barcelona", \
"AtleticoMadrid": "atmadrid", \
"Valencia": "valencia", \
"Getafe": "getafe",\
"Leganes": "leganes", \
"Mallorca": "mallorca", \
"RealMadrid": "rmadrid", \
"DeportivoAlaves": "alaves", \
"CeltaVigo": "celta", \
"RealSociedad": "sociedad", \
"RealBetis": "betis", \
"Espanyol": "espanyol", \
"Villarreal": "villarreal", \
"AthleticBilbao": "bilbao", \
"RealValladolid": "valladolid",\
"Sevilla": "sevilla",\
"Levante" : "levante"}


lig_name_change_list = [teams_tr, teams_ger, teams_eng, teams_ita, teams_sp]
league_names =["tr", "ger", "eng", "ita", "sp"] 


def parseHtml(html_list, lig_no):
  for raw_html in html_list:
    if raw_html is not None:
      html = BeautifulSoup(raw_html, 'html.parser')
      weeks = html.find_all('div', {"class" : "singleRound"})
      for week in weeks:
        week_header = week.find("div",{"class": "roundHeader"})
        file_name = "matches/"+league_names[lig_no]+ week_header.text.rstrip().lstrip().replace(" ", "")+".txt"
        import os.path
        if os.path.exists(file_name):
          first_match = False
        else:
          first_match = True
        with open(file_name, "a+", encoding='utf8') as file:
          matches = week.find_all('div', {"class": "fixtureMatch_football"})
          for match in matches:
            if first_match:
              file.write("Date "+ match.find("div", {"class": "date"}).text.rstrip().lstrip().replace(" ", "") + "\n")    
              first_match = False
            home_team = match.find("div", {"class": "homeTeam"})
            away_team = match.find("div", {"class": "awayTeam"})
            ms_res = match.find("div", {"class": "score"})
            fh_res = match.find("div", {"class": "halfTimeScore"})
            prety_home_name = lig_name_change_list[lig_no][home_team.text.rstrip().lstrip().replace(" ", "")]
            prety_away_name = lig_name_change_list[lig_no][away_team.text.rstrip().lstrip().replace(" ", "")]
            file.write(prety_home_name + " "+prety_away_name  + " " + fh_res.text.rstrip().lstrip().replace("-", " ")+ " "+ ms_res.text.rstrip().lstrip().replace("-", " ")+ "\n")
