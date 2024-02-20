import subprocess

# Команда для генерації ревізії
alembic_revision_command = "alembic revision --autogenerate -m 'Init'"

# Команда для оновлення бази даних
alembic_upgrade_command = "alembic upgrade head"

# Виконання першої команди
subprocess.run(alembic_revision_command, shell=True)

# Виконання другої команди
subprocess.run(alembic_upgrade_command, shell=True)
