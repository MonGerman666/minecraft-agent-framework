from mcpi import block # type: ignore
import math
import time

class TNTBot:
    def __init__(self, mc):
        self.mc = mc
        self.active = False

    def circle_around_player(self, radius=10, height=15, delay=3):
        """Gira al voltant del jugador i deixa caure TNT activada."""
        self.active = True
        angle = 0
        try:
            while self.active:
                pos = self.get_player_position()
                if pos is None:
                    time.sleep(1)  # Espera i torna a intentar
                    continue

                # Calcula la posició
                x = pos.x + int(radius * math.cos(math.radians(angle)))
                z = pos.z + int(radius * math.sin(math.radians(angle)))
                y = pos.y + height

                # Col·loca TNT i activa-la amb foc
                self.mc.setBlock(x, y, z, block.TNT.id)      # Col·loca TNT
                self.mc.setBlock(x, y - 1, z, block.FIRE.id)  # Activa la TNT amb foc

                # Incrementa l'angle
                angle += 10
                if angle >= 360:
                    angle = 0

                time.sleep(delay)
        except Exception as e:
            print(f"Error al bot TNT: {e}")
        finally:
            self.active = False  # Reinicia l'estat quan s'atura

    def get_player_position(self):
        """Obtén la posició del jugador amb reintents."""
        for attempt in range(5):  # Reintenta fins a 5 vegades
            try:
                pos = self.mc.player.getTilePos()
                print(f"Resposta del servidor: {pos}")  # Depuració
                if pos and all(isinstance(coord, int) for coord in (pos.x, pos.y, pos.z)):
                    return pos
                print("Resposta no vàlida. Tornant a intentar...")
                time.sleep(1)  # Pausa abans de reintentar
            except Exception as e:
                print(f"Error obtenint la posició del jugador: {e}")
        print("No s'ha pogut obtenir la posició del jugador.")
        return None

    def stop(self):
        """Atura el bot."""
        self.active = False
