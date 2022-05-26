steps_goal = 10000

sum_steps = 0
while sum_steps <= steps_goal:
    command = input()
    if command == "Going home":
        steps_home = int(input())
        sum_steps += steps_home
        break

    current_steps = int(command)
    sum_steps += current_steps


diff = abs(sum_steps - steps_goal)
if sum_steps >= steps_goal:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")