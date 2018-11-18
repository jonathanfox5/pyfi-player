import time

import audio
import crawler
import database
import utilities as u
import readrfid


def main():
    # Set up song player
    p = audio.SongPlayer()

    # Set up RFID reader
    rfid = readrfid.RFIDReader()

    # Play boot sound
    p.play_boot_sound()
    time.sleep(2)

    # Main loop, monitor RFID reader and make appropriate decisions
    try:
        while (True):
            (uid_changed, uid_string) = rfid.ReadUID()

            if uid_changed == True:
                print("UID:" + uid_string)

                if uid_string == "22198124247":
                    p.change_album("/share/music/Rammstein/Mutter")
                elif uid_string == "18518619832":
                    p.change_album("/share/music/Rick Wakeman/Criminal Record")

            time.sleep(1)

    except KeyboardInterrupt:
        print("Terminated by user")
    finally:
        rfid.CleanupGPIO()


if __name__ == "__main__":

    main()
    # dsf
