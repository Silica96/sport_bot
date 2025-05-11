from typing import Dict

def translate_team_name(team_name: str) -> str:
    translations: Dict[str, str] = {
        "LG": "🖤서울의 자존심 LG 트윈스❤️",
        "서울": "🖤절대강자축구지존FC서울❤️",
    }
    return translations.get(team_name, team_name)
