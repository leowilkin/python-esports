import csv
import os
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
    option = input("> ")
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

    # Add team to CSV file for use later
    with open('teams.csv', mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, team_lead])

    print(f"Welcome to the competition, {team_lead}!")
    main()

def manage_teams():
    teams = load_teams()
    if not teams:
        print("404. No teams found!")
        main()

    while True:
        clear_terminal()
        print("eSports League Manager")
        print("----------------------")
        display_teams(teams)

        choice = input("Select a team by number > ").strip().lower()

        if choice == 'q':
            main()
        elif choice.isdigit() and 1 <= int(choice) <= len(teams):
            team_index = int(choice) - 1  # Corrected index calculation
            print(f"Selected team: {teams[team_index][0]}")
            action = input("Do you want to (m)odify or (d)elete this team? > ").strip().lower()
            if action == 'm':
                modify_team(teams, team_index)
                save_teams(teams)
            elif action == 'd':
                delete_team(teams, team_index)
                save_teams(teams)
            else:
                print("Invalid option. Returning to team list.")
        else:
            print("Invalid option, please try again.")

def load_teams():
    teams = []
    try:
        with open('teams.csv', mode='r') as file:
            reader = csv.reader(file)
            teams = list(reader)
    except FileNotFoundError:
        print("404. The file is missing")
    return teams

def modify_team(teams, team_index):
    team = teams[team_index]
    print(f"Modifying {team[0]}:")
    new_name = input(f"Enter new team name [{team[0]}] > ") or team[0]
    new_email = input(f"Enter new team email [{team[1]}] > ") or team[1]
    new_team_lead = input(f"Enter new team lead name [{team[2]}] > ") or team[2]
    
    teams[team_index] = [new_name, new_email, new_team_lead]
    print("Team details updated successfully!")

def delete_team(teams, team_index):
    print(f"Deleting {teams[team_index][0]}...")
    del teams[team_index]
    print("Team successfully deleted.")

def save_teams(teams):
    with open('teams.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(teams)

def display_teams(teams):
    print("Teams:")
    for idx, team in enumerate(teams, start=1):
        print(f"[{idx}] {team[0]} (Email: {team[1]}, Lead: {team[2]})")
    print("\nPress 'q' to quit.")

main()
