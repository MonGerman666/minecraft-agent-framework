# Minecraft Agent Framework

Aquest projecte implementa un sistema per automatitzar accions dins d'un servidor de Minecraft mitjançant bots programats amb Python. Els bots inclouen un **TNTBot** que col·loca TNT activada al voltant del jugador i un **InsultBot** que respon al xat amb insults aleatoris.

## Característiques

- **TNTBot**:
  - Gira al voltant del jugador a 15 metres d'alçada i un radi de 10 blocs.
  - Col·loca TNT activada que explota automàticament.
  - Es pot activar amb la comanda `!tnt` i aturar amb `!stop`.

- **InsultBot**:
  - Escolta el xat i respon amb insults aleatoris.
  - Es pot activar amb la comanda `!insult` i aturar amb `!stop`.

## Requisits previs

Abans de començar, assegura’t que tens instal·lats els següents programes i biblioteques:

1. **Python 3.8 o superior**
2. **Git**
3. Biblioteca `mcpi` per a la comunicació amb el servidor de Minecraft.

## Instal·lació

1. **Clona aquest repositori:**
   ```bash
   git clone https://github.com/MonGerman666/minecraft-agent-framework.git
   cd minecraft-agent-framework
Instal·la les dependències: El projecte utilitza la biblioteca mcpi. Si no la tens instal·lada:

bash
Copiar código
pip install mcpi
Configura el servidor de Minecraft:

Configura un servidor de Minecraft Pi Edition o un servidor compatible.
Assegura’t que està actiu abans d'executar el projecte.
Ús
Executa el fitxer principal: Navega al directori del projecte i executa:

bash
Copiar código
python main.py
Activa els bots des del xat del servidor:

Escriu !insult per activar el InsultBot.
Escriu !tnt per activar el TNTBot.
Escriu !stop per aturar tots els bots.
Estructura del projecte
bash
Copiar código
minecraft-agent-framework/
├── agents/
│   ├── __init__.py       # Importa els bots
│   ├── insult_bot.py     # Bot d'insults
│   ├── tnt_bot.py        # Bot de TNT
├── mcpi/                 # Biblioteca per interactuar amb Minecraft
├── main.py               # Punt d'entrada del programa
└── README.md             # Documentació del projecte
Contribució
Les contribucions són benvingudes! Si vols afegir funcionalitats o corregir errors:

Fes un fork del repositori.
Crea una branca per a la teva funcionalitat (git checkout -b nova-funcionalitat).
Fes els teus canvis i crea un commit (git commit -m "Descripció dels canvis").
Fes un push de la branca (git push origin nova-funcionalitat).
Obre un pull request.
