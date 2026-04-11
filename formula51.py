def analyze_results(data):
    # Получите названия всех команд и отсортируйте их по алфавиту.
    first_dict = data[0]
    team = first_dict.keys()
    team = sorted(team)
    print('Команды, участвовавшие в чемпионате:')
    # Выведите названия команд:
    print(team[0])
    print(team[1])
    print(team[2])
    print(team[3])
    # * А
    # * Б
    # * В


races_data = [
    {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
    {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
    {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
]

analyze_results(races_data)