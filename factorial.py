#!usr/bin/env python3
# Created By: Marli Peters
# Date: Nov. 17, 2023
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the factorial
# of all numbers from 0 to that number.


def main():
    loop_counter = 0
    factorial_answer = 1

    user_number_str = str(input("Enter a positive number: "))
    print("")

    while True:
        try:
            user_number_int = int(user_number_str)
            if user_number_int < 0:
                print("Please enter a positive number.")
            else:
                user_number_int = int(user_number_str)
                loop_counter = loop_counter + 1
                factorial_answer = factorial_answer * loop_counter
                print("Tracking {} times through loop.".format(loop_counter))
        except:
            print("Please enter a positive number.")

        try:
            user_number_int = int(user_number_str)
            if loop_counter >= user_number_int:
                break
        except:
            break
    try:
        user_number_int = int(user_number_str)
        if user_number_int >= 0:
            print("")
            print("{}! = {}".format(user_number_str, factorial_answer))
    except:
        pass


if __name__ == "__main__":
    main()
