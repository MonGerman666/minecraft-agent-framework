from mcpi.minecraft import Minecraft
from threading import Thread
from agents.tnt_bot import TNTBot
from agents.insult_bot import InsultBot
import time

# Connecta al servidor de Minecraft
mc = Minecraft.create()

# Inicialitza els bots
tnt_bot = TNTBot(mc)
insult_bot = InsultBot(mc)

# Registre per evitar duplicats
last_message = None

def listen_for_commands():
    """Escolta el xat i activa els bots segons les comandes."""
    global last_message
    while True:
        try:
            chat_events = mc.events.pollChatPosts()
            for event in chat_events:
                message = event.message.lower()
                if message == last_message:
                    continue  # Evita duplicats
                last_message = message

                # Activa el bot d'insults
                if message == "!insult":
                    if not insult_bot.active:
                        mc.postToChat("Activant InsultBot!")
                        insult_thread = Thread(target=insult_bot.listen_and_respond)
                        insult_thread.start()
                    else:
                        mc.postToChat("InsultBot ja està actiu!")

                # Activa el bot TNT
                elif message == "!tnt":
                    if not tnt_bot.active:
                        mc.postToChat("Activant TNTBot!")
                        tnt_thread = Thread(target=tnt_bot.circle_around_player)
                        tnt_thread.start()
                    else:
                        mc.postToChat("TNTBot ja està actiu!")

                # Atura tots els bots
                elif message == "!stop":
                    mc.postToChat("Aturant tots els bots.")
                    insult_bot.stop()
                    tnt_bot.stop()
        except Exception as e:
            print(f"Error escoltant comandes: {e}")
        time.sleep(1)

# Executa la funció d'escolta de comandes en un fil separat
command_thread = Thread(target=listen_for_commands)
command_thread.start()

# Manté el programa actiu
command_thread.join()
