import random

rock = '''
    ___
---'   __)
      (___)
      (___)
      (__)
---._(__)
'''

paper = '''
    ___
---'   _)_
          __)
          ___)
         ___)
---.____)
'''

scissors = '''
    ___
---'   _)_
          __)
       ____)
      (__)
---._(__)
'''


you = int(input("Enter for rock 0 paper 1 scissors 2."))

computer = random.randrange(0, 3)

if (you == 0):
  print("rock")
  print(rock)
elif (you == 1):
  print("paper")
  print(paper)
else:
  print("scissors")
  print(scissors)

if (computer == 0):
  print("rock")
  print(rock)
elif (computer == 1):
  print("paper")
  print(paper)
else:
  print("scissors")
  print(scissors)

if ((you == 0) and (computer == 2)):
  print("You Win")
elif ((you == 2) and (computer == 1)):
  print("You Win")
elif ((you == 1) and (computer == 0)):
  print("You Win")
else:
  if ((you == 0) and (computer == 0)):
    print("You Draw")
  elif ((you == 1) and (computer == 1)):
    print("You Draw")
  elif ((you == 2) and (computer == 2)):
    print("You Draw")
  else:
    print("You loss")