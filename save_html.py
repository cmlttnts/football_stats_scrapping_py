url = "http://istatistik.nesine.com/FixtureResult/Index.aspx?sportId=1&countryId=12&tournamentId=1&languageId=1"
import urllib.request, urllib.error, urllib.parse

response = urllib.request.urlopen(url)
webContent = response.read()

f = open('test.html', 'w')
f.write(webContent)
f.close