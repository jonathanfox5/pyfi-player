import time

import audio
import crawler
import database
import utilities as u

if __name__ == "__main__":
    p = audio.SongPlayer()
    p.play_boot_sound()
    time.sleep(2)
    p.change_album("/share/Rammstein/Mutter")
