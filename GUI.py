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
from shop import Shop

# Create a new Tkinter window
window = tk.Tk()
window.title("Game Menu")
window.geometry("400x400")

# Create a label for the player's information
player_info_label = tk.Label(window, text="Player Information:")
player_info_label.pack()

# Create labels to display player's name, money, health, and points
name_label = tk.Label(window, text="Name: ")
name_label.pack()
money_label = tk.Label(window, text="Money: ")
money_label.pack()
health_label = tk.Label(window, text="Health: ")
health_label.pack()
points_label = tk.Label(window, text="Points: ")
points_label.pack()

# Function to handle player name input


def get_player_name(player: Player):
    player_name = askstring("Player Name", "Enter your name:")
    if player_name:
        player.name = player_name
        update_player_info(player)


# Create a label for the game menu
menu_label = tk.Label(window, text="Game Menu:")
menu_label.pack()

# Create buttons for each game option
room1_button = tk.Button(window, text="Enter Room 1")
room1_button.pack()
room2_button = tk.Button(window, text="Enter Room 2")
room2_button.pack()
room3_button = tk.Button(window, text="Enter Room 3")
room3_button.pack()
room4_button = tk.Button(window, text="Enter Room 4")
room4_button.pack()
shop_button = tk.Button(window, text="Visit Shop")
shop_button.pack()
inventory_button = tk.Button(window, text="View Inventory")
inventory_button.pack()
exit_button = tk.Button(window, text="Exit")
exit_button.pack()


def load_room_data():
    rooms = []
    for i in range(4):
        file_name = "Room"+str(i+1)+".txt"
        with open(file_name, 'r') as file:
            lines = file.readlines()
            description = lines[0].strip("\n") + " " + lines[1].strip("\n")
            enemy = lines[4].strip("\n").split(",")
            enemy = Enemy(enemy[0], enemy[1], enemy[2])
            points = int(lines[7].strip("\n"))
            enemy.points = points
            weapon = lines[10].strip("\n").split(",")
            weapon = Weapon(weapon[0], weapon[1], weapon[2])
            money = int(lines[13].strip("\n"))

            treasure = lines[16].strip("\n").split(",")
            if treasure[0] == "None":
                treasure = None
            else:
                treasure = Treasure(treasure[0], treasure[1])

            healingPad = lines[19].strip("\n")
            if healingPad == "None":
                healingPad = None
            else:
                healingPad = int(healingPad)

            key = lines[22].strip("\n").split(",")
            if key[0] == "None":
                key = None
            else:
                key = Key(key[0], key[1])
            room = Room(description=description, enemy=enemy, points=points, weapon=weapon,
                        money=money, treasure=treasure, healingPad=healingPad, key=key)
            rooms.append(room)
    return rooms


def read_shop_data():
    shop_data = {}
    weapons = {}
    keys = {}
    healing_pads = {}
    armours = {}
    with open("Shop.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("weapon"):
                weapon_data = line.split(":")
                weapon_name = weapon_data[0]
                name, damage, price = map(str, weapon_data[1].split(","))
                weapon = Weapon(name=name, damage=int(
                    damage), price=int(price))
                weapons[weapon_name] = weapon

            elif line.startswith("key"):
                key_data = line.split(":")
                code, price = map(str, key_data[1].split(","))
                key = Key(code=int(code), price=int(price))
                keys[code] = key

            elif line.startswith("healingPad"):
                healing_pad_data = line.split(":")
                healing_pad_name = healing_pad_data[0]
                health, price = map(str, healing_pad_data[1].split(","))
                healing_pad = HealingPad(
                    health=int(health), price=int(price))
                healing_pads[healing_pad_name] = healing_pad

            elif line.startswith("armour"):
                armour_data = line.split(":")
                armour_name = armour_data[0]
                durability, price = map(str, armour_data[1].split(","))
                armour = Armour(durability=int(durability), price=int(price))
                armours[armour_name] = armour

        shop_data["weapons"] = weapons
        shop_data["keys"] = keys
        shop_data["healing_pads"] = healing_pads
        shop_data["armours"] = armours

        return shop_data


def update_player_info(player: Player):
    # Update the labels with the player's information
    name_label.config(text="Name: " + player.name)
    money_label.config(text="Money: " + str(player.money))
    health_label.config(text="Health: " + str(player.health))
    points_label.config(text="Points: " + str(player.points))


def combat(player: Player, enemy: Enemy, use_armor, weapon_index):
    if use_armor and player.inventory.armour:
        enemy_damage = enemy.damage / player.inventory.armour.durability
    else:
        enemy_damage = enemy.damage

    player.health -= enemy_damage
    enemy.health -= player.inventory.weapons[weapon_index].damage

    if enemy.health <= 0:
        player.points += enemy.points
        del enemy
        print("You defeated the enemy and gained points")
    elif player.health <= 0:
        player.health = 0
        player.points -= 2
        print("You lost the battle lost 2 points")
        player.inventory.weapons = []
        player.inventory.armour = None

# Function to handle room button clicks


def enter_room(player: Player, room: Room):
    messagebox.showinfo("Enter Room", "You entered Room " + str(room))
    messagebox.showinfo("Enemy Information", str(room.enemy))
    # Kullanıcının envanterindeki silahları listele
    weapon_names = [weapon.name for weapon in player.inventory.weapons]
    chosen_weapon = None

    # Silah seçimini isteyen bir mesaj kutusu oluştur
    if weapon_names:
        weapon_index = messagebox.askquestion(
            "Choose Weapon Index", "Select a weapon from your inventory:\n\n" + "\n".join(weapon_names))
    else:
        messagebox.showinfo(
            "No Weapons", "You don't have any weapons in your inventory!")

    def ask_use_armor():
        result = messagebox.askquestion(
            "Use Armor", "Do you want to use armor?", icon='question')
        return result == 'yes'

    # Zırh kullanımını sorgula
    use_armor = ask_use_armor()
    combat(player=player, room=room, use_armor=use_armor,
           weapon_index=weapon_index)

# Function to handle shop button click


def visit_shop(player: Player, shop_data):
    shop = Shop(player, shop_data)
    shop.main_menu()

# Function to handle inventory button click


def view_inventory(player:Player):
    inventory:Inventory = player.inventory
    messagebox.showinfo("View Inventory", f"You are viewing your inventory {str(inventory)}")

# Function to handle exit button click


def exit_game():
    window.destroy()


def main():
    # Prompt the player for their name when the window is opened
    player = Player()
    rooms = load_room_data()
    shop_data = read_shop_data()

    window.after(0, get_player_name, player)

    # update_player_info(player)
    # Bind the button clicks to the corresponding functions

    room1_button.config(command=lambda: enter_room(player, rooms[0]))
    room2_button.config(command=lambda: enter_room(player, rooms[1]))
    room3_button.config(command=lambda: enter_room(player, rooms[2]))
    room4_button.config(command=lambda: enter_room(player, rooms[3]))
    shop_button.config(command=lambda: visit_shop(player, shop_data))
    inventory_button.config(command=lambda: view_inventory(player=player))
    exit_button.config(command=exit_game)

    # Start the Tkinter event loop
    window.mainloop()


if __name__ == "__main__":
    main()
