import os
import subprocess
import random
import datetime

# Configurar el repositorio
REPO_DIR = "whale"  # Cambia esto si el nombre de la carpeta local es diferente
if not os.path.exists(REPO_DIR):
    print(f"❌ Error: No se encontró el directorio '{REPO_DIR}'. Clona tu repo primero.")
    exit(1)

os.chdir(REPO_DIR)  # Moverse al directorio del repositorio

# Fecha de inicio (1 de enero de 2025)
start_date = datetime.date(2025, 1, 1)
end_date = datetime.date.today()

# Mensajes de commit aleatorios
commit_messages = [
    "Refactored code for better performance 🚀",
    "Added new feature 🎉",
    "Fixed a minor bug 🐛",
    "Updated documentation 📖",
    "Improved logging system 📊",
    "Optimized database queries ⚡",
    "Refactored old functions 🔄",
    "Added unit tests ✅",
    "Implemented a new algorithm 🧠"
]

# Iterar sobre cada día desde el 1 de enero hasta hoy
current_date = start_date
while current_date <= end_date:
    num_commits = random.randint(1, 5)  # Número aleatorio de commits por día

    for _ in range(num_commits):
        log_file = "log.txt"
        with open(log_file, "a") as file:
            file.write(f"{current_date} - {random.choice(commit_messages)}\n")

        commit_time = f"{random.randint(8, 22)}:{random.randint(0, 59):02d}:00"
        commit_datetime = f"{current_date} {commit_time}"

        subprocess.run(["git", "add", log_file])
        commit_message = random.choice(commit_messages)
        subprocess.run(["git", "commit", "--date", commit_datetime, "-m", commit_message])

    print(f"✅ {num_commits} commits realizados para {current_date}")
    current_date += datetime.timedelta(days=1)  # Avanzar al siguiente día

# Push final con todos los commits
subprocess.run(["git", "push"])
print("🚀 Todos los commits han sido subidos a GitHub.")