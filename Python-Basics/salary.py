open_tabs = int(input())
salary = int(input())

fine = 0
for tabs in range(open_tabs):
    site_names = input()
    if site_names == "Facebook":
        fine += 150
    elif site_names == "Instagram":
        fine += 100
    elif site_names == "Reddit":
        fine += 50
    else:
        fine += 0
diff = abs(salary - fine)
if fine > salary or salary == 0:
    print("You have lost your salary")
else:
    print(f"{round(diff)}")