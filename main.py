from enemy import Enemy
from weapon import Weapon
from treasure import Treasure
from key import Key
from room import Room
from player import Player
from inventory import Inventory
from healingPad import HealingPad
from armour import Armour 

                               
def display_player_info(player: Player):
    print(f"Name: {player.name}")
    print(f"Money: {player.money}")
    print(f"Health: {player.health}")
    print(f"Points: {player.points}")

def display_inventory(player: Player):
    print(player.inventory)



def main():
    name = input("Enter your name: ")
    player = Player(name=name)
    print(player)
    rooms = load_room_data()
    shop_data = read_shop_data()

    while True:
        print("\n===== Game Menu =====")
        print("1. Enter Room 1")
        print("2. Enter Room 2")
        print("3. Enter Room 3")
        print("4. Enter Room 4")
        print("5. Visit Shop")
        print("6. View Inventory")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            enter_room(player=player, room=rooms[0])
        elif choice == "2":
            enter_room(player=player, room=rooms[1])
        elif choice == "3":
            enter_room(player=player, room=rooms[2])
        elif choice == "4":
            enter_room(player=player, room=rooms[4])
        elif choice == "5":
            print("Welcome to the shop!")
            while True:
                print("Select an option:")
                print("1. Buy Weapons")
                print("2. Buy Keys")
                print("3. Buy Healing Pads")
                print("4. Buy Armor")
                print("5. Exit Shop")

                shop_choice = input("Enter your choice: ")

                if shop_choice == "1":
                    print("Available Weapons:")
                    for weapon_name, weapon in shop_data["weapons"].items():
                        print(f"{weapon_name}: {weapon}")

                    weapon_choice = input("Enter the name of the weapon you want to buy (or 'back' to go back to the shop menu): ")
                    if weapon_choice == "back":
                        continue

                    if weapon_choice in shop_data["weapons"]:
                        weapon:Weapon = shop_data["weapons"][weapon_choice]
                        if player.money >= weapon.price:
                            player.inventory.weapons.append(weapon)
                            player.money -= weapon.price
                            print(f"You have bought {weapon.name}!")
                            del shop_data["weapons"][weapon_choice]
                        else:
                            print("Not enough money to buy this weapon.")
                    else:
                        print("Invalid weapon choice.")

                elif shop_choice == "2":
                    print("Available Keys:")
                    for code, key in shop_data["keys"].items():
                        print(f"{code}: {key}")

                    key_choice = input("Enter the code of the key you want to buy (or 'back' to go back to the shop menu): ")
                    if key_choice == "back":
                        continue

                    key_choice = int(key_choice)
                    if key_choice in shop_data["keys"]:
                        key:Key = shop_data["keys"][key_choice]
                        if player.money >= key.price:
                            player.inventory.keys.append(key)
                            player.money -= key.price
                            print(f"You have bought the key with code {key.code}!")
                            del shop_data["keys"][key_choice]
                        else:
                            print("Not enough money to buy this key.")
                    else:
                        print("Invalid key choice.")

                elif shop_choice == "3":
                    print("Available Healing Pads:")                       
                    for key, value in shop_data["healing_pads"].items():
                        print(f"{key}: {value}")

                    healing_pad_choice = input("Enter the number of the healing pad you want to buy (or 'back' to go back to the shop menu): ")
                    if healing_pad_choice == "back":
                        continue
                                            
                    if healing_pad_choice in shop_data["healing_pads"]:
                        healing_pad:HealingPad = shop_data["healing_pads"][healing_pad_choice]
                        if player.money >= healing_pad.price:
                            player.inventory.healingPad = healing_pad
                            player.money -= healing_pad.price
                            player.health += healing_pad.health
                            print(f"You have bought a healing pad!")
                            del shop_data["healing_pads"][healing_pad_choice]
                        else:
                            print("Not enough money to buy healing pad.")
                    else:
                        print("Invalid healing pad choice.")

                elif shop_choice == "4":
                    print("Available Armours:")
                    for armour_name, armour in shop_data["armours"].items():
                        print(f"{armour_name}: {armour}")

                    armour_choice = input("Enter the name of the armour you want to buy (or 'back' to go back to the shop menu): ")
                    if armour_choice == "back":
                        continue

                    if armour_choice in shop_data["armours"]:
                        armour:Armour = shop_data["armours"][armour_choice]
                        if player.money >= armour.price:
                            player.inventory.armour = armour
                            player.money -= armour.price
                            print(f"You have bought {armour}!")
                            del shop_data["armours"][armour_choice]
                        else:
                            print("Not enough money to buy this armour.")
                    else:
                        print("Invalid armour choice.")

                elif shop_choice == "5":
                    print("Exiting shop...")
                    break

                else:
                    print("Invalid choice. Please try again.")


        elif choice == "6":
            display_inventory(player=player)
        elif choice == "7":
            print("Exiting the game...")
            break
        else:
            print("Invalid choice! Please try again")

        display_player_info(player=player)

        if player.points >= 10:
            print("Congratulations! You won the game!")
            break
        elif player.points < 0:
            print("Game over! You lost the game!")


if __name__ == "__main__":
    main()
