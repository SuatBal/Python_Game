from tkinter import messagebox, Tk
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
import main as mn
from player import Player
from room import Room
from enemy import Enemy
from weapon import Weapon
from treasure import Treasure
from key import Key
from inventory import Inventory
from healingPad import HealingPad
from armour import Armour


class Shop:
    def __init__(self, player: Player, shop_data):
        self.player: Player = player
        self.shop_data = shop_data

    def buy_weapons(self):
        msg = "Available Weapons:\n"
        weapons = "\n".join(
            [f"{weapon_name}: {weapon}" for weapon_name, weapon in self.shop_data["weapons"].items()])
        msg = msg + weapons 
        weapon_choice = askstring(
            "Buy Weapons", msg+"\nEnter the name of the weapon you want to buy (or 'back' to go back to the shop menu):")
        if weapon_choice == "back":
            return

        if weapon_choice in self.shop_data["weapons"]:
            weapon: Weapon = self.shop_data["weapons"][weapon_choice]
            if self.player.money >= weapon.price:
                self.player.inventory.weapons.append(weapon)
                self.player.money -= weapon.price
                messagebox.showinfo("Purchase Successful",
                                    f"You have bought {weapon.name}!")
                del self.shop_data["weapons"][weapon_choice]
            else:
                messagebox.showinfo("Insufficient Funds",
                                    "Not enough money to buy this weapon.")
        else:
            messagebox.showinfo("Invalid Weapon", "Invalid weapon choice.")

    def buy_keys(self):
        msg = "Available Keys:\n"
        keys = "\n".join([f"{code}: {key}" for code, key in self.shop_data["keys"].items()])
        msg = msg + keys
        key_choice = askstring(
            "Buy Keys", msg+"\nEnter the code of the key you want to buy (or 'back' to go back to the shop menu):")
        if key_choice == "back":
            return

        key_choice = key_choice
        if key_choice in self.shop_data["keys"]:
            key: Key = self.shop_data["keys"][key_choice]
            if self.player.money >= key.price:
                self.player.inventory.keys.append(key)
                self.player.money -= key.price
                messagebox.showinfo(
                    "Purchase Successful", f"You have bought the key with code {key.code}!")
                del self.shop_data["keys"][key_choice]
            else:
                messagebox.showinfo("Insufficient Funds",
                                    "Not enough money to buy this key.")
        else:
            messagebox.showinfo("Invalid Key", "Invalid key choice.")

    def buy_healing_pads(self):
        msg = "Available Healing Pads\n"
        healing_pads = "\n".join(
            [f"{key}: {value}" for key, value in self.shop_data["healing_pads"].items()])
        msg = msg + healing_pads
        healing_pad_choice = askstring(
            "Buy Healing Pads", msg+"\nEnter the number of the healing pad you want to buy (or 'back' to go back to the shop menu):")
        if healing_pad_choice == "back":
            return

        if healing_pad_choice in self.shop_data["healing_pads"]:
            healing_pad: HealingPad = self.shop_data["healing_pads"][healing_pad_choice]
            if self.player.money >= healing_pad.price:
                self.player.inventory.healingPad = healing_pad
                self.player.money -= healing_pad.price
                self.player.health += healing_pad.health
                messagebox.showinfo("Purchase Successful",
                                    "You have bought a healing pad!")
                del self.shop_data["healing_pads"][healing_pad_choice]
            else:
                messagebox.showinfo("Insufficient Funds",
                                    "Not enough money to buy healing pad.")
        else:
            messagebox.showinfo("Invalid Healing Pad",
                                "Invalid healing pad choice.")

    def buy_armour(self):
        msg = "Available Armours\n"
        armours = "\n".join([f"{armour_name}: {armour}" for armour_name, armour in self.shop_data["armours"].items()])
        msg = msg + armours
        armour_choice = askstring(
            "Buy Armour", msg+"\nEnter the name of the armour you want to buy (or 'back' to go back to the shop menu):")
        if armour_choice == "back":
            return

        if armour_choice in self.shop_data["armours"]:
            armour: Armour = self.shop_data["armours"][armour_choice]
            if self.player.money >= armour.price:
                self.player.inventory.armour = armour
                self.player.money -= armour.price
                messagebox.showinfo("Purchase Successful",
                                    f"You have bought {str(armour)}!")
                del self.shop_data["armours"][armour_choice]
            else:
                messagebox.showinfo("Insufficient Funds",
                                    "Not enough money to buy this armour.")
        else:
            messagebox.showinfo("Invalid Armour", "Invalid armour choice.")

    def main_menu(self):
        messagebox.showinfo("Shop", "Welcome to the shop!")
        while True:
            shop_choice = askstring(
                "Shop Menu", "Select an option:\n1. Buy Weapons\n2. Buy Keys\n3. Buy Healing Pads\n4. Buy Armour\n5. Exit Shop")

            if shop_choice == '1':
                self.buy_weapons()
            elif shop_choice == '2':
                self.buy_keys()
            elif shop_choice == '3':
                self.buy_healing_pads()
            elif shop_choice == '4':
                self.buy_armour()
            elif shop_choice == '5':
                break
            else:
                messagebox.showwarning("Invalid choice", "Please try again.")

            if shop_choice == 'exit':
                break
