swimming = int(input("Swimming time in minutes: "))
print(swimming)
cycling = int(input("Cycling time in minutes: "))
print(cycling)
running = int(input("Running time in minutes: "))
print(running)
total_time = swimming + cycling + running
print("Total time: ", total_time)
qualifying_time = 100
if total_time <= qualifying_time:
    print("Award: Provincial Colours")
elif total_time > 100 and total_time <= 105:
    print("Award: Provincial Half Colours")
elif total_time > 105 and total_time <= 110:
    print("Award: Provincial Scroll")
else:
    print("No award")
