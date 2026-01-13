from datetime import datetime
from JSON_functions import load_file, save_file
from config import get_workouts_file

def date_to_str(date):
    if date is None:
        return None
    return datetime.strftime(date, "%Y-%m-%d %H:%M")

def str_to_date(date_str):
    if date_str is None:
        return None
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M")

def add_workout(user_id,wo_date,exercise,amount,amount_type,intensity):
    workouts = load_file(get_workouts_file())
    new_id = max([w['wo_id'] for w in workouts])+1 if workouts else 1
    new_w = {'wo_id':new_id, 
            'user_id':user_id, 
            'wo_date':date_to_str(wo_date), 
            'exercise':exercise, 
            'amount':amount, 
            'amount_type':amount_type,
            'intensity':intensity}
    workouts.append(new_w)
    save_file(workouts,get_workouts_file())
    return new_w

def get_workout(get_id, user_id=None):
    workouts = load_file(get_workouts_file())
    if user_id is not None: #if user_id != None, it is a non admin user (only access to its own workouts)
        for w in workouts:
            if w['wo_id'] == get_id and w['user_id'] == user_id:
                w_ret = w
                w_ret['wo_date'] = str_to_date(w['wo_date'])
                return w_ret
    else:
        for w in workouts:
            if w['wo_id'] == get_id:
                w_ret = w
                w_ret['wo_date'] = str_to_date(w['wo_date'])
                return w_ret
    return None

def get_workout_by_user(user_id, ini_date=None, end_date=None):
    workouts = load_file(get_workouts_file())
    user_workouts = [w for w in workouts if w['user_id']==user_id]   
    
    if ini_date and not end_date:
        # Si no se especifica fecha fin se da por hecho que se quiere ver el rango desde la fecha de origen en adelante
        user_workouts = [w for w in user_workouts if str_to_date(w['wo_date'])>=ini_date]
    elif ini_date and end_date:
        user_workouts = [w for w in user_workouts if str_to_date(w['wo_date'])>=ini_date and str_to_date(w['wo_date'])<=end_date]

    for w in user_workouts:
        w['wo_date'] = str_to_date(w['wo_date'])

    user_workouts.sort(key=lambda w: w['wo_date'])
    return user_workouts

def mod_workout(mod_id, field, field_value):
    workouts = load_file(get_workouts_file())
    for w in workouts:
        if w['wo_id'] == mod_id:
            if field == "wo_date":
                w[field] = date_to_str(field_value)
            else:
                w[field]=field_value
            save_file(workouts, get_workouts_file())
            return w
    return None

def delete_workout(delete_id):
    workouts = load_file(get_workouts_file())
    workouts_f = [w for w in workouts if w['wo_id']!=delete_id]
    save_file(workouts_f,get_workouts_file())
    return

def delete_workout_by_user(user_id):
    workouts = load_file(get_workouts_file())
    workouts_f = [w for w in workouts if w['user_id']!=user_id]    
    save_file(workouts_f, get_workouts_file())
    return


def count_workouts(user_id, ini_date=None, end_date=None):
    workouts = load_file(get_workouts_file())
    user_workouts = [w for w in workouts if w['user_id']==user_id]
    if ini_date and not end_date:
        user_workouts = [w for w in user_workouts if str_to_date(w['wo_date'])>=ini_date]
    elif ini_date and end_date:
        user_workouts = [w for w in user_workouts if str_to_date(w['wo_date'])>=ini_date and str_to_date(w['wo_date'])<=end_date]
    return len(user_workouts)
    
# Validation functions

def val_datetime(date):
    if date == "":
        return datetime.now()
    
    try:
        return datetime.strptime(date, "%Y-%m-%d %H:%M")
    except ValueError:
        pass
    
    try:
        d = datetime.strptime(date, "%Y-%m-%d")
        return datetime.combine(d.date(),datetime.min.time())
    except ValueError:
        pass
    raise ValueError("ERROR: Invalid date format, use YYYY-MM-DD or YYYY-MM-DD HH:MM.")

def val_date(date, allow_fut=False):
    date_f = val_datetime(date)
    if date_f > datetime.now() and not allow_fut:
        raise ValueError("ERROR: You are trying to break space-time. Please, enter a valid date.")
    return date_f

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

def val_wo(wo_id, user_id = None):
    try:
        wo_id = int(wo_id)
    except (ValueError, TypeError):
        raise ValueError("ERROR: Workout ID must be a positive number.")
    if user_id is not None: #user_id != None when non admin user
        if get_workout(wo_id, user_id) == None:
            raise ValueError(f"ERROR: Workout ID {wo_id} does not exist for User ID {user_id}.")
    elif get_workout(wo_id) == None:
        raise ValueError(f"ERROR: Workout ID {wo_id} does not exist.")
    return wo_id