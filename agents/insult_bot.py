import random
import time

class InsultBot:
    def __init__(self, mc):
        self.mc = mc
        self.active = False
        self.insults = [
            "Ets més lent que un cargol!",
            "Quina construcció més lletja!",
            "No tens estil!",
            "He vist zombies amb més gràcia que tu!",
            "Ets tan dolent que els creepers no volen explotar al teu costat!",
            "Si fossis un mob, series un porquet perdut.",
            "El teu inventari és ple de caos, com tu!",
            "La teva casa sembla feta per un noob somnolent.",
            "Els villagers et miren i volen emigrar!",
            "Les ovelles es despentenen només de veure't!",
        ]

    def listen_and_respond(self):
        """Escolta el xat i respon amb insults."""
        self.active = True
        try:
            while self.active:
                chat_events = self.mc.events.pollChatPosts()
                if not chat_events:
                    time.sleep(1)  # Espera abans de revisar de nou
                    continue
                for event in chat_events:
                    insult = random.choice(self.insults)
                    self.mc.postToChat(insult)
                time.sleep(3)  # Pausa entre insults
        except Exception as e:
            print(f"Error al bot d'insults: {e}")
        finally:
            self.active = False  # Reinicia l'estat quan s'atura

    def stop(self):
        """Atura el bot."""
        self.active = False
