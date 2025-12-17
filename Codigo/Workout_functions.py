from datetime import datetime
from JSON_functions import load_file, save_file
from config import WORKOUTS_FILE


def add_workout(user_id,wo_date,exercise,amount,amount_type,intensity):
    workouts = load_file(WORKOUTS_FILE)
    new_id = max([w['wo_id'] for w in workouts])+1 if workouts else 1
    new_w = {'wo_id':new_id, 
            'user_id':user_id, 
            'wo_date':wo_date, 
            'exercise':exercise, 
            'amount':amount, 
            'amount_type':amount_type,
            'intensity':intensity}
    workouts.append(new_w)
    save_file(workouts,WORKOUTS_FILE)
    return new_w

def get_workout(get_id):
    workouts = load_file(WORKOUTS_FILE)
    for w in workouts:
        if w['wo_id'] == get_id:
            return w
    return None


def get_workout_by_user(user_id, ini_date=None, end_date=None):
    workouts = load_file(WORKOUTS_FILE)
    user_workouts = [w for w in workouts if w['user_id']==user_id]   
    
    if ini_date and not end_date:
        user_workouts = [w for w in user_workouts if w['wo_date']==ini_date]
    elif ini_date and end_date:
        user_workouts = [w for w in user_workouts if w['wo_date']>=ini_date and w['wo_date']<=end_date]
    return user_workouts

def delete_workout(delete_id):
    workouts = load_file(WORKOUTS_FILE)
    workouts_f = [w for w in workouts if w['wo_id']!=delete_id]
    save_file(workouts_f,WORKOUTS_FILE)
    return

def delete_workout_by_user(user_id):
    workouts = load_file(WORKOUTS_FILE)
    workouts_f = [w for w in workouts if w['user_id']!=user_id]    
    save_file(workouts_f, WORKOUTS_FILE)
    return


def count_workouts(user_id, ini_date=None, end_date=None):
    workouts = load_file(WORKOUTS_FILE)
    user_workouts = [w for w in workouts if w['user_id']==user_id]
    if ini_date and not end_date:
        user_workouts = [w for w in user_workouts if w['wo_date']==ini_date]
    elif ini_date and end_date:
        user_workouts = [w for w in user_workouts if w['wo_date']>=ini_date and w['wo_date']<=end_date]
    return len(user_workouts)
    
# Validation functions

def val_date(date, allow_fut=False):
    try:
        date_f = datetime.strptime(date,"%Y-%m-%d")
    except ValueError:
        raise ValueError("ERROR: Invalid date format, use YYYY-MM-DD.")
    if date_f > datetime.now() and not allow_fut:
        raise ValueError("ERROR: You are trying to break space-time. Please, enter a valid date.")
    return date

def val_amt(amt):
    try:
        amt = int(amt)
    except (ValueError, TypeError):
        raise ValueError("ERROR: Amount must be a positive number.")
    if amt <= 0:
        raise ValueError("ERROR: Amount must be a positive number.")
    return amt

def val_amt_tp(amount_type):
    if amount_type not in ["t","r"]:
        raise ValueError("ERROR: Amount type must be 'r' (reps) or 't' (time).")
    return amount_type

def val_intensity(intensity):
    if intensity not in ["Lo","Me","Hi"]:
        raise ValueError("ERROR: Intensity must be 'Lo', 'Me', 'Hi'.")
    return intensity

def val_wo(wo_id):
    try:
        wo_id = int(wo_id)
    except (ValueError, TypeError):
        raise ValueError("ERROR: Workout ID must be a positive number.")
    if get_workout(wo_id) == None:
        raise ValueError(f"ERROR: Workout ID {wo_id} does not exist.")
    return wo_id