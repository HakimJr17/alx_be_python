from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Save current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Formats date/time
    print("Current date and time:", formatted_date)

def calculate_future_date():
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))  # Prompts the user for input
    except ValueError:
        print("Error: Please enter a valid integer.")
        return
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)  # Calculates the future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))  # Prints future date in YYYY-MM-DD format

# Run the functions
display_current_datetime()
calculate_future_date()



# This script displays the current date and time, prompts the user for a number of days,
# and calculates the future date by adding the specified number of days to the current date.

def main():
    display_current_datetime()
    calculate_future_date()
if __name__ == "__main__":
    main()