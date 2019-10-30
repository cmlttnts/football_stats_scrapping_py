

#ağustos
tr_xpath1 = '//*[@id="mainFixtureResultPage"]/div[2]/div[1]/div[1]/div[1]'
ger_xpath1 = '//*[@id="fixtureStageListViewDataContent"]/div/div[1]/div[1]'
eng_xpath1 = '//*[@id="mainFixtureResultPage"]/div[2]/div[1]/div[1]/div[1]'
ita_xpath1 = '//*[@id="mainFixtureResultPage"]/div[2]/div[1]/div[1]/div[1]'
sp_xpath1 = '//*[@id="mainFixtureResultPage"]/div[2]/div[1]/div[1]/div[1]'
#eylül
tr_xpath2 = '//*[@id="mainFixtureResultPage"]/div[2]/div[1]/div[1]/div[3]'
ger_xpath2 = '//*[@id="fixtureStageListViewDataContent"]/div/div[1]/div[3]'
eng_xpath2 = '//*[@id="mainFixtureResultPage"]/div[2]/div[1]/div[1]/div[3]'
ita_xpath2 = '//*[@id="mainFixtureResultPage"]/div[2]/div[1]/div[1]/div[3]'
sp_xpath2 = '//*[@id="mainFixtureResultPage"]/div[2]/div[1]/div[1]/div[3]'
#ekim
tr_xpath3 = '//*[@id="mainFixtureResultPage"]/div[2]/div[1]/div[1]/div[5]'
ger_xpath3 ='//*[@id="fixtureStageListViewDataContent"]/div/div[1]/div[5]' 
eng_xpath3 = '//*[@id="mainFixtureResultPage"]/div[2]/div[1]/div[1]/div[5]'
ita_xpath3 = '//*[@id="mainFixtureResultPage"]/div[2]/div[1]/div[1]/div[5]'
sp_xpath3 = '//*[@id="mainFixtureResultPage"]/div[2]/div[1]/div[1]/div[5]'

#kasım
tr_xpath4 = '//*[@id="mainFixtureResultPage"]/div[2]/div[1]/div[1]/div[7]'
ger_xpath4 = '//*[@id="fixtureStageListViewDataContent"]/div/div[1]/div[7]'
eng_xpath4 = '//*[@id="mainFixtureResultPage"]/div[2]/div[1]/div[1]/div[7]'
ita_xpath4 = '//*[@id="mainFixtureResultPage"]/div[2]/div[1]/div[1]/div[7]'
sp_xpath4 = '//*[@id="mainFixtureResultPage"]/div[2]/div[1]/div[1]/div[7]'

tr_xpaths = [tr_xpath4] #[tr_xpath1, tr_xpath2, tr_xpath3]
ger_xpaths = [ger_xpath4]#[ger_xpath1, ger_xpath2, ger_xpath3]
eng_xpaths = [eng_xpath4]#[eng_xpath1, eng_xpath2, eng_xpath3]
ita_xpaths = [ita_xpath4]#[ita_xpath1, ita_xpath2, ita_xpath3]
sp_xpaths = [sp_xpath4]#[sp_xpath1, sp_xpath2, sp_xpath3]

all_xpaths = [tr_xpaths, ger_xpaths, eng_xpaths, ita_xpaths, sp_xpaths]
raw_htmls = []
tr_url = "http://istatistik.nesine.com/FixtureResult/Index.aspx?sportId=1&countryId=12&tournamentId=1&languageId=1"
ger_url = "http://istatistik.nesine.com/FixtureResult/Index.aspx?sportId=1&countryId=3&tournamentId=5&languageId=1"
eng_url = "http://istatistik.nesine.com/FixtureResult/Index.aspx?sportId=1&countryId=2&tournamentId=2&languageId=1"
ita_url = "http://istatistik.nesine.com/FixtureResult/Index.aspx?sportId=1&countryId=4&tournamentId=6&languageId=1"
sp_url = "http://istatistik.nesine.com/FixtureResult/Index.aspx?sportId=1&countryId=8&tournamentId=7&languageId=1"
all_urls = [tr_url, ger_url, eng_url, ita_url, sp_url]


