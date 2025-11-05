# NAME: Heena Chhoker
# DATE : 2 November 2025
# PROJECT TITLE : Daily Calorie Tracker 



print(" Welcome to the Daily Calorie Tracker!")
print("This tool helps you log your meals and monitor your daily calorie intake.")

Meals = []
Calories = []

meal_count = int(input("How many meals would you like to enter today ? "))

for i in range(meal_count):
    print(f"\nMeal {i+1} :")
    meal_name = input("Enter the meal name (e.g. Breakfast , Lunch) :")
    calorie_amount = float(input("Enter the Calorie amount: "))

    Meals.append(meal_name)
    Calories.append(calorie_amount)

print("\n Meal and Calorie Data Recorded Successfully!")
print("Here’s what you entered:")

# Display collected data
for i in range(meal_count):
    print(f"{Meals[i]} — {Calories[i]} calories")


total_calories = sum(Calories)
average_calories = total_calories / meal_count

# Display calculations
print("\n Calorie Summary:")
print(f"Total Calorie Intake: {total_calories} calories")
print(f"Average Calories per Meal: {average_calories:.2f} calories")

# Ask user for their daily calorie limit
daily_limit = float(input("\nEnter your daily calorie limit: "))


if total_calories > daily_limit:
    print("You have exceeded your daily calorie limit! Try to eat lighter next time.")
elif total_calories == daily_limit:
    print(" Perfect! You’ve exactly met your daily calorie goal.")
else:
    remaining = daily_limit - total_calories
    print(f" Great job! You are {remaining:.2f} calories under your daily limit.")

# --- Task 5: Neatly Formatted Output ---

print("\n-----------------------------")
print("  Daily Calorie Summary Report")
print("-----------------------------")
print(f"{'Meal Name':<15}{'Calories'}")
print("-" * 28)

# Print each meal and calorie neatly
for i in range(meal_count):
    print(f"{Meals[i]:<15}{Calories[i]:>7.0f}")

# Print total and average neatly
print("-" * 28)
print(f"{'Total:':<15}{total_calories:>7.0f}")
print(f"{'Average:':<15}{average_calories:>7.2f}")
print("-----------------------------")



# --- Task 6 (Bonus): Save Session Log to File ---
import datetime

save_choice = input("\nWould you like to save this session to a file? (yes/no): ").strip().lower()

if save_choice in ['yes', 'y']:
    # Create a timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open a file to write session data
    with open("calorie_log.txt", "w") as file:
        file.write("----- Daily Calorie Tracker Log -----\n")
        file.write(f"Timestamp: {timestamp}\n\n")
        file.write(f"{'Meal Name':<15}{'Calories'}\n")
        file.write("-" * 28 + "\n")

        # Write all meal entries
        for i in range(meal_count):
            file.write(f"{Meals[i]:<15}{Calories[i]:>7.0f}\n")

        # Write total and average
        file.write("-" * 28 + "\n")
        file.write(f"{'Total:':<15}{total_calories:>7.0f}\n")
        file.write(f"{'Average:':<15}{average_calories:>7.2f}\n\n")

        # Write daily limit status
        file.write(f"Daily Calorie Limit: {daily_limit}\n")
        if total_calories > daily_limit:
            file.write("Status: Exceeded daily limit \n")
        elif total_calories == daily_limit:
            file.write("Status: Met daily limit \n")
        else:
            remaining = daily_limit - total_calories
            file.write(f"Status: {remaining:.2f} calories under limit \n")

        file.write("------------------------------------\n")

    print("\n Session saved successfully as 'calorie_log.txt'.")
else:
    print("\n Session not saved.")



    # -------END OF PROGRAM------

