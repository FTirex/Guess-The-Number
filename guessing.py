import random 
class player :      #Define Player Class
    def __init__(self):
        self.name = str(input("Nickname\n"))
        print(f"{'*'*5} Welcome {self.name} {'*'*5}\n")
        self.score = 0 
        self.times = 5
        self.level = 1

    def levelup(self): #It gets harder as the level goes up
        if self.level > 1:
            guess_limit = 4**self.level
            return guess_limit
        else:
            return 4

    def play(self): 
        while True:
            guess_limit = self.levelup()
            key = random.randint(1,guess_limit)
            print(f"{'*'*5} Current Level: {self.level}, Guess Limit: {guess_limit} {'*'*5}\n")
            try:
                choice = int(input("Your Choice\n"))
                for i in range(1,self.times+1):
                    if (choice != key):
                        print("Sadge You Are Wrong")
                        print("Try Again")
                        choice = int(input("Your Choice\n"))
                    else:
                        print("GG WP")
                        print(f"You guessed it in {i} tries !\n")  #we add +1 to i cz our i start from 0 so the counter stop in 4 not 5 to make it realistic to simple user we add +1 
                        self.level += 1
                        break
            except KeyboardInterrupt:
                print(f"Your final level is {self.level} !")
                break

player1 = player()      #create an object named player1

player1.play()          #we called play Function to our Player1  
    