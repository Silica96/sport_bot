import requests, json
from datetime import date

def get_volleyball():
    URL = "https://api-gw.sports.naver.com/schedule/games?fields=basic,superCategoryId,categoryName,stadium,statusNum,gameOnAir,hasVideo,title,specialMatchInfo,roundCode,seriesOutcome,seriesGameNo,round,groupName&superCategoryId=volleyball&fromDate="+date.today().strftime('%Y-%m-%d')+"&toDate="+date.today().strftime('%Y-%m-%d')+"&size=500"
    # URL = "https://api-gw.sports.naver.com/schedule/games?fields=basic,superCategoryId,categoryName,stadium,statusNum,gameOnAir,hasVideo,title,specialMatchInfo,roundCode,seriesOutcome,seriesGameNo,round,groupName&superCategoryId=volleyball&fromDate=2023-10-15&toDate=2023-10-15&size=500"

    print(URL)
    page = requests.get(URL)

    score_json = json.loads(page.text)
    home_team_list = []
    away_team_list = []
    home_team_score = []
    away_team_score = []
    game_status = []
    if score_json['code'] != 400:
        for score in score_json['result']["games"]:
            if score['categoryName'] == "배구기타":
                pass
            else:
                home_team_list.append(score['homeTeamName'])
                away_team_list.append(score['awayTeamName'])
                home_team_score.append(str(score['homeTeamScore']))
                away_team_score.append(str(score['awayTeamScore']))
                game_status.append(score['statusInfo'])

        l = []
        total = 0
        while total < len(home_team_list):
            l.append(game_status[total] + "    " + home_team_list[total] + " " + home_team_score[total]+" : "+ away_team_score[total] + " "+ away_team_list[total] )
            total += 1
        msg = "\n".join(l)
        return msg
    else:
        msg = '오늘 게임이 없습니다.'
        return msg
    
print(get_volleyball())