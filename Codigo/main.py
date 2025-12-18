import os
from datetime import datetime
from User_functions import add_user, get_user, mod_user, delete_user, val_user, val_age, val_email, val_password
from Workout_functions import add_workout, delete_workout, get_workout, mod_workout, get_workout_by_user, count_workouts, delete_workout_by_user, val_date, val_amt_tp, val_intensity, val_wo, val_amt
from getpass import getpass
import hashlib

def hash_password(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def menu_add_user():
    # clean_con()
    print(f"\n{'='*10}{' '*5} ADD USER {' '*5}{'='*10}")
    print("")
    
    try:
        name = input("Name: ")
        age = val_age(input("Age: "))
        city = input("City: ")
        email = val_email(input("Email: "),"Y")
        pwd = hash_password(val_password(getpass("Select your password: "),getpass("Type your password again: ")))

        new_user = add_user(name, age,city, email, pwd)

        print(f"New user, {new_user['name']}, added successfully with ID {new_user['user_id']} and email: {new_user['email']}")

    except ValueError as e:
        print(e)
    
    pause()

def menu_get_user():
    # clean_con()
    print(f"\n{'='*10}{' '*5} GET USER {' '*5}{'='*10}")
    print("")
    
    try:
        user = get_user(val_user(input("User ID: ")))
        print(f"Name: {user['name']}\nAge: {user['age']}\nCity: {user['city']}")
    except ValueError as e:
        print(e)
    
    pause()

def menu_mod_user():
    # clean_con()
    print(f"\n{'='*10}{' '*4} MODIFY USER {' '*3}{'='*10}")
    print("")
    try:
        user_id = val_user(input("User ID to be modified: "))
    except ValueError as e:
        print(e)
        pause()
        return
    while True:
        print("\nWhich field would you like to change?")
        print("     1.- Name")
        print("     2.- Age")
        print("     3.- City")
        print("     4.- Email")
        print("     5.- Password")
        print("\n     0.- Cancel")
        opcion = input("\nSelect an option: ")
        try:
            match opcion:
                case "0":
                    return
                case "1":
                    field = "name"
                    new_value = input("\nIntroduce the new name: ")
                    break
                case "2":
                    field = "age"
                    new_value = val_age(input("\nIntroduce the new age: "))
                    break
                case "3":
                    field = "city"
                    new_value = input("\nIntroduce the new city: ")
                    break
                case "4":
                    field = "email"
                    new_value = val_email(input("\nIntroduce the new email: "),"Y")
                    break
                case "5":
                    field = "password"
                    new_value = hash_password(val_password(getpass("Select your new password: "),getpass("Type your new password again: ")))
                    break
                case _:
                    print("Option is not valid")
                    pause()
        except ValueError as e:
            print(e)
            pause()

    mod_user(user_id, field, new_value)
    print("User has been modified successfully.")
    pause()
    
def menu_del_user():
    # clean_con()
    print(f"\n{'='*10}{' '*4} DELETE USER {' '*3}{'='*10}")
    print("")
    try:
        user_id = val_user(input("User ID: "))
    except ValueError as e:
        print(e)
        pause()
        return

    # Delete all the workouts related to the User ID that is going to be deleted
    x=count_workouts(user_id)
    delete_workout_by_user(user_id)
    if x==0:
        print(f"No workouts found for User ID {user_id}")
    else:
        print(f"{x} workout logs have been removed successfully from User ID {user_id}")

    # Delete user
    delete_user(user_id)
    print(f"User ID {user_id} was deleted successfully.")
    pause()

def menu_add_wo():
    # clean_con()
    print(f"\n{'='*10}{' '*4} ADD WORKOUT {' '*3}{'='*10}")
    print("")
    try:
        user_id = val_user(input("User ID: "))
        wo_date = val_date(input("Workout date YYYY-MM-DD: "))
        exercise = input("Exercise: ")
        amount_type = val_amt_tp(input("Amount type 'r' (reps) / 't' (time): "))
        amount = val_amt(input("Amount: "))
        intensity = val_intensity(input("Intensity 'Lo'/'Me'/'Hi': "))

        new_wo = add_workout(user_id,wo_date,exercise,amount,amount_type,intensity)

        print(f"New workout logged --> Workout ID: {new_wo['wo_id']} | User ID: {new_wo['user_id']} | Date: {new_wo['wo_date']} | Exercise: {new_wo['exercise']} | {new_wo['amount']} {'min' if new_wo['amount_type'] == 't' else 'repeticiones'} | Intensity:  {new_wo['intensity']}")
    except ValueError as e:
        print(e)
    pause()


def menu_get_wo():
    # clean_con()
    print(f"\n{'='*10}{' '*4} GET WORKOUT {' '*3}{'='*10}")
    print("")
    try:
        user_id = val_user(input("User ID: "))
        wo_ini_date = input("From date YYYY-MM-DD (optional)): ").strip() or None
        wo_end_date = None
        if wo_ini_date:
            wo_ini_date = val_date(wo_ini_date)
            wo_end_date = input("To date YYYY-MM-DD (optional)): ").strip() or None
        if wo_end_date:
            wo_end_date = val_date(wo_end_date, True)
        
        workouts = get_workout_by_user(user_id,wo_ini_date,wo_end_date)
        if not workouts:
            print("No workouts found for the selected filters.")
            pause()
            return
        for w in workouts:
            print(f"Workout ID: {w['wo_id']} | User ID: {w['user_id']} | Date: {w['wo_date']} | Exercise: {w['exercise']} | {w['amount']} {'min' if w['amount_type'] == 't' else 'repeticiones'} | Intensity:  {w['intensity']}")
        
        total_reps = sum(int(w['amount']) for w in workouts if w['amount_type']=='r')
        total_mins = sum(int(w['amount']) for w in workouts if w['amount_type']=='t')
        wo_ini_date = datetime.strptime(min(w['wo_date'] for w in workouts),"%Y-%m-%d")
        wo_end_date = datetime.strptime(max(w['wo_date'] for w in workouts),"%Y-%m-%d")
        delta = wo_end_date - wo_ini_date 
        
        print("\nSummary:")
        print(f"    Total workout sessions: {len(workouts)}")
        print(f"    Workouts per day: {round(len(workouts)/(delta.days+1),2)}")
        print(f"    Total reps: {total_reps}")
        print(f"    Total minutes: {total_mins}")
    except ValueError as e:
        print(e)
    
    pause()


def menu_mod_workout():
    # clean_con()
    print(f"\n{'='*10}{' '*2} MODIFY WORKOUT {' '*2}{'='*10}")
    print("")
    try:
        wo_id = val_wo(input("Workout ID to be modified: "))
    except ValueError as e:
        print(e)
        pause()
        return
    while True:
        print("\nWhich field would you like to change?")
        print("     1.- Workout date")
        print("     2.- Exercise")
        print("     3.- Amount type")
        print("     4.- Amount")
        print("     5.- Intensity")
        print("\n     0.- Cancel")
        opcion = input("\nSelect an option: ")
        try:
            match opcion:
                case "0":
                    return
                case "1":
                    field = "wo_date"
                    new_value = val_date(input("\nIntroduce the new date (YYYY/MM/DD): "))
                    break
                case "2":
                    field = "exercise"
                    new_value = input("\nIntroduce the new exercise: ")
                    break
                case "3":
                    field = "amount_type"
                    new_value = val_amt_tp(input("\nIntroduce the new amount type (r/t): "))
                    break
                case "4":
                    field = "amount"
                    new_value = val_amt(input("\nIntroduce the new amount: "))
                    break
                case "5":
                    field = "intensity"
                    new_value = val_intensity(input("\nIntroduce the new intensity ('Lo'/'Me'/'Hi'): "))
                    break
                case _:
                    print("Option is not valid")
                    pause()
        except ValueError as e:
            print(e)
            pause()

    mod_workout(wo_id, field, new_value)
    print("Workout has been modified successfully.")
    pause()

def menu_del_wo():
    # clean_con()
    print(f"\n{'='*10}{' '*2} DELETE WORKOUT {' '*2}{'='*10}")
    print("")
    try:
        wo_id = val_wo(input("Workout ID: "))
    except ValueError as e:
        print(e)
        pause()
        return
    
    delete_workout(wo_id)
    print(f"Workout ID {wo_id} has been removed successfully.")


def pause():
    input("\nPress ENTER to return to the main menu")

def clean_con():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_main_menu():
    clean_con()

    print("="*40)
    print(f"{"="*10}{" "*4} Welcome to {" "*4}{"="*10}")
    print(f"{"="*10}{" "*6} MATRIX {" "*6}{"="*10}")
    print("="*40)
    print("")
    print("     User functions:")
    print("     1.- Create user")
    print("     2.- View user")
    print("     3.- Modify user")
    print("     4.- Delete user")
    print("")
    print("     Workout functions:")
    print("     5.- Add workout")
    print("     6.- View workout")
    print("     7.- Delete workout")
    print("")
    print("     0.- Exit")


def main_menu():
    while True:
        show_main_menu()
        opcion = input("\nSelect an option: ")

        match opcion:
            case "0":
                print("See you soon! And don't trust anyone who says burpees are fun.")
                break
            case "1":
                menu_add_user()
            case "2":
                menu_get_user()
            case "3":
                menu_mod_user()
            case "4":
                menu_del_user()
            case "5":
                menu_add_wo()
            case "6":
                menu_get_wo()
            case "7":
                menu_mod_wo()
            case "8":
                menu_del_wo()
            case _:
                print("Please, select a valid option")
                pause()
        

if __name__ == "__main__":
    main_menu()