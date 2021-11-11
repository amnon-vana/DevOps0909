def welcome(name):
    print("Hello %s and welcome to the World of Game(WoG)." % (name))
    print("Here you can find many cool games to play.")


def load_game():
    res = 0
    while int(res) not in range(1, 4):
        print("Please choose a game to play")
        print("\t1. Memory game - a sequence of numbers will apears for 1 second ahd you have to guess it back.")
        print("\t2. Guess game - guess a number and see if you chose like the computer.")
        print("\t3. Currency Roulette - try and guess the value of a random ampunt of USD in ILS.")
        res = input("Your choice is: ")
        if not res.isnumeric():
            res = 0
    res = 0
    while int(res) not in range(1, 5):
        res = input("Please choose game difficulty from 1 to 5: ")
        if not res.isnumeric():
            res = 0
