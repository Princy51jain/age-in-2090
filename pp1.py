# practice problem 1--------------age in 2090

name = input("Enter your name: ")
y_o_b = int(input("Enter your year of birth: "))
curr_year = int(input("Enter the current year: "))
if len(str(y_o_b)) == 4:

    if y_o_b <= 1900:
        print("You seem to be the oldest person alive !!")
        print(f"Your current age is {curr_year - y_o_b}")

    elif y_o_b > 2023:
        print("You are not yet born")

    else:
        print(f"Your current age is {curr_year - y_o_b}")

    year = int(input("Enter the year in which you want to see your age: "))
    if year > 2023:
        print(f"Your age in year {year} will be {year - y_o_b}")

    elif year < 2023:
        print(f"Your age in year {year} was {year - y_o_b}")

    else:
        print(f"Your current age is {year - y_o_b}")

    if year != 2090:
        print(f" Also --> your age in the year 2090 will be {2090 - y_o_b}")

else:
    print("Please check your year of birth!!")
