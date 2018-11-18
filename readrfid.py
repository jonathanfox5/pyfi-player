import RPi.GPIO as GPIO
import mfrc522driver as MFRC522


class RFIDReader():
    def __init__(self):
        # Create an object of the class MFRC522
        self.MIFAREReader = MFRC522.MFRC522()
        self.last_uid = None

    def ReadUID(self):
        # Scan for cards
        (status, TagType) = self.MIFAREReader.MFRC522_Request(
            self.MIFAREReader.PICC_REQIDL)

        # Get the UID of the card
        (status, uid) = self.MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        uid_changed = False
        uid_string = None
        if status == self.MIFAREReader.MI_OK:

            # Get UID
            uid_string = str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3])
            if uid_string != self.last_uid:
                uid_changed = True
                self.last_uid = uid_string

        packet = (uid_changed, uid_string)

        return packet

    def CleanupGPIO(self):
        GPIO.cleanup()