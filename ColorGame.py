
import random
from colorama import Fore

def menu():
    print('--------------')
    print('Color Game')
    print('--------------')

def color_game():

    score = 0
    colors_fore = [Fore.BLACK,Fore.RED,Fore.CYAN,Fore.GREEN,Fore.WHITE,Fore.YELLOW]
    colors_word = ['black','red','blue','green','white','yellow']
  
    input_user = 0
    random_color = 0

    while( input_user==random_color ):

        random_color= random.choice(colors_fore)
        random_color_word = random.choice(colors_word).upper()

        print(random_color + random_color_word )

        if(random_color==Fore.BLACK):random_color = 'black'
        elif(random_color==Fore.RED):random_color = 'red'
        elif(random_color==Fore.GREEN):random_color = 'green'
        elif(random_color==Fore.WHITE):random_color = 'white'
        elif(random_color==Fore.YELLOW):random_color = 'yellow'
        elif(random_color==Fore.CYAN):random_color = 'blue'
        
        
        input_user = input(Fore.WHITE).lower()

        random.shuffle(colors_fore)
        random.shuffle(colors_word)
        print(Fore.WHITE +'--+----+--')
        if(input_user==random_color):score = score + 1

    print(Fore.WHITE + f'Score : {score}')



def main():
    menu()
    color_game()
main()