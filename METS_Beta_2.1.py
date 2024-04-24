"""Name: METS_Beta_2.1.py
Author: Microwave (Contact MicrowaveGoMMM on discord for any questions)
Description: (M)icrowave's (E)xternal (T)racker for (S)kyblock. (its all about the mets babyyyyyy)
Date: 4/23/24"""

#NOTE: This is a really fucking bad way of doing any of this. What i'm doing should NOT be attempted by anyone who has any self respect. All of this shitfuck code is shitfuck code that works somehow.
#NOTE: Too bad!

from tkinter import *
from tkinter import messagebox
import requests 
#Define the class (aka. start this bullshit)
class MainAPI:
    #make the fancy shmancy menu
    #NOTE: this menu looks fucking terrible.
    #NOTE: Too bad!
    #TODO: Redo The Menu, if someone other than me sees this and knows of a better way of doing this, contact me on discord (MicrowaveGoMMM)
    #NOTE: (This is technically compatible with mobile using Pydroid 3!)
    #TODO: HOW THE FUCK DO I CHANGE THE MENU NAME
    def __init__(self):
        self.root =Tk()
        self.root.geometry("200x200+800+300")
        #Get the In Game Name
        self.lbl_IGN = Label(self.root, text="IGN")
        self.lbl_IGN.grid(row=0, column=0)
        
        self.entry_IGN = Entry(self.root)
        self.entry_IGN.grid(row=0, column=1)
        #Get the profile using the "cute_name" rather than the ID
        self.lbl_profile = Label(self.root, text="Profile")
        self.lbl_profile.grid(row=1, column=0)

        self.entry_profile = Entry(self.root)
        self.entry_profile.grid(row=1, column=1)
        #SHOW THE BUTTONS
        #TODO: MAKE MORE BUTTONS
        self.btn_submit = Button(self.root, text="Coins", command=self.get_entry_coins)
        self.btn_submit.grid(row=4, column=0)

        self.btn_submit = Button(self.root, text="Slayers", command=self.get_entry_slayers)
        self.btn_submit.grid(row=4, column=1)

        mainloop()
    #Get all the coin data for when the user presses "coins"
    def get_entry_coins(self):
        name = self.entry_IGN.get()
        profile = self.entry_profile.get()
        URLcoins = f"https://sky.shiiyu.moe/api/v2/coins/{name}/{profile}"

        response_coins = requests.get(URLcoins)
        self.coin = response_coins.json()
        #check for error
        if self.coin.get('cute_name') == None:
            print(f"Error in coins! {self.coin.get('error')}")
            self.show_error_coins()
        #theres no error
        else:
            bank = int(self.coin.get('bank'))
            purse = int(self.coin.get('purse'))
            #checking for another error 
            if response_coins.status_code == 200:
                #showing the information
                print("fetched coin info")
                messagebox.showinfo("Hypixel Bank", f"Viewing {name}'s coin info on profile {profile}.\nCoins in bank:\t{bank:,}\nCoins in purse:\t{purse:,}")
            else:
                #fuck
                print(f"Error in Coins! {self.coin.get('error')}")
                self.show_error_coins()
    #Get all the Slayer data for when the user presses "Slayers"
    def get_entry_slayers(self):
        #Get the information and store that bitch
        playerName = self.entry_IGN.get()
        profileName = self.entry_profile.get()
        URLslayers = f"https://sky.shiiyu.moe/api/v2/slayers/{playerName}/{profileName}"
        response_slayers = requests.get(URLslayers)
        self.slayers = response_slayers.json()
        #get the profile ID for easier reference
        profileID = list(self.slayers.keys())[0] 
        #check for errors
        #NOTE: This is different than the coins method because the coins call DOES NOT have a profile ID. This is a mistake on the coins rather than here IMO.
        if self.slayers.get(f"{profileID}") == None:
           print(f"Error in Slayers! {main.get('error')}")
           self.show_error_slayers()
        else:
            #Check for error again.
            if response_slayers.status_code == 200:
                #Store the Slayers data to make code a little smaller.
                #TODO: The rest of the slayers (Spider, Blaze, Enderman, Vampire, Wolf.)
                zombieStats = self.slayers.get(f"{profileID}").get("data").get("slayers").get("zombie")
                print("fetched slayers info")
                #Show the information
                #NOTE: I want to redo this entire thing.
                #TODO: show another window with more choices with all the slayers instead of showing all the slayers on one simple INFO box.
                messagebox.showinfo("Hypixel Slayers", f"""Viewing {playerName}'s Slayer info on profile {profileName}.
                                    \nTotal XP:\t{self.slayers.get(f"{profileID}").get("data").get("total_slayer_xp")}
                                    \nZombie:\tLevel: {zombieStats.get('level').get('currentLevel')} (Xp: {zombieStats.get('level').get('xp')})
                                    \n\tXp needed: {zombieStats.get('level').get('xpForNext') - zombieStats.get('level').get('xp')}
                                    \n\tTotal kills: {zombieStats.get('kills').get('total')}""")
            else:
                #erroed aagain beacvuse ofc there is
                print(f"Error in Slayers! {self.slayers.get('error')}")
                self.show_error_slayers()
           
            
    #NOTE: There is def a better way to distinguish errors... Too Bad!
    #show coin error
    def show_error_coins(self):
     error = self.coin.get('error')
     messagebox.showerror(f"An Error Has occured", f"An Error has occured when fetching the coin info.\nPlease make sure you typed the information correctly\nThe cause from the API is shown below:\n{error}")
    #show slayer errors
    def show_error_slayers(self):
     error = self.slayers.get('error')
     messagebox.showerror(f"An Error Has occured", f"An Error has occured when fetching slayers info.\nPlease make sure you typed the information correctly\nThe cause from the API is shown below:\n{error}")
        
main = MainAPI()
        