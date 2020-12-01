#!/usr/bin/env python3

# Created by: Nicholas Graziano
# Created on: November 2020
# This module calcullates the total between 2 numbers


def main():
    # this function adds 2 numbers together
    # input
    First_Number = int(input("Enter the First_Number):"))
    Second_Number = int(input("Enter the Second_Number:"))

    # process
    total = First_Number + Second_Number

    # output
    print("")
    print("The total between the two numbers is {}"
          .format(total))


if __name__ == "__main__":
    main()
