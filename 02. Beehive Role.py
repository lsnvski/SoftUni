iq = int(input())
power = int(input())
sex = input()

if iq >= 80 and power >= 80 and sex == "female":
    print("Queen Bee")
elif iq >= 80:
    print("Repairing Bee")
elif iq >= 60:
    print("Cleaning Bee")
elif power >= 80 and sex == "male":
    print("Drone Bee")
elif power >= 60:
    print("Guard Bee")
else:
    print("Worker Bee")