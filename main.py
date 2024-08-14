import os
import csv
import platform

def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():
    print("eSports League Manager")
    print("----------------------")
    print("[1] Add a new team")
    print("[2] Manage teams")
    print("[3] Input match results")
    print("[4] Display league table")
    print("[5] Exit")
    print("----------------------")
    option = input("> 1")
    if option == "1":
        add_team()
    elif option == "2":
        manage_teams()
    elif option == "3":
        input_match_results()
    elif option == "4":
        display_league_table()
    elif option == "5":
        exit()
    else:
        print("Invalid option")
        main()

def add_team():
    clear_terminal()
    print("eSports League Manager")
    print("----------------------")
    name = input("Enter new team name > ")
    email = input("Enter team contact email > ")
    team_lead = input("Enter team lead name > ")

    # add team to csv file for use later
    with open('teams.csv', mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, team_lead])

    print(f"Welcome to the competition, {team_lead}!")



main()