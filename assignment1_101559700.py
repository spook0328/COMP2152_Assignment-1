#Author: <Jui Hsin Wong>
#Assignment: #1 
gym_member = "Alex Alliton" #string
preferred_weight_kg = 20.5 #float
highest_reps = 25 # int
membership_active = True #bool

# dict[str, tuple[int, int, int]]
workout_starts = {
    "John": (50, 50, 10),
    "Jane": (50, 50, 20),
    "Doe" : (50, 50, 50)
}
for name, minutes in list(workout_starts.items()):
    total = sum(minutes)
    workout_starts[f"{name}_Total"] = total
print(workout_starts)

# list[list[int]]
workout_list = [
    list(minutes)
    for name, minutes in workout_starts.items()
    if "_Total" not in name
]
print(workout_list)

yoga_run = [row[:2] for row in workout_list]
print("Yoga and running :",yoga_run)

weight_lasttwo = [row[2] for row in workout_list[-2:]]
print("Weight last two person :",weight_lasttwo)

for name, minutes in workout_starts.items():
    if "_Total" in name and minutes >= 120:
        fname = name.replace("_Total", "")
        print (f"Great job staying active, {fname}!")

        name_input  = input ("Enter a friend's name: ")
if name_input in workout_starts:
    yoga,run,weight = workout_starts[name_input]
    total = workout_starts[f"{name_input}_Total"]
    
    print(f"{name_input}: ")
    print(f" Yoga: {yoga} min")
    print(f" Run: {run} min")
    print(f" Weight: {weight} min")
    print(f" Total: {total} min")
else:
    print(f"Friend {name_input} not found in the records.")

    min = __builtins__["min"]
totals = {
    name : value
    for name, value in workout_starts.items()
    if "_Total" in name}

highest = max(totals, key=totals.get)
lowest  = min(totals, key=totals.get)

highest_name = highest.replace("_Total", "")
lowest_name  = lowest.replace("_Total", "")

print(f"Highest total workout minutes: {highest_name} ({totals[highest]} min)")
print(f"Lowest total workout minutes:  {lowest_name} ({totals[lowest]} min)")