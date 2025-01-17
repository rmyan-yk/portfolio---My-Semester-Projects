###Project 2: Pokemon Project 
#**Summary**: This program allows users to play as the Pokemon Bulbasaur. Players can train, compete in gym battles, and evolve Bulbasaur into Venusaur
#**Key Features**: 
  #Uses pixel art and print commands to draw the 3 evolutions of Bulbasaur
  #Uses random to determine outcomes of winning or losing gym battles (50% chance)
  #Uses a while loop and a break to repeat the game forever or end it.
  #Makes use of user input to give the player multiple choices


#Initialize
import random
#Global Variables
pokemon_level = 0
pokemon_name = "Bulbasaur"
day = 1
#Drawing Functions to create pixel art for all pokemon
def drawBulbasaur():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠉⢳⠴⢲⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠤⠤⠤⠤⠤⠤⠤⠤⠖⠊⠀⣠⠎⠀⡞⢹⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠊⠁⠀⠀⠀⠀⠀⢀⡠⠤⠄⠀⠀⠀⠁⠀⠀⢀⠀⢸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠤⠤⠄⣀⠀⠀⠀⠀⢀⣌⠀⠀⠀⠀⠀⢀⣠⣆⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠘⡄⠀⠀⠀⠀
⠀⠀⠀⠀⡴⠁⠀⠀⠐⠛⠉⠁⠀⠀⣉⠉⠉⠉⠑⠒⠉⠁⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠱⡀⠀⠀⠀
⠀⠀⠀⢰⣥⠆⠀⠀⠀⣠⣴⣶⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠑⡄⠀⠀
⠀⠀⢀⡜⠁⠀⠀⢀⠀⠻⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠸⡀⠀
⠀⢀⣮⢖⣧⢠⠀⣿⠇⠀⠀⠁⠀⠀⠀⠠⠀⢀⣠⣴⣤⡀⠀⠀⠀⠈⡗⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢱⠀
⠀⣼⠃⣼⣿⠘⠀⠀⠀⢠⣶⣿⡆⠀⠀⠁⣠⠊⣸⣿⣿⣿⡄⠀⠀⠀⡇⠀⢑⣄⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠸⡆
⠀⣿⢰⣿⣿⠀⠀⠀⠀⠙⠻⠿⠁⠀⠀⠠⠁⠀⣿⣿⣿⣿⡇⠀⠀⠀⠇⠀⢻⣿⣷⣦⣀⡀⣀⠠⠋⠀⠀⠀⢀⡇
⠈⠉⠺⠿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⢦⡀⠀⠀⠀⠀⡸⠀
⠘⣟⠦⢀⠀⠀⢠⠀⠀⡠⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠁⣀⠔⠀⠀⠀⠀⠀⠀⠀⠛⠻⠟⠋⠀⠙⢦⠀⣠⠜⠀⠀
⠀⠈⠑⠤⡙⠳⣶⣦⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⡶⠞⠁⠀⠀⣠⠖⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠈⢯⠁⠀⠀⠀
⠀⠀⠀⠀⠈⢳⠤⣙⡻⠿⣿⣿⣿⣿⡿⠿⠛⠉⠀⢀⣀⡤⡚⠁⠀⠀⠀⠀⠀⠀⣧⠖⣁⣤⣦⠀⠀⠈⢇⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠀⢀⣩⣍⠓⠒⣒⠒⠒⠒⠒⠊⠉⠁⢀⡟⠀⠀⣾⣷⠀⠀⠀⠀⠏⢴⣿⣿⣿⠀⠀⠀⢸⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣶⣿⣿⣿⠀⠀⠈⠒⢄⣀⡀⠀⠀⠀⣼⣶⣿⡇⠈⠋⠀⠀⠀⡼⠀⠈⠻⣿⡿⠀⠀⠀⢸⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⡿⠿⠋⠀⠀⠀⠀⡜⠁⠈⢯⡀⢺⣿⣿⣿⠃⠀⠀⠀⢀⣼⣇⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣦⣄⣠⣀⣠⠞⠀⠀⠀⠈⠛⣿⡛⠛⠁⠀⠀⠀⣠⠊⠀⠈⢦⣄⣀⣀⣀⣀⢀⡼⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠉⠀⠀⠀⠀⠀⠀⠘⠛⠿⣿⠷⡾⠗⠊⠁⠀⠀⠀⠈⠉⠙⠛⠛⠛⠉⠀⠀⠀⠀⠀""")

def drawIvysaur():
    print("Ivysaur Picture (could not find 1)")

def drawVenusaur():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⡤⠴⠶⠶⠶⠶⠶⢦⣄⠀⠀⠀⠀⢀⣀⣤⠤⠴⠶⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣋⣁⣀⣀⣀⠀⠀⠀⣀⣴⣤⣾⢷⡾⠛⣾⡿⢻⣤⣤⠀⠀⠀⠀⠈⠉⠛⠶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠖⠚⠋⠉⠉⠉⠉⠉⠉⠉⠉⢉⣛⡳⣿⣿⠿⠙⠷⠟⠷⠋⠻⠾⠻⣿⣷⠶⠖⠒⠒⠒⠒⠒⠻⠿⠦⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠋⠁⠀⠀⠀⠀⢀⣠⣤⡴⠶⠛⠛⠋⠉⠉⠉⠛⠛⠲⢦⣄⠀⠀⢀⣠⣤⠶⠿⠓⠒⠶⠶⠶⠦⣤⣤⣀⡀⠀⠀⠀⠉⠙⠓⠶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠀⠀⠀⠀⣀⣤⣶⠾⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣹⣷⣴⣿⣉⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠳⢦⣄⡀⠀⠀⠀⠈⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⢀⣠⡶⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣄⣀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⡾⠛⠁⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⢦⣌⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠸⣧⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣽⠆⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠦⣤⣀⣀⣤⠀⠀⠀⢠⣾⡃⠀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡼⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣉⣻⠶⣤⣤⣿⣿⣿⣿⣿⣿⣏⢀⣤⡈⣡⣙⣿⣿⣿⣿⣿⣿⣿⣾⣿⣷⣿⡆⠀⣰⣦⣤⣴⠶⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣀⣴⡶⠶⣶⣿⣟⠛⢿⣯⢉⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢻⠷⠓⠲⣶⡤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡿⠷⠄⠈⠉⠛⣀⣠⣽⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣄⣀⠙⠛⠉⠿⠷⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⠛⠓⠚⠛⠂⠀⠀⠰⠶⠛⠛⣻⠏⠉⠹⠿⣿⣿⡛⠛⠻⠿⠿⠿⣿⣉⣤⡴⠞⠀⠀⠀⢸⣿⡇⠀⠀⠀⢀⣀⠉⢻⣿⠿⠛⠛⠛⣛⣽⣿⣿⠃⠉⢿⣿⡿⣏⠛⠻⣶⣶⠾⠛⠻⠷⢤⣄⡀⠀⠀⠀⠀
⠀⢀⣈⣭⠿⠛⠀⠀⠀⠀⣠⡆⠀⠀⠀⠋⣶⠀⠀⢀⣽⣿⣿⣦⣄⠀⠀⠀⢿⣋⣁⣤⣴⠖⠀⠀⢸⣿⠀⠀⠀⠀⠀⠙⠿⣿⡿⠀⠀⣠⣾⣿⣿⣿⣿⣄⠀⠀⠉⠃⠀⠀⠀⢻⣆⠀⠀⠀⠀⢠⣈⡉⠛⠶⣤⡄
⢸⡏⠁⣀⠀⢀⣴⡇⠀⢠⣿⠁⠀⡄⠀⣼⣿⠀⢀⣿⣟⣿⣿⣻⣿⣷⡄⠀⠘⢻⣟⠋⢀⣠⣤⠀⠈⠁⠀⠀⠸⣶⣄⣶⣤⡿⠁⠀⠾⠿⣿⣯⣿⣿⣤⣿⣧⡀⠘⣿⣆⠀⣤⣀⠹⣷⣄⠀⣦⣈⠙⢿⣷⡾⠋⠀
⠘⠛⢿⣏⣴⣿⣏⣀⣠⡟⣿⣤⣼⣷⣶⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠻⠾⣿⡿⢁⡄⠀⠀⠀⢤⣀⠘⣿⠿⠟⠀⢀⣀⣀⡀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⠟⢷⣬⣿⣷⣤⡼⠷⠀⠀
⠀⠀⠀⠀⠁⠀⠉⠉⠉⣴⢏⣿⣿⣿⣿⣿⠟⠛⢻⣿⠟⠀⠀⠀⢴⡛⠉⠁⠀⢀⠀⠀⠻⢶⣿⠃⢀⣿⡄⢈⣿⠟⠋⠀⡀⠀⠀⠀⣉⣽⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠉⠹⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡾⠿⠋⢹⣿⡏⠀⢀⡾⠁⠀⠀⠀⠀⣾⠛⣶⣤⣀⠸⡇⠀⠀⠀⠙⠷⢾⠟⠿⠟⠁⠀⠀⢸⡇⣀⣤⣾⣿⢹⡇⠀⠀⠀⠀⠙⣿⡛⠋⠀⢻⣿⣿⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⠉⠁⠀⠀⢸⡿⠀⠀⢾⡁⠀⠀⠀⠀⠀⠹⣄⠙⠛⣹⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠈⠛⠿⣤⣉⣀⠼⠁⠀⣀⠀⠀⣸⡇⠀⠀⠈⣿⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣟⢀⣀⠀⠀⢸⡇⠀⠀⠘⢷⡀⠀⠲⣦⣀⡀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣴⠾⠋⠀⣰⡟⠀⠀⠀⠀⣿⡏⠀⠀⠀⢀⣸⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣤⣦⣾⡇⠀⠀⠀⠈⠳⢶⣤⣾⣽⣿⣟⣿⣶⡶⠶⢦⣤⣀⠀⢠⡀⠀⠀⠀⣤⠀⣠⣤⡶⠖⠛⢿⣿⣿⣽⠛⣠⣦⣴⠾⠋⠀⠀⠀⠀⠀⣿⠁⠀⢀⣴⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠈⠛⢿⡄⢹⣿⣿⡀⠀⠀⠀⠉⠛⠳⠶⠶⠶⠶⠶⠛⠋⠀⠀⠀⠀⢸⣿⣿⢃⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⣿⣤⣾⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⡻⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⡿⣫⡾⠃⠀⠀⠀⠀⠀⠀⣤⠀⠀⣸⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣟⣿⣿⣿⢿⣿⣧⡺⣧⡄⠀⠀⢀⣀⡀⠉⠻⣮⣝⣿⣿⣿⣤⣤⣀⣀⣀⣀⣀⣀⣀⣤⣴⣿⣿⡿⣫⣾⠛⣁⣄⠀⠀⠀⠀⠀⠛⠋⠀⢠⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠈⠉⠙⠒⠋⠙⢷⣄⠀⠀⠀⠘⠛⠁⠀⠀⣠⣿⡿⢿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣽⡾⠋⠀⠀⠿⠷⠀⠀⠀⠀⠀⠀⠀⣠⡿⠳⠞⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣷⣶⣶⣶⣾⣿⣿⣿⣿⠃⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢉⡟⠀⠀⠀⠀⠀⠀⠀⢰⣤⣶⠆⢀⣴⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠹⢿⣿⡟⢿⣿⣿⣏⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⣹⡆⢢⡾⠻⣧⠀⠀⣴⢶⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠉⠉⠙⠻⣇⣠⡿⠷⠾⣧⣈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")

def evolve(): #Evolves pokemon into next form
    global pokemon_name
    global pokemon_level
    if pokemon_level >= 20:
        pokemon_name = "Venusaur"
        drawVenusaur()
    elif pokemon_level >= 10:
        pokemon_name = "Ivysaur"
        drawIvysaur()
    elif pokemon_level <= 10:
        drawBulbasaur()


def Training(): #Train: increases pokemon level by 1
    global pokemon_level
    global pokemon_name
    pokemon_level = pokemon_level + 1
    print(str(pokemon_name)+" "+"trained his skills")
    print(str(pokemon_name)+" "+"is now level"+" "+str(pokemon_level))


def Gym_Battle(): #increases pokemon level by 2 if pokemon wins, by 0 if it loses.
    global pokemon_name
    global pokemon_level
    outcome = random.randint(1,2) #50% chance to win or lose
    print(str(pokemon_name)+" "+"is going into a gym battle...Goodluck!")
    if outcome == 1:
        print(str(pokemon_name)+" "+"won! You gain 2 levels")
        pokemon_level = pokemon_level + 2
        print(str(pokemon_name)+" "+"is now pokemon level"+" "+str(pokemon_level))
    if outcome == 2:
        print(str(pokemon_name)+" "+"lost!")
        print(str(pokemon_name)+" "+"is still pokemon level"+" "+str(pokemon_level))


def Rest(): #Displays current name of pokemon, it's current level, and an image of the pokemon.
    global pokemon_name
    global pokemon_level
    print(str(pokemon_name)+" "+"(level"+" "+str(pokemon_level)+" "+"pokemon"+")"+" "+"is resting")

#Main
global pokemon_name
global pokemon_level
print("Welcome to Pokemon Evolution! Your pokemon is"+" "+str(pokemon_name))
drawBulbasaur()
while True:
    global day
    print("Day" +" "+str(day))
    print("Select an activity for the day")
    print("""1. Train
    2. Gym Battle
    3. Rest (Display info)
    4. Quit""")
    day = day+1
    activity = int(input("Activity: "))
    if activity == 1:
        Training()
        evolve()
    if activity == 2:
        Gym_Battle()
        evolve()
    if activity == 3:
        Rest()
        evolve()
    if activity == 4:
        print("Ended Game")
        break

