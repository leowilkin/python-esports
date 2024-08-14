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
    print("[5] Identify winning player")
    print("[6] Identify winning team")
    print("[7] Delete player or team results")
    print("[8] Exit")
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
        identify_winning_player()
    elif option == "6":
        identify_winning_team()
    elif option == "7":
        delete_player_or_team()
    elif option == "8":
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
            team_index = int(choice) - 1
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

def input_match_results():
    clear_terminal()
    print("Input Match Results")
    print("-------------------")
    name = input("Enter player name > ")
    team = input("Enter team name > ")
    round_number = input("Enter round number > ")
    kills = int(input("Enter number of kills > "))
    deaths = int(input("Enter number of deaths > "))
    
    kd_ratio = round(kills / deaths, 2) if deaths != 0 else float('inf')

    with open('results.txt', mode='a') as file:
        file.write(f"{name},{team},{round_number},{kills},{deaths},{kd_ratio}\n")

    print(f"Results recorded for {name} (KD Ratio: {kd_ratio})")
    main()

def display_league_table():
    clear_terminal()
    print("League Table")
    print("------------")
    print("{:<15} {:<15} {:<15} {:<10} {:<10} {:<10}".format("Name", "Team", "Round", "Kills", "Deaths", "KD Ratio"))

    try:
        with open('results.txt', mode='r') as file:
            for line in file:
                name, team, round_number, kills, deaths, kd_ratio = line.strip().split(',')
                print("{:<15} {:<15} {:<15} {:<10} {:<10} {:<10}".format(name, team, round_number, kills, deaths, kd_ratio))
    except FileNotFoundError:
        print("No results found.")

    input("\nPress Enter to return to the main menu.")
    main()

def identify_winning_player():
    clear_terminal()
    print("Identify Winning Player")
    print("-----------------------")

    max_kd_ratio = -1
    winning_player = ""

    try:
        with open('results.txt', mode='r') as file:
            for line in file:
                name, _, _, _, _, kd_ratio = line.strip().split(',')
                if float(kd_ratio) > max_kd_ratio:
                    max_kd_ratio = float(kd_ratio)
                    winning_player = name

        if winning_player:
            print(f"The winning player is {winning_player} with a KD Ratio of {max_kd_ratio}.")
        else:
            print("No player data found.")
    except FileNotFoundError:
        print("No results found.")

    input("\nPress Enter to return to the main menu.")
    main()

def identify_winning_team():
    clear_terminal()
    print("Identify Winning Team")
    print("---------------------")

    team_kd_ratios = {}

    try:
        with open('results.txt', mode='r') as file:
            for line in file:
                _, team, _, _, _, kd_ratio = line.strip().split(',')
                if team not in team_kd_ratios:
                    team_kd_ratios[team] = []
                team_kd_ratios[team].append(float(kd_ratio))

        if team_kd_ratios:
            winning_team = max(team_kd_ratios, key=lambda t: sum(team_kd_ratios[t]) / len(team_kd_ratios[t]))
            avg_kd_ratio = sum(team_kd_ratios[winning_team]) / len(team_kd_ratios[winning_team])
            print(f"The winning team is {winning_team} with an average KD Ratio of {avg_kd_ratio:.2f}.")
        else:
            print("No team data found.")
    except FileNotFoundError:
        print("No results found.")

    input("\nPress Enter to return to the main menu.")
    main()

def delete_player_or_team():
    clear_terminal()
    print("Delete Player or Team Results")
    print("-----------------------------")
    target = input("Enter the name of the player or team to delete > ")

    try:
        with open('results.txt', mode='r') as file:
            lines = file.readlines()

        with open('results.txt', mode='w') as file:
            for line in lines:
                if target.lower() not in line.lower():
                    file.write(line)

        print(f"All records for '{target}' have been deleted.")
    except FileNotFoundError:
        print("No results found.")

    input("\nPress Enter to return to the main menu.")
    main()

main()
