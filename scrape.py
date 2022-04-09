import requests
from bs4 import BeautifulSoup

URL = "https://www.vlr.gg/77797/xset-vs-cloud9-champions-tour-north-america-stage-1-challengers-lr3"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
header = soup.find(class_ = "match-header-vs")

teamHeader = soup.findAll(class_ = "wf-title-med")
team1 = teamHeader[0].text.strip()
team2 = teamHeader[1].text.strip()

scoreHeader = soup.find(class_ = "js-spoiler").contents
team1Score = scoreHeader[1].text.strip()
team2Score = scoreHeader[5].text.strip()

print(team1, team1Score + ":" + team2Score, team2)
