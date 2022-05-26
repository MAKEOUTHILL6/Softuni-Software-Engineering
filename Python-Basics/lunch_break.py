from math import ceil

serial_name = input()
episode_duration = int(input())
break_time = int(input())

time_for_lunch = break_time // 1/8
time_for_chilling = break_time // 1/4
time_left = break_time - time_for_lunch - time_for_chilling
diff = abs(time_left - episode_duration)

if time_left <= episode_duration:
    print(f''' You don't have enough time to watch {serial_name}, you need {ceil(diff)} more minutes.''')
else:
    print( f'You have enough time to watch {serial_name} and left with {ceil(diff)} minutes free time.')

