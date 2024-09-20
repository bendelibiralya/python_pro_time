import random
import time
from speechrecog import speech_eng  

kolay = ["dairy", "mouse", "computer"]


orta = ["programming", "algorithm", "developer"]


zor = ["neural network", "machine learning", "artificial intelligence"]


seviye = input("Hangi seviyede oynamak istersin? kolay/orta/zor ")

def play_game(level):
    
    if level == "kolay":
        word = random.choice(kolay)
    elif level == "orta":
        word = random.choice(orta)
    elif level == "zor":
        word = random.choice(zor)
        
    print(word)
    time.sleep(1)
    print("get ready!")
    time.sleep(1)
    print("and...")
    time.sleep(1)
    print("go!")

    result = speech_eng()
    print(result)
    time.sleep(1)
    if result.lower() == word.lower():
        print("correct yayy")
    else:
        print("try again :(")
      
play_game(seviye)