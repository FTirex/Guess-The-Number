import random 
class player :      #Define Player Class
    def __init__(self):
        self.name = input("Nickname\n")
        self.score = 0 
        self.times = 5
        self.choice = int(input("Your Choice\n"))

    def play (self): 
        key = random.randint(0,4)
        print('Pc Choose :',key)
        for i in range(self.times):
            if (self.choice != key):
                print("Sadge Your Are Wrong")
                print("Try Again")
                self.choice = int(input("Your Choice\n"))
            elif (self.choice == key):
                print("GG WP")
                print(f"you guess it in {i+1} Time ")   #we add +1 to i cz our i start from 0 so the counter stop in 4 not 5 to make it realistic to simple user we add +1 
                break
            

player1 = player()      #create an object named player1
player1.play()          #we called play Function to our Player1  
