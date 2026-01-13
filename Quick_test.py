# import os
# from User_functions import add_user, get_user, delete_user, val_user, val_age
# from datetime import datetime
# from Workout_functions import add_workout, delete_workout, get_workout, count_workouts

# add_user("Alberto", 86, "Sevilla")
# delete_user(3)
# delete_user(4)

# add_workout(3, "2025-12-09", "Correr", "30", "t","Media")
# print(count_workouts(1))
# add_workout(1, "2025-12-30", "Correr", "100", "r","Alta")
# delete_workout(8)
# print(count_workouts(1,"2025-12-09"))
# print(count_workouts(1,"2025-12-10"))

# print(count_workouts(1,"2025-12-09","2025-12-22"))

# print(datetime.now())

# import os

# path = "C:/Users/Fiuter/iCloudDrive/iCloud~com~omz-software~Pythonista3/Matrix/JSON"

# print("Existe:", os.path.exists(path))
# print("Contenido:", os.listdir(path))

from datetime import datetime
import json
import os

# Rutas de los archivos
files_to_update = [
    r"c:\Users\Fiuter\iCloudDrive\iCloud~com~omz-software~Pythonista3\Matrix\JSON\workouts_prod.json",
    r"c:\Users\Fiuter\iCloudDrive\iCloud~com~omz-software~Pythonista3\Matrix\JSON\workouts_dev.json"
]

for file_path in files_to_update:
    if not os.path.exists(file_path):
        print(f"✗ Archivo no encontrado: {file_path}")
        continue
    
    # Cargar el JSON
    with open(file_path, 'r', encoding='utf-8') as f:
        workouts = json.load(f)
    
    print(f"\nActualizando: {file_path}")
    
    # Actualizar cada fecha
    for workout in workouts:
        try:
            # Parsear la fecha antigua (YYYY-MM-DD)
            date_obj = datetime.strptime(workout['wo_date'], "%Y-%m-%d")
            # Convertir a nuevo formato sin segundos (YYYY-MM-DD HH:MM)
            workout['wo_date'] = date_obj.strftime("%Y-%m-%d 00:00")
            print(f"  ✓ Workout ID {workout['wo_id']}: {workout['wo_date']}")
        except ValueError as e:
            print(f"  ✗ Error en Workout ID {workout['wo_id']}: {e}")
    
    # Guardar el archivo actualizado
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(workouts, f, indent=2, ensure_ascii=False)
    
    print(f"  ✓ Archivo actualizado correctamente.")

print("\n✓ Todos los archivos han sido actualizados.")