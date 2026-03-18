import requests
from datetime import datetime
from team_utils import translate_team_name


def fetch_kbo_team_stats_single_line():
    year = datetime.now().year
    url = f"https://api-gw.sports.naver.com/statistics/categories/kbo/seasons/{year}/teams"
    response = requests.get(url)
    data = response.json()

    result_string = ""
    for team in data["result"]["seasonTeamStats"]:
        name = translate_team_name(team["teamName"])
        wins = team["winGameCount"]
        draws = team["drawnGameCount"]
        losses = team["loseGameCount"]
        game_behind = team["gameBehind"]
        result_string += f" {name} ({wins}승, {draws}무, {losses}패, {game_behind})\n"

    return result_string


def translate_team_name(team_name):

    if team_name == "LG":
        return "🖤서울의 자존심 LG 트윈스❤️"

    return team_name
