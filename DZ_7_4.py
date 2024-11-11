team1_num = 5
team2_num = 6

score_1 = 40
score_2 = 42

team1_time = 1552.512
team2_time = 2153.31451

tasks_titale = 82
time_avg = 45.2

challenge_result = 'Победа команды Волшебники данных!'

if (score_1 >= score_2) and (team1_time > team2_time):
    result = 'Победа команды Мастера кода!'
        #result = 'Победа команды Мастера кода!’
elif (score_1 <= score_2) and (team1_time < team2_time):
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'


# Используем %:
print('Используем %:')
print('количество участников первой команды %s.' % team1_num)
print('В команде Мастера кода участников: %s %s' % ('5', '!'))
print('количество участников в обоих командах %s %s.' % (team1_num, team2_num))
print('Итого сегодня в командах участников: %d и %d %s.' % (5, 6, '!'))


#Используем format
print()
print('Используем format:')
print('Количество задач решённых командой 2 {}.'.format(score_2))
print('Команда Волшебники данных решала задач:  {} {}.'.format(42, '!'))
print('время за которое команда 2 решила задачи {}'.format(team1_time))
print('Волшебники данных решили задачи за {} {} {}'.format('18015.2', 'c', '!'))


# Используем f-строки
print()
print('Используем f-строки:')
print(f'количество решённых задач по командам {score_1}, {score_2}')
print(f'Команды решили {score_1} и {score_2} задач.')


print(f'Исход соревнования {challenge_result}.')
print(f'Результат битвы: {result}.')
print(f'количество задач {tasks_titale} и среднее время решения {time_avg}.')
print(f'Сегодня было решено {82} задач, в среднем по {350.4} секунды на задачу!.')
