from bs4 import BeautifulSoup
import requests

def get_baseball():
    URL = "https://www.koreabaseball.com/Schedule/ScoreBoard.aspx"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    r_score = []
    l_score = []
    l_team = []
    r_team = []
    flag = []

    left_team_all = soup.find(id="cphContents_cphContents_cphContents_udpRecord").find_all("p", class_="leftTeam")
    right_team_all = soup.find(id="cphContents_cphContents_cphContents_udpRecord").find_all("p", class_="rightTeam")
    flag_all = soup.find_all("strong",class_="flag")

    for l in left_team_all:
        l_score.append(l.find("em", class_="score").text)
        l_team.append(l.find("strong", class_="teamT").text)
    
    for f in flag_all:
        flag.append(f.text)

    for r in right_team_all:
        r_score.append(r.find("em", class_="score").text)
        r_team.append(r.find("strong", class_="teamT").text)

    l = []
    total = 0
    while total < len(flag):
        l.append(flag[total] + "    " + l_team[total] + " " + str(l_score[total])+" : "+ str(r_score[total])  + " "+ r_team[total] )
        total += 1
    if len(l) == 0:
        msg = "오늘 경기가 없습니다"
    else:
        msg = "\n".join(l)
    return msg
