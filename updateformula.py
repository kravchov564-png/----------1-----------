def analyze_results(data):
    # Получите названия всех команд и отсортируйте их по алфавиту.
    first_dict = data[0]
    teams = first_dict.keys()
    teams = sorted(teams)

    print('Команды, участвовавшие в чемпионате:')
    for team in teams:
        print(f'{team}')
        # Выведите названия команд:
        #print(team[0])
        #print(team[1])
        #print(team[2])
        #print(team[3])

    scores = {}
    for race in data:
        for team_name, score in race.items():
            if team_name in scores:
                scores[team_name] += score
            else:
                scores[team_name] = score

    winner_team = None
    winner_score = 0
    for team_name, score in scores.items():
        if score > winner_score:
            winner_score = score
            winner_team = team_name

    print('В чемпионате победила команда', winner_team, 'с результатом', winner_score, 'баллов')


races_data = [
    {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
    {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
    {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
]

analyze_results(races_data)