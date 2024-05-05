import requests
from bs4 import BeautifulSoup


def fetch_kfootball_team_stats():
    url = "https://sports.news.naver.com/kfootball/record/index"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    table_body = soup.find("tbody", {"id": "regularGroup_table"})
    rows = table_body.find_all("tr")

    team_scores = {}

    for i, row in enumerate(rows):
        cells = row.find_all("td")

        if len(cells) >= 11:  # 열의 수가 충분한지 확인
            rank = row.find("th").text.strip()
            team_name = cells[0].text.strip()
            games_played = cells[1].text.strip()
            points = cells[2].text.strip()
            wins = cells[3].text.strip()
            draws = cells[4].text.strip()
            losses = cells[5].text.strip()
            goals_for = cells[6].text.strip()
            goals_against = cells[7].text.strip()
            goal_difference = cells[8].text.strip()
            fouls = cells[10].text.strip()  # 파울 수

            team_scores[team_name] = (
                f"{team_name} (승점: {points}, {wins}승, {draws}무, {losses}패)"
            )

    # 결과를 문자열로 정리하여 반환
    result_string = ""
    for team, data in team_scores.items():
        result_string += f"{data}\n"

    return result_string


# 함수 호출 및 출력 결과 확인
kfootball_stats = fetch_kfootball_team_stats()
print(kfootball_stats)

