# Utiliser une image de base légère de Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le container
WORKDIR /app

# Copier les fichiers de l'application dans le container
COPY . /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exposer le port utilisé par Flask
EXPOSE 5000

# Définir la commande par défaut pour lancer l'application
CMD ["python", "app.py"]
