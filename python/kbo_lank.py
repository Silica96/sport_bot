import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo"

# Fetching the webpage
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the team rankings
table = soup.find("table", {"class": "tEx"})

table_body = soup.find("tbody", {"id": "regularTeamRecordList_table"})
rows = table_body.find_all("tr")

team_scores = {}

for row in rows:
    columns = row.find_all("td")
    rank = row.th.text.strip()
    team_name = columns[0].text.strip()
    games_played = columns[1].text.strip()
    wins = columns[2].text.strip()
    losses = columns[3].text.strip()
    draws = columns[4].text.strip()
    win_rate = columns[5].text.strip()
    game_difference = columns[6].text.strip()
    streak = columns[7].text.strip()
    obp = columns[8].text.strip()
    slg = columns[9].text.strip()
    last_ten = columns[10].text.strip()

    team_scores[team_name] = {
        "Rank": rank,
        "Games Played": games_played,
        "Wins": wins,
        "Losses": losses,
        "Draws": draws,
        "Win Rate": win_rate,
        "Game Difference": game_difference,
        "Streak": streak,
        "OBP": obp,
        "SLG": slg,
        "Last 10 Games": last_ten,
    }

# 결과 출력
for team, data in team_scores.items():
    print(f"Team: {team}")
    for key, value in data.items():
        print(f"{key}: {value}")
    print()
