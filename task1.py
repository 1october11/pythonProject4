minute = 60
hour = 360
day = 86400
week = 604800
month = 2629743
year = 31556926

duration = int(input('Укажите продолжительность в секундах: '))
if duration <= minute:
    print('{} сек'.format(duration))
elif minute <= duration and hour > duration:
    inputminute = duration // minute
    inputsecond = duration % minute
    print('{} мин {} сек'.format(inputminute,inputsecond));
elif duration >= hour and duration < day:
    inputhour = duration // hour
    duration = duration % hour
    inputminute = duration // minute
    inputsecond = duration % minute
    print('{} час {} мин {} сек'.format(inputhour,inputminute, inputsecond));
elif duration >= day and duration < week:
    inputday = duration // day
    duration = duration % day
    inputhour = duration // hour
    duration = duration % hour
    inputminute = duration // minute
    inputsecond = duration % minute
    print('{} дн {} час {} мин {} сек'.format(inputday, inputhour, inputminute, inputsecond));

