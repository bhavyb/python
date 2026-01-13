from datetime import datetime
import time

def current_datetime():
    print("\nCurrent Date and Time:", datetime.now().strftime("%Y-%m-%d "
                                                             "%H:%M:%S"))
    print("==============================")


def date_difference():
    d1 = input("Enter the first date (YYYY-MM-DD): ")
    d2 = input("Enter the second date (YYYY-MM-DD): ")
    diff = abs((datetime.strptime(d1, "%Y-%m-%d") - datetime.strptime(d2, "%Y-%m-%d")).days)
    print("Difference:", diff, "days")
    print("==============================")


def format_date():
    print(datetime.now().strftime("%d-%m-%Y %I:%M %p"))
    print("==============================")


def stopwatch():
    input("Press Enter to Start...")
    start = time.time()
    input("Press Enter to Stop...")
    end = time.time()
    print("Elapsed Time:", round(time.time() - start, 2),"second")
    print("==============================")


def countdown():
    sec = int(input("Enter the seconds: "))
    while sec:
        print(sec)
        time.sleep(1)
        sec -= 1
    print("Time's Up!")
    print("==============================")


def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display Current Date and Time")
        print("2. Calculate Difference between two dates")
        print("3. Format Date")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("6. Back to Main menu")

        ch = input("Enter your choice: ")
        if ch == "1":
            current_datetime()
        elif ch == "2":
            date_difference()
        elif ch == "3":
            format_date()
        elif ch == "4":
            stopwatch()
        elif ch == "5":
            countdown()
        elif ch == "6":
            break