# Python E-Sports

## Description

A Python CLI E-Sports League table for a FPS game

## Instructions

An eSports league hosts a competition to find the best player at a popular first person shooting game. The event is being hosted in a large stadium and there will be prizes awarded for the best individual player and the most successful team.
You have been asked to create the command line program that manages the event, it will need to include team registration, and recording the results of each individual round.

At the start of the even teams can sign up where they will need to provide their team name and contact details.

During the event there will be 5 different rounds, at the end of each round each participant has their kills and deaths count entered into the system, which will calculate a KD Ratio to represent their success at each round (*a bigger KD ratio is better*). This information should be stored to a text file so that if the program is terminated during the run of the competition it does not cause the results to be lost.

The KD ratio is simply `kills / deaths` and should be stored as a `float` rounded to 2DP.

The table below is an example of the information that should be stored during the competition:

|         Name        |       Team      | Round Number | Kills | Deaths | KD Ratio |
|:-------------------:|:---------------:|:------------:|:-----:|:------:|----------|
|     James Jones     |   Death Eaters  |       1      |   14  |    2   | 7.0      |
|    Kara Kettering   | Golden Sparkles |       1      |   42  |   12   | 3.5      |
|     Lauren Leon     |   Death Eaters  |       1      |   21  |    4   | 5.25     |
| Mario Michaelangelo | Golden Sparkles |       1      |   39  |   20   | 1.95     |

The competition program should have the ability to delete every record for a certain player or team, if they have been disqualified.

At then end of the competition the winning player is selected by identifying the player who scored the highest KD ratio in any round. The winning team is calculated by working out the average KD ratio for every player, for every round, and the team with the highest average KD ratio wins.

Task
You have been asked to develop a command line program that is able to manage the eSports competition as above, making sure that you have:

* Created an effective user interface using menus
* Have the ability to add and store teams
* Have the ability to add each player's result at the end of each round
* Validate data sensibly to prevent garbage data entry
* Calculate the KD ratio for each data entry automatically, and store this with the other data
* Store the results in a text file after each entry
* Have a method to display all results, and filter by team, player or round
* Include the ability to delete all results from individuals or teams if they have cheated
* Have an option to identify the winning player
* Have an option to identify the winning team
![image](https://github.com/user-attachments/assets/e1e262f7-4dbe-4e55-9f77-cfe412865c2c)

