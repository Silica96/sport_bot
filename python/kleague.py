import requests
from datetime import datetime
from team_utils import translate_team_name


def fetch_kfootball_team_stats():
    year = datetime.now().year
    url = f"https://api-gw.sports.naver.com/statistics/categories/kleague/seasons/{year}/teams"
    response = requests.get(url)
    data = response.json()

    result_string = ""
    for team in data["result"]["seasonTeamStats"]:
        name = translate_team_name(team["teamName"])
        points = team["points"]
        wins = team["wins"]
        draws = team["draws"]
        losses = team["losses"]
        result_string += f"{name} (승점: {points}, {wins}승, {draws}무, {losses}패)\n"

    return result_string


# 함수 호출 및 출력 결과 확인
kfootball_stats = fetch_kfootball_team_stats()
print(kfootball_stats)

