"""Name: Hypixel_Api
Author: Nathaniel McCoy
Description: Basic Example to pull current Bank and Purse information from the SkyCrypt API (which uses the Hypixel API.) with a GUI"""

from tkinter import *
from tkinter import messagebox
import requests 

class MainAPI:
    def __init__(self):
        self.root =Tk()
        self.root.geometry("200x200+800+300")

        self.lbl_IGN = Label(self.root, text="IGN")
        self.lbl_IGN.grid(row=0, column=0)

        self.entry_IGN = Entry(self.root)
        self.entry_IGN.grid(row=0, column=1)

        self.lbl_profile = Label(self.root, text="Profile")
        self.lbl_profile.grid(row=1, column=0)

        self.entry_profile = Entry(self.root)
        self.entry_profile.grid(row=1, column=1)

        self.btn_submit = Button(self.root, text="Coins", command=self.get_entry_coins)
        self.btn_submit.grid(row=4, column=0)

        self.btn_submit = Button(self.root, text="Slayers", command=self.get_entry_slayers)
        self.btn_submit.grid(row=4, column=1)

        mainloop()

    def get_entry_coins(self):
        name = self.entry_IGN.get()
        profile = self.entry_profile.get()
        URLcoins = f"https://sky.shiiyu.moe/api/v2/coins/{name}/{profile}"

        response_coins = requests.get(URLcoins)
        self.coin = response_coins.json()
        if self.coin.get('cute_name') == None:
            print(f"Error in coins! {self.coin.get('error')}")
            self.show_error_coins()
        else:
            bank = int(self.coin.get('bank'))
            purse = int(self.coin.get('purse'))
            if response_coins.status_code == 200:
                print("fetched coin info")
                messagebox.showinfo("Hypixel Bank", f"Viewing {name}'s coin info on profile {profile}.\nCoins in bank:\t{bank:,}\nCoins in purse:\t{purse:,}")
            else:
                print(f"Error in Coins! {self.coin.get('error')}")
                self.show_error_coins()

    def get_entry_slayers(self):
        playerName = self.entry_IGN.get()
        profileName = self.entry_profile.get()
        URLslayers = f"https://sky.shiiyu.moe/api/v2/slayers/{playerName}/{profileName}"
        response_slayers = requests.get(URLslayers)
        self.slayers = response_slayers.json()
        profileID = list(self.slayers.keys())[0] 
        if self.slayers.get(f"{profileID}").get("cute_name") == None:
           print(f"Error in Slayers! {main.get('error')}")
           self.show_error_slayers()
        else:
            if response_slayers.status_code == 200:
                zombieStats = self.slayers.get(f"{profileID}").get("data").get("slayers").get("zombie")
                print("fetched slayers info")
                messagebox.showinfo("Hypixel Slayers", f"""Viewing {playerName}'s Slayer info on profile {profileName}.
                                    \nTotal XP:\t{self.slayers.get(f"{profileID}").get("data").get("total_slayer_xp")}
                                    \nZombie:\t""")
            else:
                print(f"Error in Slayers! {self.slayers.get('error')}")
                self.show_error_slayers()
           
            

    def show_error_coins(self):
     error = self.coin.get('error')
     messagebox.showerror(f"An Error Has occured", f"An Error has occured when fetching the coin info.\nPlease make sure you typed the information correctly\nThe cause from the API is shown below:\n{error}")

    def show_error_slayers(self):
     error = self.slayers.get('error')
     messagebox.showerror(f"An Error Has occured", f"An Error has occured when fetching slayers info.\nPlease make sure you typed the information correctly\nThe cause from the API is shown below:\n{error}")
        
main = MainAPI()
        