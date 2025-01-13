#!/bin/bash

echo "==============================="
echo " Minecraft Agent Framework"
echo "==============================="

echo "
Aquest projecte implementa un sistema per automatitzar accions dins d'un servidor de Minecraft mitjançant bots programats amb Python. Els bots inclouen un TNTBot que col·loca TNT activada al voltant del jugador i un InsultBot que respon al xat amb insults aleatoris.
"

echo "
## Característiques
- TNTBot:
  - Gira al voltant del jugador a 15 metres d'alçada i un radi de 10 blocs.
  - Col·loca TNT activada que explota automàticament.
  - Es pot activar amb la comanda !tnt i aturar amb !stop.
- InsultBot:
  - Escolta el xat i respon amb insults aleatoris.
  - Es pot activar amb la comanda !insult i aturar amb !stop.
"

echo "
## Requisits previs
Abans de començar, assegura’t que tens instal·lats els següents programes i biblioteques:
1. Python 3.8 o superior
2. Git
3. Biblioteca mcpi per a la comunicació amb el servidor de Minecraft.
"

echo "
## Instal·lació
1. Clona aquest repositori:
   git clone https://github.com/MonGerman666/minecraft-agent-framework.git
   cd minecraft-agent-framework
2. Instal·la les dependències:
   pip install mcpi
3. Configura el servidor de Minecraft:
   - Configura un servidor de Minecraft Pi Edition o un servidor compatible.
   - Assegura’t que està actiu abans d'executar el projecte.
"

echo "
## Ús
1. Executa el fitxer principal:
   python main.py
2. Activa els bots des del xat del servidor:
   - Escriu !insult per activar el InsultBot.
   - Escriu !tnt per activar el TNTBot.
   - Escriu !stop per aturar tots els bots.
"

echo "
## Estructura del projecte
minecraft-agent-framework/
├── agents/
│   ├── __init__.py       # Importa els bots
│   ├── insult_bot.py     # Bot d'insults
│   ├── tnt_bot.py        # Bot de TNT
├── mcpi/                 # Biblioteca per interactuar amb Minecraft
├── main.py               # Punt d'entrada del programa
└── README.md             # Documentació del projecte
"

echo "
## Contribució
Les contribucions són benvingudes! Si vols afegir funcionalitats o corregir errors:
1. Fes un fork del repositori.
2. Crea una branca per a la teva funcionalitat:
   git checkout -b nova-funcionalitat
3. Fes els teus canvis i crea un commit:
   git commit -m 'Descripció dels canvis'
4. Fes un push de la branca:
   git push origin nova-funcionalitat
5. Obre un pull request.
"

echo "
## Llicència
Aquest projecte està sota la llicència MIT. Consulta el fitxer LICENSE per a més detalls.
"

