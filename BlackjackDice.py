## CS 101 Problem Solving & Programming
## Program 2
## Christopher J. Neeley
## Date created: Sep 8, 2015
## Date due: Oct 4, 2015
## PROBLEM: 
##      Create a game of Blackjack, with dice
##
## SOLUTION:
##      1. Create loop for repeating the game
##      2. Ask player for money and wager
##      3. Roll the dice for each person, ask player if they want to roll more, then roll more for the dealer
##      4. Print out if they've won or not, total in pot, and if they want to play again
##      5. Create small methods for checks, ending the game, and help
##################################################################################

# Import random for dice, sys for ending the game
import random
import sys
# Set some varaibles before starting
continuePlaying = True
resetEverything = True
maxAmountHadInPot = 0
dealerDiceAmount = 0
playerDiceAmount = 0
roundCount = 0

# Define method for ending the game
def endGame():
  print('Thank you for playing.')
  sys.exit(0)
# Define method for input checking
def intCheck(var):
  try:
    int(var)
    return True
  except ValueError:
    return False
# Define method for the help option, color for better readability
def help():
  print('\033[34m(At any point you may press: help or h for help, quit or q to quit, capitalization does not matter)')
  print("""Blackjack Dice is a simple game. 
      Each person starts off by rolling two dice, the player then continues to roll a single dice until they go over 21 and bust or they choose to stop. 
      The dealer then rolls until he busts or he reaches higher than the player without going over 21. 
      If it is a tie, then no one wins.\033[30m""")

# Name the Game
print('\033[35mWelcome to Blackjack Dice\033[30m')
print('')

# Began game loop
while continuePlaying:
  # Start and reset of game
  if resetEverything:
    amountInPot = 0
    # Make sure amount in pot is eligible
    while amountInPot <= 0:
      # Get amount of money in pot
      amountInPot = raw_input('Enter the amount of money you want in chips. ==> $')
      # Check if input is int or not
      if intCheck(amountInPot):
        amountInPot = int(amountInPot)
        # Check if the number is over 0
        if amountInPot <= 0:
          print('\033[31mThe amount must be greater than 0.\033[30m')
      # If not a int
      elif not intCheck(amountInPot):
        # Help ignore capitalization
        amountInPot = amountInPot.lower()
        # Quit the game
        if amountInPot == 'quit' or amountInPot == 'q':
          endGame()
        # Print help information
        elif amountInPot == 'help' or amountInPot == 'h':
          help()
          amountInPot = 0
        # Make sure they know only numbers, without decimals
        else:
          print('\033[31mThe amount must be a number greater than 0. Flat numbers only.\033[30m')
          amountInPot = 0
    resetEverything = False

    maxAmountHadInPot = amountInPot
  # Set some values
  wagerAmount = 0
  dealerContinueRolling = True
  playerContinueRolling = True
  # Make sure wager amount is eligible
  while wagerAmount <= 0 or wagerAmount > amountInPot:
    # Get amount they want to wager
    wagerAmount = raw_input('Enter the amount you want to wager. ==> $')
    # Check if input is a int
    if intCheck(wagerAmount):
      wagerAmount = int(wagerAmount)
      # Wager needs to be more than 0
      if wagerAmount <= 0:
        print('\033[31mThe wager must be greater than 0.\033[30m')
      # But less than the amount in the pot
      elif wagerAmount > amountInPot:
        print('\033[31mThe wager cannot be greater than the amount you have in the pot.\033[30m')
    # If not an int
    elif not intCheck(wagerAmount):
      # Help ignore capitalization
      wagerAmount = wagerAmount.lower()
      # Quit the game
      if wagerAmount == 'quit' or wagerAmount == 'q':
        endGame()
      # Print help information
      elif wagerAmount == 'help' or wagerAmount == 'h':
        help()
        wagerAmount = 0
      # Make sure they know only numbers, without decimals
      else:
        print('\033[31mThe amount must be greater than 0. Flat numbers only.\033[30m')

  # Roll dices for dealer
  diceRollOne = random.randint(1, 6)
  diceRollTwo = random.randint(1, 6)
  # Put amount in the dealers current number
  dealerDiceAmount = diceRollOne + diceRollTwo
  # Print numbers for dealer
  print 'Dealer rolled a %i and a %i for a total of %i.' % (diceRollOne, diceRollTwo, dealerDiceAmount)
  # Roll dices for the player
  diceRollOne = random.randint(1, 6)
  diceRollTwo = random.randint(1, 6)
  # Put amount in the players current number
  playerDiceAmount = diceRollOne + diceRollTwo
  # Print numbers for player
  print 'You rolled a %i and a %i for a total of %i.' % (diceRollOne, diceRollTwo, playerDiceAmount)
  # Loop for player continuing to roll the dice
  while playerContinueRolling:
    # Ask player if they want to continue to roll the dice
    doesPlayerWantToKeepRolling = raw_input('Do you want to roll again? (Y,YES,N,NO) ==> ')
    # Check if input is eligible
    if not intCheck(doesPlayerWantToKeepRolling):
      # Stop rolling player dice
      if doesPlayerWantToKeepRolling == 'n' or doesPlayerWantToKeepRolling == 'no':
        playerContinueRolling = False
        print 'You stayed on %i.' % (playerDiceAmount)
      # Continue rolling player dice
      elif doesPlayerWantToKeepRolling == 'y' or doesPlayerWantToKeepRolling == 'yes':
        diceRollOne = random.randint(1, 6)
        playerDiceAmount += diceRollOne
        # Print out roll
        print 'You rolled a %i for a total of %i.' % (diceRollOne, playerDiceAmount)
      # Quit the game
      elif doesPlayerWantToKeepRolling == 'q' or doesPlayerWantToKeepRolling == 'quit':
        endGame()
      # Print help information
      elif doesPlayerWantToKeepRolling == 'h' or doesPlayerWantToKeepRolling == 'help':
        help()
    # Check to see if the player busts or not, say how much they lost
    if playerDiceAmount > 21:
      print """You busted, I'm so sorry

The dealer won this round, you've lost your $%i wager.""" % (wagerAmount)
      # Skip rolling for dealer and subtract wager from pot
      playerContinueRolling = False
      dealerContinueRolling = False
      amountInPot -= wagerAmount
  # Start rolling for dealer if player did not bust
  if not playerContinueRolling:
    while dealerContinueRolling:
      # Roll for dealer
      diceRollOne = random.randint(1, 6)
      dealerDiceAmount += diceRollOne
      print 'The dealer rolled a %i, for a total of %i.' % (diceRollOne, dealerDiceAmount)
      # Checks to see if the dealer busts
      if dealerDiceAmount > 21:
        print 'Congratulations, you won $%i.' % (wagerAmount)
        dealerContinueRolling = False
        amountInPot += wagerAmount
        playerDiceAmount = 0
        dealerDiceAmount = 0
        wagerAmount = 0
      # Checks to see if the dealer hits 21 then compares to player
      elif dealerDiceAmount == 21:
        # It's a tie if both are 21
        if playerDiceAmount == 21:
          print('You have both tied, no one wins.')
          dealerContinueRolling = False
          playerDiceAmount = 0
          dealerDiceAmount = 0
          wagerAmount = 0
        # If dealer is higher than player, player loses
        else:
          print 'The dealer won this round, you have lost your $%i wager.' % (wagerAmount)
          dealerContinueRolling = False
          playerDiceAmount = 0
          dealerDiceAmount = 0
      # Check if the dealer beats the player
      elif dealerDiceAmount > playerDiceAmount:
        print 'The dealer won this round, you have lost your $%i wager.' % (wagerAmount)
        dealerContinueRolling = False
        playerDiceAmount = 0
        dealerDiceAmount = 0
  # Set max amount ever had in the pot
  if amountInPot > maxAmountHadInPot:
    maxAmountHadInPot = amountInPot
  # Count rounds
  roundCount += 1
  # Show amount in pot
  print 'You now have $%i in the pot.' % (amountInPot)
  # Check if player is broke
  if amountInPot <= 0:
    # Print that they are broke, print number of rounds and highest amount in pot
    print('You ran out of money.')
    print 'You played %i rounds. Your highest pot was %i' % (roundCount, maxAmountHadInPot)
    playAgain = ''
    # Ask the player if they want to play again
    while not playAgain == 'y' and not playAgain == 'yes' and not playAgain == 'n' and not playAgain == 'no':
      # Get player input
      playAgain = raw_input('Do you want to play again? (Y,YES,N,NO) ==> ')
      # Check if input is acceptable
      if not intCheck(playAgain):
        playAgain = playAgain.lower()
        # Quit the game
        if playAgain == 'n' or playAgain == 'no':
          endGame()
        # Restart the game
        elif playAgain == 'y' or playAgain == 'yes':
          resetEverything = True
          roundCount = 0
          maxAmountHadInPot = 0
        # Print help information
        elif playAgain == 'h' or playAgain == 'help':
          help()
        # Quit game
        elif playAgain == 'q' or playAgain == 'quit':
          endGame()
