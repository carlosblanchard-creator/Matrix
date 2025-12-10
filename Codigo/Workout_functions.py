from datetime import datetime
from JSON_functions import load_file, save_file
from User_functions import get_user, val_user

File_name = "workouts.json"

def add_workout(user_id,wo_date,exercise,amount,amount_type,intensity):
    
    workouts = load_file(File_name)
    new_id = max([w['wo_id'] for w in workouts])+1 if workouts else 1
    try:
        new_w = {'wo_id':new_id, 
                 'user_id':val_user(user_id), 
                 'wo_date':val_date(wo_date), 
                 'exercise':exercise, 
                 'amount':amount, 
                 'amount_type':val_amt_tp(amount_type),
                 'intensity':val_intensity(intensity)}
    except ValueError as e:
        print(e)
        return None

    workouts.append(new_w)
    save_file(workouts,File_name)

    print(f"New workout logged --> Workout ID: {new_w['wo_id']} | User ID: {new_w['user_id']} | Date: {new_w['wo_date']} | Exercise: {new_w['exercise']} | {new_w['amount']} {"min" if new_w['amount_type'] == "t" else "repeticiones"} | Intensity:  {new_w['intensity']}")

    return new_w

def get_workout(get_id):
    workouts = load_file(File_name)
    for w in workouts:
        if w['wo_id'] == get_id:
            return w
    return None

def delete_workout(delete_id):

        workouts = load_file(File_name)
        try:
            workouts_f = [w for w in workouts if w['wo_id']!=val_wo(delete_id)]
        except ValueError as e:
            print(e)
            return False
        
        save_file(workouts_f,File_name)

        print(f"Workout ID {delete_id} was deleted successfully.")
        return True

def count_workouts(user_id, ini_date=None, end_date=None):
    workouts = load_file(File_name)
    try:
        user_workouts = [w for w in workouts if w['user_id']==val_user(user_id)]
        if ini_date and not end_date:
            user_workouts = [w for w in user_workouts if w['wo_date']==val_date(ini_date)]
        elif ini_date and end_date:
            user_workouts = [w for w in user_workouts if w['wo_date']>=val_date(ini_date) and w['wo_date']<=val_date(end_date, True)]
        return len(user_workouts)
    except ValueError as e:
        print(e)
        return 0
    
# Validation functions

def val_date(date, allow_fut=False):
    try:
        date_f = datetime.strptime(date,"%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format, use YYYY-MM-DD.")
    if date_f > datetime.now() and not allow_fut:
        raise ValueError("You are trying to break space-time. Please, enter a valid date.")
    return date

def val_amt_tp(amount_type):
    if amount_type not in ["t","r"]:
        raise ValueError("Amount type must be 'r' (reps) or 't' (time).")
    return amount_type

def val_intensity(intensity):
    if intensity not in ["Lo","Me","Hi"]:
        raise ValueError("Intensity must be 'Lo', 'Me', 'Hi'.")
    return intensity

def val_wo(wo_id):
    if get_workout(wo_id) == None:
        raise ValueError(f"User {wo_id} does not exist.")
    return wo_id