import os
from datetime import datetime
from User_functions import add_user, get_user, delete_user, val_user, val_age
from Workout_functions import add_workout, delete_workout, get_workout, get_workout_by_user, count_workouts, delete_workout_by_user, val_date, val_amt_tp, val_intensity, val_wo, val_amt

def menu_add_user():
    # clean_con()
    print(f"\n{'='*10}{' '*5} ADD USER {' '*5}{'='*10}")
    print("")
    
    try:
        name = input("Name: ")
        age = val_age(input("Age: "))
        city = input("City: ")
        new_user = add_user(name, age,city)

        print(f"New user, {new_user['name']}, added successfully with ID {new_user['user_id']}")
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
        wo_date = val_date(input("Workout date: "))
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
        wo_ini_date = input("From date (optional, YYYY-MM-DD): ").strip() or None
        wo_end_date = None
        if wo_ini_date:
            wo_ini_date = val_date(wo_ini_date)
            wo_end_date = input("To date (optional, YYYY-MM-DD): ").strip() or None
        if wo_end_date:
            wo_end_date = val_date(wo_end_date, True)
        
        workouts = get_workout_by_user(user_id,wo_ini_date,wo_end_date)
        for w in workouts:
            print(f"Workout ID: {w['wo_id']} | User ID: {w['user_id']} | Date: {w['wo_date']} | Exercise: {w['exercise']} | {w['amount']} {'min' if w['amount_type'] == 't' else 'repeticiones'} | Intensity:  {w['intensity']}")
        
        total_reps = sum(int(w['amount']) for w in workouts if w['amount_type']=='r')
        total_mins = sum(int(w['amount']) for w in workouts if w['amount_type']=='t')
        wo_ini_date = datetime.strptime(min(w['wo_date'] for w in workouts),"%Y-%m-%d")
        wo_end_date = datetime.strptime(max(w['wo_date'] for w in workouts),"%Y-%m-%d")
        delta = wo_end_date - wo_ini_date
        print(delta)
        print("\nSummary:")
        print(f"    Total workout sessions: {len(workouts)}")
        print(f"    Workouts per day: {round(len(workouts)/delta.days,2) if delta.days>0 else 0}")
        print(f"    Total reps: {total_reps}")
        print(f"    Total minutes: {total_mins}")
    except ValueError as e:
        print(e)
    
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

# def menu_count_wo():


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
    print("     3.- Delete user")
    print("")
    print("     Workout functions:")
    print("     4.- Add workout")
    print("     5.- View workout")
    print("     6.- Delete workout")
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
        

if __name__ == "__main__":
    main_menu()