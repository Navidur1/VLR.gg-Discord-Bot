import requests
from bs4 import BeautifulSoup

URL = "https://www.vlr.gg/77797/xset-vs-cloud9-champions-tour-north-america-stage-1-challengers-lr3"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
header = soup.find(class_="match-header-vs")

team_header = soup.findAll(class_="wf-title-med")
team1 = team_header[0].text.strip()
team2 = team_header[1].text.strip()

score_header = soup.find(class_="js-spoiler").contents
team1Score = score_header[1].text.strip()
team2Score = score_header[5].text.strip()

print(team1, team1Score + ":" + team2Score, team2)
