import brickpi3
import time
from motor import chariot
from motor import pont
from motor import calibrePont
from motor import prendreJeton
from motor import descendreElevateur
from motor import ouvrirPince

# depuis la position de calibrage du pont jusqu'a une position
# de jeton
PONT_TO_A = 2
PONT_TO_B = 3.1
PONT_TO_C = 4.3
PONT_TO_D = 5.3
PONT_TO_E = 6
PONT_TO_F = 7
PONT_TO_G = 8.3

# depuis la position d'un jeton jusqu'a la positon de calibrage
# du pont
CALIBRAGE_PONT_POS_A = 1
CALIBRAGE_PONT_POS_B = 1.8
CALIBRAGE_PONT_POS_C = 2.4
CALIBRAGE_PONT_POS_D = 3.5
CALIBRAGE_PONT_POS_E = 4
CALIBRAGE_PONT_POS_F = 5
CALIBRAGE_PONT_POS_G = 6



BP = brickpi3.BrickPi3()

def A1():
    pont(-40)
    time.sleep(PONT_TO_A)
    pont(0)
    chariotToutaGauche()

def A2():
    pont(-40)
    time.sleep(PONT_TO_A)
    pont(0)
    chariotAuMilieu()

def A3():
    pont(-40)
    time.sleep(PONT_TO_A)
    pont(0)
    chariotToutaDroite()


def B1():
    pont(-40)
    time.sleep(PONT_TO_B)
    pont(0)
    chariotToutaGauche()
    chariot(-20)
    time.sleep(0.5)
    chariot(0)

def B2():
    pont(-40)
    time.sleep(PONT_TO_B)
    pont(0)
    chariotAuMilieu()

def B3():
    pont(-40)
    time.sleep(PONT_TO_B)
    pont(0)
    chariotToutaDroite()
    chariot(20)
    time.sleep(0.5)
    chariot(0)

def C1():
    pont(-40)
    time.sleep(PONT_TO_C)
    pont(0)
    chariotToutaGauche()
    chariot(-20)
    time.sleep(1)
    chariot(0)

def C2():
    pont(-40)
    time.sleep(PONT_TO_C)
    pont(0)
    chariotAuMilieu()

def C3():
    pont(-40)
    time.sleep(PONT_TO_C)
    pont(0)
    chariotToutaDroite()
    chariot(20)
    time.sleep(1.1)
    chariot(0)

def D1():
    pont(-40)
    time.sleep(PONT_TO_D)
    pont(0)
    chariotToutaGauche()

def D2():
    pont(-40)
    time.sleep(PONT_TO_D)
    pont(0)
    chariotToutaGauche()
    chariot(-20)
    time.sleep(0.5)
    chariot(0)

def D3():
    pont(-40)
    time.sleep(PONT_TO_D)
    pont(0)
    chariotToutaGauche()
    chariot(-20)
    time.sleep(1)
    chariot(0)

def D4():
    pont(-40)
    time.sleep(PONT_TO_D)
    pont(0)
    chariotToutaDroite()
    chariot(20)
    time.sleep(1)
    chariot(0)

def D5():
    pont(-40)
    time.sleep(PONT_TO_D)
    pont(0)
    chariotToutaDroite()
    chariot(20)
    time.sleep(0.5)
    chariot(0)

def D6():
    pont(-40)
    time.sleep(PONT_TO_D)
    pont(0)
    chariotToutaDroite()

def E1():
    pont(-40)
    time.sleep(PONT_TO_E)
    pont(0)
    chariotToutaGauche()
    chariot(-20)
    time.sleep(1)
    chariot(0)

def E2():
    pont(-40)
    time.sleep(PONT_TO_E)
    pont(0)
    chariotAuMilieu()

def E3():
    pont(-40)
    time.sleep(PONT_TO_E)
    pont(0)
    chariotToutaDroite()
    chariot(20)
    time.sleep(1.1)
    chariot(0)

def F1():
    pont(-40)
    time.sleep(PONT_TO_F)
    pont(0)
    chariot(-20)
    time.sleep(0.5)
    chariot(0)

def F2():
    pont(-40)
    time.sleep(PONT_TO_F)
    pont(0)
    chariotAuMilieu()

def F3():
    pont(-40)
    time.sleep(PONT_TO_F)
    pont(0)
    chariot(20)
    time.sleep(0.5)
    chariot(0)


def G1():
    pont(-40)
    time.sleep(PONT_TO_G)
    pont(0)
    chariotToutaGauche()

def G2():
    pont(-40)
    time.sleep(PONT_TO_G)
    pont(0)

def G3():
    pont(-40)
    time.sleep(PONT_TO_G)
    pont(0)
    chariotToutaDroite()

def allerLigneF():
    calibrePont()
    pont(-60)
    time.sleep(5.45)
    pont(0)


def F2toD1():
    calibrePont()
    allerLigneF()
    chariotAuMilieu()
    prendreJeton()

def chariotToutaDroite():
    statusMoteur = 1
    while statusMoteur != 0:
        chariot(-7.5)
        time.sleep(0.1)
        statusMoteur = BP.get_motor_status(BP.PORT_A)[3]
        print(statusMoteur)
    chariot(20)
    time.sleep(0.1)
    chariot(0)


def chariotAuMilieu():
    statusMoteur = 1
    while statusMoteur != 0:
        chariot(-7.5)
        time.sleep(0.1)
        statusMoteur = BP.get_motor_status(BP.PORT_A)[3]
        print(statusMoteur)
    chariot(20)
    time.sleep(1.6)
    chariot(0)


def chariotToutaGauche():
    statusMoteur = 1
    while statusMoteur != 0:
        chariot(7.5)
        time.sleep(0.1)
        statusMoteur = BP.get_motor_status(BP.PORT_A)[3]
        print(statusMoteur)
    chariot(0)
    print('calibrage ok')


def G2toE1():
    calibrePont(CALIBRAGE_PONT_POS_D)
    G2()
    chariotAuMilieu()
    prendreJeton()
    pont(40)
    time.sleep(3)
    pont(0)
    chariotToutaGauche()
    descendreElevateur()
    ouvrirPince()