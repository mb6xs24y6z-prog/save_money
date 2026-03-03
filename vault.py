import csv
import sys


def main():
    filename = "save_money.csv"
    

    print(f"""1. To insert coin
2. To view saved money.""")
    ques = input("Press 1 or 2: ")
    if ques == "1":
        write_to_csv(filename)
    elif ques == "2":
        total = total_coins_save(filename)
        print(f"You have: {total} coins in your vault.")


def get_input():
    return input_err_handler("Insert Coins: ")


def write_to_csv(filename):
    while True:
        try:
            with open(filename, "a") as file:
                coins = get_input()
                writer = csv.DictWriter(file, fieldnames=["coins"])
                writer.writerow({"coins": coins})
        except KeyboardInterrupt:
            sys.exit()


def total_coins_save(filename):
    """ Show how much money the user has saved """
    total_coins = 0
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_coins += float(row["coins"])
    return total_coins


def input_err_handler(prompt, data_type=float):
    available_coins = [0.5, 1, 2, 5, 10]
    while True:
        try:
            coins = data_type(input(prompt))
            if not coins in available_coins:
                print(f"Valid coins are: {available_coins}")
            elif coins in available_coins:
                print(f"Inserted {coins} coins.")
                return coins
        except ValueError:
            continue


if __name__ == "__main__":
    main()
