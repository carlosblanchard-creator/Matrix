import os
from User_functions import add_user, get_user, delete_user, val_user, val_age
from Workout_functions import add_workout, delete_workout, get_workout, count_workouts, delete_workout_by_user, val_date, val_amt_tp, val_intensity, val_wo, val_amt

def menu_add_user():
    # clean_con()
    print(f"\n{'='*10}{' '*5} ADD USER {' '*5}{'='*10}")
    print("")
    name = input("Name: ")
    age = input("Age: ")
    city = input("City: ")

    try:
        new_user = add_user(name, val_age(age),city)
    except ValueError as e:
        print(e)

    print(f"New user, {new_user['name']}, added successfully with ID {new_user['user_id']}")
    pause()

def menu_get_user():
    # clean_con()
    print(f"\n{'='*10}{' '*5} GET USER {' '*5}{'='*10}")
    print("")
    user_id = input("User ID: ")
    
    try:
        user = get_user(val_user(user_id))
        print(f"Name: {user['name']}\nAge: {user['age']}\nCity: {user['city']}")
    except ValueError as e:
        print(e)
    
    pause()
    
def menu_del_user():
    # clean_con()
    print(f"\n{'='*10}{' '*4} DELETE USER {' '*3}{'='*10}")
    print("")
    user_id = input("User ID: ")

    try:
        uid = val_user(user_id)
    except ValueError as e:
        print(e)
        pause()
        return

    # Delete all the workouts related to the User ID that is going to be deleted
    x=count_workouts(uid)
    delete_workout_by_user(uid)
    if x==0:
        print(f"No workouts found for User ID {uid}")
    else:
        print(f"{x} workout logs have been removed successfully from User ID {uid}")

    # Delete user
    delete_user(uid)
    print(f"User ID {uid} was deleted successfully.")
    pause()

def menu_add_wo():
    # clean_con()
    print(f"\n{'='*10}{' '*4} ADD WORKOUT {' '*3}{'='*10}")
    print("")
    user_id = input("User ID: ")
    wo_date = input("Workout date: ")
    exercise = input("Exercise: ")
    amount_type = input("Amount type 'r' (reps) / 't' (time): ")
    amount = input("Amount: ")
    intensity = input("Intensity 'Lo'/'Me'/'Hi': ")

    try:
        new_wo = add_workout(val_user(user_id),val_date(wo_date),exercise,val_amt(amount),val_amt_tp(amount_type),val_intensity(intensity))
    except ValueError as e:
        print(e)

    print(f"New workout logged --> Workout ID: {new_wo['wo_id']} | User ID: {new_wo['user_id']} | Date: {new_wo['wo_date']} | Exercise: {new_wo['exercise']} | {new_wo['amount']} {'min' if new_wo['amount_type'] == 't' else 'repeticiones'} | Intensity:  {new_wo['intensity']}")

    pause()


# def menu_get_wo():

# def menu_del_wo():

# def menu_count_wo():


def pause():
    input("\nPress ENTER to return to the main manu")

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
    print("     3.- Delete user")
    print("")
    print("     Workout functions:")
    print("     4.- Add workout")
    print("     5.- View workout")
    print("     6.- Delete workout")
    print("     7.- Count workouts")
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
                menu_del_user()
            case "4":
                menu_add_wo()
            case "5":
                menu_get_wo()
            case "6":
                menu_del_wo()
            case "7":
                menu_count_wo()
        

if __name__ == "__main__":
    main_menu()