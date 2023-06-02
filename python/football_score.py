# https://sports.news.naver.com/kfootball/schedule/scoreboard?year=2023&month=06&category=kleague&date=20230603
import requests, json
from datetime import date

def get_football():
    URL = "https://sports.news.naver.com/kfootball/schedule/scoreboard?year="+date.today().strftime('%Y')+"&month="+date.today().strftime('%m')+"&category=kleague&date="+date.today().strftime('%Y%m%d')
    # URL = "https://sports.news.naver.com/kfootball/schedule/scoreboard?year=2023&month=06&category=kleague&date=20230603"

    print(URL)
    page = requests.get(URL)

    score_json = json.loads(page.text)
    home_team_list = []
    away_team_list = []
    home_team_score = []
    away_team_score = []
    game_status = []
    if len(score_json['scoreboardList']) > 0:
        for score in score_json['scoreboardList']:
            home_team_list.append(score['homeTeamName'])
            away_team_list.append(score['awayTeamName'])
            home_team_score.append(str(score['homeTeamScore']))
            away_team_score.append(str(score['awayTeamScore']))
            game_status.append(score['gameStatus'])

        l = []
        total = 0
        while total < len(score_json['scoreboardList']):
            l.append(game_status[total] + "    " + home_team_list[total] + " " + home_team_score[total]+" : "+ away_team_score[total] + " "+ away_team_list[total] )
            total += 1
        msg = "\n".join(l)
        return msg
    else:
        msg = '오늘 게임이 없습니다.'
        return msg