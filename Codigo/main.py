from User_functions import add_user, get_user, delete_user
from Workout_functions import add_workout, delete_workout, get_workout, count_workouts

add_user("Alberto", 86, "Sevilla")
# delete_user(3)
# delete_user(4)

# add_workout(3, "2025-12-09", "Correr", "30", "t","Media")
print(count_workouts(1))
# add_workout(1, "2025-12-30", "Correr", "100", "r","Alta")
# delete_workout(8)
print(count_workouts(1,"2025-12-09"))
print(count_workouts(1,"2025-12-10"))

print(count_workouts(1,"2025-12-09","2025-12-22"))