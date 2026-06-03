# Hvilken version eller hvilket python image skil vi bruge?
FROM python:3.14-slim

# Angiv arbejds directory
WORKDIR /app

# Kopier alle filler fra
COPY . .
# COPY HelloWorld.py .

# kør scriptet, når docker container starter
CMD ["python", "HelloWorld.py"]