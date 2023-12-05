import random
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
players = []
#List to store player objects
class Player:
    # Initialize Player with a name, scores for different categories, turn count, and Yahtzee bonus count
    def __init__(self, name):
        self.name = name
         # Dictionary to hold scores for different categories
        self.scores = {
            "Ones": None,
            "Twos": None,
            "Threes": None,
            "Fours": None, 
            "Fives": None,
            "Sixes": None,
            "ThreeOfAKind": None,
            "FourOfAKind": None,
            "FullHouse": None,
            "SmallStraight": None,
            "LargeStraight": None,
            "Chance": None,
            "Yahtzee": None
        }
       
        self.turncount = 0
        self.yahtzee_bonus_count = 0
        # Methods to set scores for different categories and calculate total scores
    def set_score(self, category, score):
        # Set the score for a specific category
        self.scores[category] = score

    def calculate_upper_section_total(self):
        upper_section_categories = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]
        self.total_upper_section = sum(self.scores[cat] for cat in upper_section_categories if self.scores[cat] is not None)
        if self.total_upper_section >= 63:
            self.upper_section_bonus = 35
        else:
            self.upper_section_bonus = 0

    def calculate_total_lower_section(self):
        lower_section_categories = ["ThreeOfAKind", "FourOfAKind", "FullHouse", "SmallStraight", "LargeStraight", "Yahtzee", "Chance"]
        self.total_lower_section = sum(self.scores[cat] for cat in lower_section_categories if self.scores[cat] is not None)

    def calculate_grand_total(self):
        self.calculate_upper_section_total()
        self.calculate_total_lower_section()
        self.grand_total = self.total_upper_section + self.upper_section_bonus + self.total_lower_section
        print(self.grand_total) 

class YahtzeeGame:
    def __init__(self, root):
         # Initialize the Yahtzee game with GUI elements and game variables
        self.root = root
        self.dice_images = [
            ImageTk.PhotoImage(Image.open("C:/Users/ethan/Desktop/Yahtzee/OneDie.png")),
            ImageTk.PhotoImage(Image.open("C:/Users/ethan/Desktop/Yahtzee/TwoDie.png")),
            ImageTk.PhotoImage(Image.open("C:/Users/ethan/Desktop/Yahtzee/ThreeDie.png")),
            ImageTk.PhotoImage(Image.open("C:/Users/ethan/Desktop/Yahtzee/FourDie.png")),
            ImageTk.PhotoImage(Image.open("C:/Users/ethan/Desktop/Yahtzee/FiveDie.png")),
            ImageTk.PhotoImage(Image.open("C:/Users/ethan/Desktop/Yahtzee/SixDie.png"))
        ]
        self.title_screen = ImageTk.PhotoImage(Image.open("C:/Users/ethan/Desktop/Yahtzee/Yaht.png"))

        self.dice_values = []
        self.reroll_counter = 1
        self.re_rolls = []
        self.keep_die = []
        self.yahtzees = 0
        self.player_counter = 0
        self.create_ui()

    def create_ui(self):
        #Create GUI elements to initilize the game
        self.roll_display = Canvas(self.root, width=1280, height=700, background="grey")
        self.roll_display.grid(column=5, row=5)
        self.roll_display.create_image(600, 330, image =self.title_screen)
        self.start_btn = tk.Button(text="Start", padx = 20, pady = 20, command= self.start)
        self.roll_display.create_window(600, 550,  window= self.start_btn)
        self.game_console = tk.Label(width= 10, height= 10, text="Game")
    
    def start(self):
        #Create game setup and rules screen
        self.menu = tk.Toplevel(self.root)
        self.menu.attributes('-fullscreen', True)
        self.commands = Label(self.menu, text="Welcome to the help & game set up screen!")
        self.commands.grid()
        self.exit_btn = tk.Button(self.menu, text= "Exit", command= self.menu.destroy)
        self.exit_btn.grid()
        self.help_btn = tk.Button(self.menu, text="help", command= self.yahtzee_rules)
        self.help_btn.grid()
        self.set_up_btn = tk.Button(self.menu, text="Set up Game", command=self.setup)
        self.set_up_btn.grid()
    
    def yahtzee_rules(self):
        self.commands.config(text= "EXAMPLE SCORE CARD:\nUPPER SECTION \n Ones (Count and add only ones) \n Twos (Count and add only twos)\n Threes (Count and add only threes) \n Fours (count and add only fours)\n Fives (count and add only fives)\n Sixes (count and add only sixes)\n Total Score \n Bonus if Total >= 63 (Add 35) \n Total \nLOWER SECTION \n 3 of a Kind (Total all dice)\n 4 of a kind(Total all dice)\n Full House (25 Points) \n SM Straight(30 Points) \n LRG Straight (40 Points) \n YAHTZEE (50 Points) \n Chance (Add Total of all Dice) \n YAHTZEE BONUS (100 Points PER, takes place of another unused scorecard item, limit of 3) \n Total of Lower Section \n Total of Upper Section \n Grand Total )")

    def setup(self):
        #Allows game to be setup with 1-4 players
        self.one_player_btn = tk.Button(self.menu, text="One Player Game", command= lambda: self.select_player(1))
        self.one_player_btn.grid()
        self.two_player = tk.Button(self.menu, text="Two Player Game", command= lambda: self.select_player(2))
        self.two_player.grid()
        self.three_player = tk.Button(self.menu, text="Three Player Game", command= lambda: self.select_player(3))
        self.three_player.grid()
        self.four_player = tk.Button(self.menu, text="Four Player Game", command= lambda: self.select_player(4))
        self.four_player.grid()

    def select_player(self, number):
        #Sets up player names and passes # of players
        self.counter = 1
        self.player_name = tk.StringVar
        self.prompt = tk.Label(self.menu, text="Enter Player" + str(self.counter) + "\'s name")
        self.prompt.grid()
        self.name_entry = tk.Entry(self.menu, textvariable= self.player_name)
        self.name_entry.grid()
        self.name_btn = tk.Button(self.menu, text="Confirm Name", command= lambda: self.set_name(number))
        self.name_btn.grid()

    def set_name(self, number):
        #allows player to set name, and sets up amount of players
        self.player_names.append(self.name_entry.get())
        self.counter += 1
        self.prompt.config(text="Enter Player" + str(self.counter) + "\'s name")
        self.name_entry.delete(0, END)
        if len(self.player_names) >= number:
            for i in range(number):
                players.append(Player(self.player_names[i]))
            self.menu.destroy()
            self.roll_display.delete("all")
            self.get_roll()

    def game_output(self, text):
        #Function for output to the game display "Console"
            self.roll_display.create_window(100, 500, window= self.game_console) 
            self.game_console.config(text= text)  

    def get_roll(self):
        #Gets players roll, and also checks to see if the game is completed for that player
        self.get_player()
        self.player.turncount += 1
        self.game_output(str(self.player.name) + "\'s Turn!")
        self.dice_values = []
        for _ in range(5):
            self.dice_values.append(random.randint(1, 6))
        self.update_dice_images(self.dice_values)
        self.create_keep_btns()
        if self.player.turncount > 13:
            self.player.calculate_grand_total()
            self.roll_display.delete("all")
            self.game_output(str(self.player.name) + "\'s final score is: " + str(self.player.grand_total))
            self.roll_display.create_window(1150, 600, window= self.next_turn_btn)

    def create_keep_btns(self):
        #Create keep buttons that allow player to keep dice they have rolled
        re_roll_btn = tk.Button(text="ReRoll", padx=20, pady=20, command=self.re_roll)
        self.roll_display.create_window(400, 200, anchor='n', window=re_roll_btn)

        if self.reroll_counter == 2:
            self.create_scoring_btns()
            re_roll_btn.config(state='disabled')

        self.keep_die = []
        for i, value in enumerate(self.dice_values):
            #Place keep buttons on screen
            keep_button = tk.Button(text='KEEP', command=lambda v=value, b=i: self.keep(v, b))
            row = i // 3
            col = i % 3
            x = 150 * col + 75
            y = 300 * row
            self.roll_display.create_window(x, y, anchor='n', window=keep_button)
            self.keep_die.append(keep_button)

    def keep(self, value, button_index):
        self.re_rolls.append(value)
        self.keep_die[button_index].config(state='disabled')

    def re_roll(self):
        #Re rolls the players hand
        self.roll_display.delete('all')
        self.game_output(str(self.player.name)+ "\'s turn!")
        while len(self.re_rolls) < 5:
            self.re_rolls.append(random.randint(1, 6))
        self.dice_values = self.re_rolls
        self.re_rolls = []
        self.update_dice_images(self.dice_values)

        for button in self.keep_die:
            button.destroy()
        self.create_keep_btns()
        self.reroll_counter += 1

    def create_scoring_btns(self):
        #Creates buttons for scoring
        ones_btn = tk.Button(text="Ones", command= lambda : self.singles(ones_btn, 1, "Ones"))
        twos_btn = tk.Button(text="Twos", command= lambda: self.singles(twos_btn, 2, "Twos"))
        threes_btn = tk.Button(text="Threes", command= lambda: self.singles(threes_btn, 3, "Threes"))
        fours_btn = tk.Button(text="Fours", command= lambda: self.singles(fours_btn, 4, "Fours"))
        fives_btn = tk.Button(text="Fives", command= lambda: self.singles(fives_btn, 5, "Fives"))
        sixes_btn = tk.Button(text="Sixes", command= lambda: self.singles(sixes_btn, 6, "Sixes"))
        three_of_a_kind_btn = tk.Button(text="Three of a Kind", command= lambda: self.three_of_kind(three_of_a_kind_btn))
        four_of_a_kind_btn = tk.Button(text="Four of a Kind", command= lambda: self.four_of_kind(four_of_a_kind_btn))
        full_house_btn = tk.Button(text="Full House", command= lambda: self.full_house(full_house_btn))
        sm_straight_btn = tk.Button(text="Small Straight", command= lambda: self.sm_straight(sm_straight_btn))
        lrg_straight_btn = tk.Button(text="Large Straight", command = lambda: self.lrg_straight(lrg_straight_btn))
        chance_btn = tk.Button(text="Chance", command= lambda: self.chance(chance_btn))
        yahtzee_btn = tk.Button(text="Yahtzee", command= lambda: self.yahtzee(yahtzee_btn))
        self.scoring_btns = [ones_btn,twos_btn,threes_btn,fours_btn,fives_btn,sixes_btn,three_of_a_kind_btn,four_of_a_kind_btn,full_house_btn,sm_straight_btn,lrg_straight_btn,chance_btn, yahtzee_btn]
        self.yval_list = []
        if self.player.scores["Yahtzee"] == 50 and self.dice_values.count(self.dice_values[0]) == 5:
            self.yahtzee_bonus_btn = tk.Button(text="Yahtzee Bonus", command= self.yahtzee_bonus)
            self.roll_display.create_window(1225, 554.4, window= self.yahtzee_bonus_btn)
            
        for i, scoring_button in enumerate(self.scoring_btns):
            spacing = 1.54
            row = i + 1
            x = 1000  # Adjust x-coordinate for button placement
            y = 30  * row * spacing  # Adjust y-coordinate for button placement under each die
            self.yval_list.append(y)
            self.roll_display.create_window(x, y, anchor='nw', window=scoring_button)
        for i, score in enumerate(self.player.scores):
            #Checks if a player has already scored a certain item
            if self.player.scores[score] != None:
                self.scoring_btns[i].config(state="disabled")
                self.roll_display.create_text(1150, self.yval_list[i], text= self.player.scores[score])
                

    def get_player(self):
        self.player = players[self.player_counter]
        self.player_counter += 1
        if self.player_counter > len(players) - 1:
            self.player_counter = 0
#Functions for scoring player's hands
    def singles(self, button, number, category):
        score = 0
        for i in self.dice_values:
            if i == number:
                score += number
        button.config(state ='disabled')
        self.calculate_and_display_score(category, score, self.yval_list[number - 1])
        
    def three_of_kind(self, button):
        sorted_dice = sorted(self.dice_values, reverse=True)
        score = 0
        for i in range(len(sorted_dice) - 2):
            if sorted_dice[i] == sorted_dice[i + 1] == sorted_dice[i + 2]:
                score = sum(sorted_dice)
                break
        self.calculate_and_display_score("ThreeOfAKind",score, yval= 265)
        button.config(state='disabled')
       
    def four_of_kind(self, button):
        sorted_dice = sorted(self.dice_values, reverse=True)
        score = 0
        for i in range(len(sorted_dice) - 3):
            if sorted_dice[i] == sorted_dice[i + 1] == sorted_dice[i + 2] == sorted_dice[i + 3]:
                score = sum(sorted_dice)
                break
        self.calculate_and_display_score("FourOfAKind", score, yval= 300)
        button.config(state='disabled')
        
    def full_house(self, button):
        sorted_dice = sorted(self.dice_values, reverse=True)
        score = 0
        if (sorted_dice[0] == sorted_dice[1] and sorted_dice[2] == sorted_dice[3] == sorted_dice[4]) or (sorted_dice[0] == sorted_dice[1] == sorted_dice[2] and sorted_dice[3] == sorted_dice[4]):
            score = 25
        self.calculate_and_display_score("FullHouse", score, yval= 335)
        button.config(state='disabled')
        
    def sm_straight(self, button):
        score = 0
        sorted_dice = sorted(set(self.dice_values))  
        for i in range(len(sorted_dice) - 3):
            if sorted_dice[i] + 3 >= sorted_dice[i + 3]:
                score = 30
                break
        self.calculate_and_display_score("SmallStraight", score, yval=370)
        button.config(state='disabled')

        
        

    def lrg_straight(self, button):
        score = 0
        sorted_dice = sorted(self.dice_values)
        if ( sorted_dice == [1, 2, 3, 4, 5] or
        sorted_dice == [2, 3, 4, 5, 6] 
        ):
            score = 40
        self.calculate_and_display_score("LargeStraight",score, yval = 405)
        button.config(state='disabled')
       
    def chance(self, button):
        score = sum(self.dice_values)
        self.calculate_and_display_score("Chance",score, yval = 440)
        button.config(state='disabled')
    
    def yahtzee(self, button):
        score = 0
        if self.dice_values.count(self.dice_values[0]) == 5:
            score = 50
            self.yahtzees += 1
            self.game_console.config(text="YAHTZEE!!!!!!")
        self.calculate_and_display_score("Yahtzee", score, yval = 475)
        button.config(state = 'disabled')
    
        
    def calculate_and_display_score(self,category, score, yval):
        for button in self.scoring_btns:
            button.config(state="disabled")
        self.player.set_score(category, score)
        self.roll_display.create_text(1150, yval, text=str(score))  
        self.next_turn_btn = tk.Button(text="Next Turn", command= self.play_turn)
        self.roll_display.create_window(1150, 600, window= self.next_turn_btn)


    def update_dice_images(self, rolls):
        row, col = 0, 0
        spacing = 20
        for i in range(5):
            x = 150 * col + spacing * col
            y = 150 * row + spacing * row
            self.roll_display.create_image(x, y, anchor='nw', image=self.dice_images[rolls[i] - 1])
            col += 1
            if col == 3:
                col = 0
                row += 1
    def yahtzee_bonus(self):
        self.game_console.config(text="YAHTZEE BONUS!!!")
        if self.player.yahtzee_bonus_count == 2:
            self.yahtzee_bonus_btn.config(state="disabled")
        for button in self.scoring_btns:
            category = button.cget("text")
            button.config(command=lambda cat=category: self.calculate_and_display_score(cat, 100, 555.4))
        self.player.yahtzee_bonus_count += 1

        
    def play_turn(self):
        self.roll_display.delete("all")
        self.reroll_counter = 1
        self.player.turncount += 1
        self.get_roll()
#Main program is run here
if __name__ == "__main__":
    root = Tk()
    game = YahtzeeGame(root)
    root.state('zoomed')
    root.mainloop()
