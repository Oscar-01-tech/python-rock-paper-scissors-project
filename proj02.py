#OSCAR ALVAREZ PROJECT 2: ROCK PAPER SCISSORS
import random  # This add the element of randomness to the program.

rules = {  # This determines which weapon beats which.
  ('scissors', 'scissors'): 'Tie',
  ('scissors', 'paper'): 'Scissors wins!',
  ('scissors', 'rock'): 'Rock wins!',
  ('paper', 'paper'): 'Tie',
  ('paper', 'rock'): 'Paper wins!',
  ('paper', 'scissors'): 'Scissors wins!',
  ('rock', 'rock'): 'Tie',
  ('rock', 'paper'): 'Paper wins!',
  ('rock', 'scissors'): 'Rock wins!'
}

humans_rocks = 0  # These will initialize all of the counters for the final stats at 0.
humans_papers = 0
humans_scissors = 0
humans_wins = 0
computers_wins = 0
ties = 0

while True:   # This loop begins the game that will end when the user quits.
  humanweapon = input("Press R/r for rock, P/p for paper, S/s for scissors, or Q/q to quit: ").lower() #This insures that the input will be recognized as lowercase no matter what case it is.

  if humanweapon in ['q', 'quit']: #This controls what happens when this player chooses to quit.
    print('Game over!')  #When the player quits the following two line will print
    break   #this will break the loop and end the game.

  if humanweapon not in ['r', 'p', 's']:
    print("Your input is invalid. Please re-enter your input again.")  # This will cause the program to reprompt for a correct input
  else:  # If the input is valid
   #The follwing adds the user's input to the weapon counters
    if humanweapon == 'r':  
      humanweapon = 'rock'   #If the user enter's rock this will be added to the rock stats.
      humans_rocks += 1
    elif humanweapon == 'p':
      humanweapon = 'paper'   #If the user enter's paper this will be added to the paper stats.
      humans_papers += 1
    else:
      humanweapon = 'scissors'   #If none of the previous conditions are met, the input will be added to the scissor's stats.
      humans_scissors += 1

    computerweapon = random.choice(['rock', 'paper', 'scissors']) #This allows the computer to choose it's own weapon randomly.

    print("Player chooses " + humanweapon + " this round")  #These announce who won this round.
    print("Computer chooses " + computerweapon + " this round")

    #This determines the results of the game
    if (humanweapon, computerweapon) in rules:
      result = rules[(humanweapon, computerweapon)]
    else:
      result = rules[(computerweapon, humanweapon)]

    print(result)
   
    if result == 'Tie':   # Updates the score and announces the winner of the round.
      print("It's a tie!")   #If the round is a tie this will add the number 1 to the counter counting ties
      ties += 1
    elif (humanweapon, computerweapon) in rules and rules[(humanweapon, computerweapon)].startswith(humanweapon.capitalize()):
      print("Player wins!!!")  #Check's if the player's choice wins the round by seeing if this is a possible combination that exists in the rules and then capitilizes it to match the outcomes in the rules. If it does, this makes the program say the player won and then add the number 1 to the counter recording the player's wins.
      humans_wins += 1
    else:
      print("Computer wins!!!")  #If none of the above conditions are met the program will record this round a a win for the computer and add the number 1 to the counter recording computer wins.
      computers_wins += 1


print('Thanks for playing!')    #Final results that will be printed after the game ends.
print('Final Score:')
print("Total Computer Wins: " + str(computers_wins))
print("Total Player Wins: " + str(humans_wins))
print("Total Ties: " + str(ties))
print("Player's Weapon Choices:")
print("Player used rock " + str(humans_rocks) + " times this series.")
print("Player used paper " + str(humans_papers) + " times this series.")
print("Player used scissors " + str(humans_scissors) + " times this series.")