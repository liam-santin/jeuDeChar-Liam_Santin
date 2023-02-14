import brickpi3
import time

BP = brickpi3.BrickPi3()


def chariot(vitesse):
    BP.set_motor_power(BP.PORT_A,vitesse)

def pont(vitesse):
    BP.set_motor_power(BP.PORT_D,vitesse)

def pince(vitesse):
    BP.set_motor_power(BP.PORT_C,vitesse)

def elevateur(vitesse):
        BP.set_motor_power(BP.PORT_B, vitesse)



def fermerPince():
    statusMoteur = 1
    while statusMoteur != 0:
        pince(-30)
        time.sleep(0.1)
        statusMoteur = BP.get_motor_status(BP.PORT_C)[3]
        print(statusMoteur)
    print("pression OK")
    pince(20)
    time.sleep(0.20)
    pince(0)

def ouvrirPince():
    pince(40)
    time.sleep(1.5)
    pince(0)

# prend un jeton à partir de la pince deja ouverte en bas

def descendreElevateur():
    elevateur(20)
    time.sleep(4.3)
    elevateur(0)

def calibrePince():
    statusMoteur = 1
    while statusMoteur != 0:
        pince(-40)
        time.sleep(0.1)
        statusMoteur = BP.get_motor_status(BP.PORT_C)[3]
        print(statusMoteur)
    pince(30)
    time.sleep(2)
    pince(0)

def calibreElevateur():
    statusMoteur = 1
    while statusMoteur != 0:
        elevateur(-20)
        time.sleep(0.1)
        statusMoteur = BP.get_motor_status(BP.PORT_B)[3]
        print(statusMoteur)
    elevateur(20)
    time.sleep(1)
    elevateur(0)

def calibrePont(temps):
    pont(50)
    time.sleep(temps)
    pont(0)
    statusMoteur = 221
    while statusMoteur > 220 :
        pont(20)
        time.sleep(0.2)
        statusMoteur = BP.get_motor_status(BP.PORT_D)[3]
        print(statusMoteur)
    pont(-20)
    time.sleep(0.5)
    pont(0)

def calibreJetonPince():
    ouvrirPince()
    calibreElevateur()
    descendreElevateur()

def prendreJeton():
    calibreElevateur()
    calibrePince()
    descendreElevateur()
    fermerPince()
    calibreElevateur()

def allMotor(vitesse):
    chariot(vitesse)
    pont(vitesse)
    pince(vitesse)
    elevateur(vitesse)
