from JSON_functions import load_file, save_file

File_name = 'workouts.json'

def add_workout(user_id,wo_date,exercise,amount,amount_type,intensity):
    workouts = load_file()
    new_id = max([w['wo_id'] for w in workouts])+1 if workouts else 1
    new_w = {'wo_id':new_id, 'user_id':user_id, 'wo_date':wo_date, 'excercise':exercise, 'amount':amount, 'amount_type':amount_type,'intensity':intensity}

    workouts.append(new_w)
    save_file(workouts)

    print(f'New workout logged at {new_w[wo_date]}: {new_w[exercise]}')