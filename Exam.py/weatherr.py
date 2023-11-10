temperatures = [
    [22, 24, 19, 21, 25, 23, 20],  # Week 1
    [20, 22, 21, 23, 24, 22, 21],  # Week 2
    [23, 21, 20, 22, 24, 25, 23],  # Week 3
]

#Average
def calculate_weekly_average(week_temperatures):
    # Calculate the average temperature for the week
    average_temperature = sum(week_temperatures) / len(week_temperatures)
    return average_temperature


# Calculate and print the average temperature for each week
for week_index, week_temperatures in enumerate(temperatures, start=1):
    average_temp = calculate_weekly_average(week_temperatures)
    print(f"Week {week_index}: Average Temperature = {average_temp:.2f}")


#hottest day of the week
def find_highest_temperature_day(week_temperatures):
    # Find the index of the maximum temperature in the week
    max_temperature_day = week_temperatures.index(max(week_temperatures)) + 1
    return max_temperature_day


#Identify Consistently Mild Weeks
def is_week_in_range(week_temperatures):
    # Check if all temperatures in the week are between 20 and 25 (inclusive)
    return all(20 <= temp <= 25 for temp in week_temperatures)

for week_index, week_temperatures in enumerate(temperatures, start=1):
    highest_temp_day = find_highest_temperature_day(week_temperatures)
    print(f"Week {week_index}: Day with the Highest Temperature = {highest_temp_day}")


# Find and print the weeks that meet the criterion
weeks_in_range = [week_index + 1 for week_index, week_temperatures in enumerate(temperatures) if is_week_in_range(week_temperatures)]

print("Weeks with temperatures between 20 and 25 (inclusive):", weeks_in_range)

def calculate_temperature_changes(week_temperatures):
    # Initialize the list of temperature changes
    temperature_changes = [week_temperatures[0]]

    # Calculate the temperature change from the previous day to the current day
    for i in range(1, len(week_temperatures)):
        change = week_temperatures[i] - week_temperatures[i - 1]
        temperature_changes.append(change)

    return temperature_changes

# Calculate and print the temperature changes for each week
for week_index, week_temperatures in enumerate(temperatures, start=1):
    temperature_changes = calculate_temperature_changes(week_temperatures)
    print(f"Week {week_index}: Temperature Changes = {temperature_changes}")

#BONUS

def calculate_weekly_average(week_temperatures):
    # Calculate the average temperature for the week
    average_temperature = sum(week_temperatures) / len(week_temperatures)
    return average_temperature

# Calculate historical average temperatures for each week
historical_averages = [calculate_weekly_average(week_temperatures) for week_temperatures in temperatures]

# Print the historical averages
print("Historical Average Temperatures:")
for week_index, average_temp in enumerate(historical_averages, start=1):
    print(f"Week {week_index}: {average_temp:.2f}")

# Compare historical averages with actual temperatures
differences = [[actual - historical for actual, historical in zip(week_temperatures, historical_averages)] for week_temperatures in temperatures]

# Print the differences
print("\nTemperature Differences (Actual - Historical):")
for week_index, difference_list in enumerate(differences, start=1):
    print(f"Week {week_index}: {difference_list}")