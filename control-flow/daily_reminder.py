# daily_reminder.py

while True:
    task = input("Enter your task:").strip()
    if task:
        break
    print("Task cannot be empty. Please enter a valid task.")

while True:
    priority = input("Priority (high/medium/low):").strip().lower()
    if priority in ("high", "medium", "low"):
        break
    print("Please enter 'high', 'medium', or 'low' for priority.")

while True:
    time_bound = input("Is it time-bound? (yes/no):").strip().lower()
    if time_bound in ("yes", "no"):
        break
    print("Please enter 'yes' or 'no'.")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that should be done today.")
        else:
            print(f"\nNote: '{task}' is a medium priority task. Plan to do it soon.")
    case "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a low priority task, but it needs to be done today.")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
