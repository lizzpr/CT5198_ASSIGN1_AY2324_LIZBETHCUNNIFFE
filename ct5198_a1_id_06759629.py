# Student Name: Lizbeth Cunniffe. ID: 06759629
# This program creates list to store number of customers a business had each day
# it calculates maximum, minimum and average number of customers for week.

# initializes empty list to store number of customers each day
da_cust = []

# uses for loop to input number of customers for each of 7 days
for day in range(1, 8):
    while True:
        try:
            # asks user to enter number of customers for day
            cust = int(input(f"Enter the number of customers on day {day}: "))

            # checks if input is valid number non-negative
            if cust < 0:
                print("The number of customers cannot be negative, please enter valid number.")
            else:
                # adding number of customers for day to list
                da_cust.append(cust)
                break  # Exits loop after valid input
        except ValueError:
            # handling invalid inputs where input is not an integer
            print("Input is invalid, please enter a whole number.")

# calculates maximum, minimum, and average number of customers
max_cust = max(da_cust)
min_cust = min(da_cust)
avg_cust = round(sum(da_cust) / len(da_cust))

# prints results
print(f"\nThe maximum number of customers in a day is: {max_cust}")
print(f"The minimum number of customers in a day is: {min_cust}")
print(f"The average number of customers per day is: {avg_cust}")
