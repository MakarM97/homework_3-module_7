# Использование %:
team1_num = 5
print('В команде Мастера кода участников: %s' % team1_num)
team_1, team_2 = 5, 6
print('Итого сегодня в командах участников: %s и %d' % (team_1, team_2))

# Использование format():
score_2 = 42
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
team2_time = 18015.2
print('Волшебники данных решили задачи за {} c !'.format(team2_time))

# Использование f-строк:
score_1, score_2 = 40, 42
print(f'Команды решили {score_1} и {score_2} задач.')
challenge_result = "Результат битвы: победа команды Мастера кода!"
print(f'{challenge_result}')
tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
team1_time = 350.4 * 40
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(result)