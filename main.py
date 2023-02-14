import os
import brickpi3
import cv2
import time

import matplotlib.pyplot as plt
import picamera2
import threading
import numpy as np



BP = brickpi3.BrickPi3()
picam2 = picamera2.Picamera2()

BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.TOUCH)

listePosition = []


def detectCouleurJeton(a,b, img):
    x = a
    y = b
    (r, g, b) = img[y, x]
    print("Couleur du pixel ({}, {}) : {}".format(x, y, r, g, b))

    if r < 80 and g < 80 and b < 80:
        return False
    else:
        return True


def cercle(a, b, img, r, position):
    img = cv2.circle(img, (a, b), r, (0, 255, 0), 5)
    couleur = detectCouleurJeton(a, b, img)
    print(position)
    listePosition.append((position, couleur))


def dessin(nbrCercle):
    camera_config = picam2.create_still_configuration(main={"size": (3280, 2464)}, lores={"size": (1968, 1478)},
                                                      display="lores")
    picam2.configure(camera_config)
    picam2.start()
    time.sleep(1)
    listePosition = [""]
    while True:
        nombreTourActuel = 0
        listePosition = []

        img = picam2.capture_array("main")

        # Convert to grayscale.
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Blur using 3 * 3 kernel.
        gray_blurred = cv2.blur(gray, (3, 3))

        plt.imshow(gray_blurred)
        plt.show()

        # Apply Hough transform on the blurred image.
        detected_circles = cv2.HoughCircles(gray_blurred,
                                            cv2.HOUGH_GRADIENT, 4, 60, param1=52,
                                            param2=65, minRadius=75, maxRadius=77)

        # Convert the circle parameters a, b and r to integers.
        if detected_circles is not None:
            detected_circles = np.uint16(np.around(detected_circles))
            for pt in detected_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]

                if 2540 > a > 2260 and 345 > b > 105:
                    cercle(a, b, img, r, "G1")
                    nombreTourActuel += 1

                elif 1660 > a > 1410 and 375 > b > 135:
                    cercle(a, b, img, r, "G2")
                    nombreTourActuel += 1

                elif 770 > a > 510 and 440 > b > 180:
                    cercle(a, b, img, r, "G3")
                    nombreTourActuel += 1

                elif 2200 > a > 1990 and 690 > b > 420:
                    cercle(a, b, img, r, "F1")
                    nombreTourActuel += 1

                elif 1655 > a > 1420 and 710 > b > 470:
                    cercle(a, b, img, r, "F2")
                    nombreTourActuel += 1

                elif 1110 > a > 840 and 730 > b > 470:
                    cercle(a, b, img, r, "F3")
                    nombreTourActuel += 1

                elif 1900 > a > 1660 and 1010 > b > 770:
                    cercle(a, b, img, r, "E1")
                    nombreTourActuel += 1

                elif 1670 > a > 1410 and 1030 > b > 790:
                    cercle(a, b, img, r, "E2")
                    nombreTourActuel += 1

                elif 1430 > a > 1190 and 1040 > b > 800:
                    cercle(a, b, img, r, "E3")
                    nombreTourActuel += 1

                elif 2580 > a > 2300 and 1290 > b > 940:
                    cercle(a, b, img, r, "D1")
                    nombreTourActuel += 1

                elif 2250 > a > 2000 and 1270 > b > 950:
                    cercle(a, b, img, r, "D2")
                    nombreTourActuel += 1

                elif 1940 > a > 1685 and 1270 > b > 950:
                    cercle(a, b, img, r, "D3")
                    nombreTourActuel += 1

                elif 1470 > a > 1210 and 1270 > b > 1000:
                    cercle(a, b, img, r, "D4")
                    nombreTourActuel += 1

                elif 1140 > a > 840 and 1290 > b > 1020:
                    cercle(a, b, img, r, "D5")
                    nombreTourActuel += 1

                elif 780 > a > 530 and 1290 > b > 1020:
                    cercle(a, b, img, r, "D6")
                    nombreTourActuel += 1

                elif 1930 > a > 1690 and 1500 > b > 1250:
                    cercle(a, b, img, r, "C1")
                    nombreTourActuel += 1

                elif 1700 > a > 1450 and 1500 > b > 1250:
                    cercle(a, b, img, r, "C2")
                    nombreTourActuel += 1

                elif 1480 > a > 1210 and 1550 > b > 1250:
                    cercle(a, b, img, r, "C3")
                    nombreTourActuel += 1

                elif 2270 > a > 2020 and 1800 > b > 1520:
                    cercle(a, b, img, r, "B1")
                    nombreTourActuel += 1

                elif 1700 > a > 1450 and 1840 > b > 1560:
                    cercle(a, b, img, r, "B2")
                    nombreTourActuel += 1

                elif 1160 > a > 880 and 1860 > b > 1560:
                    cercle(a, b, img, r, "B3")
                    nombreTourActuel += 1

                elif 2645 > a > 2370 and 2150 > b > 1875:
                    cercle(a, b, img, r, "A1")
                    nombreTourActuel += 1

                elif 1730 > a > 1470 and 2170 > b > 1930:
                    cercle(a, b, img, r, "A2")
                    nombreTourActuel += 1

                elif 800 > a > 510 and 2200 > b > 1930:
                    cercle(a, b, img, r, "A3")
                    nombreTourActuel += 1

                else:
                    print('pas trouver')

                plt.imshow(img)
                plt.show()
                print(nombreTourActuel)
                if nombreTourActuel == nbrCercle:
                    time.sleep(2)
                    print('tout trouver')
                    return
                print('-------------')

        else:

            print('Aucun pion trouver')
            break
        print('recommencer')


def mouvementLicite():
    print(listePosition)



def run():
    dessin(4)
    mouvementLicite()
    os._exit(0)


def stop():
    try:
        while True:
            # read and display the sensor value
            # BP.get_sensor retrieves a sensor value.
            # BP.PORT_1 specifies that we are looking for the value of sensor port 1.
            # BP.get_sensor returns the sensor value (what we want to display).
            try:
                value = BP.get_sensor(BP.PORT_4)
                print(value)
                if value == 1:
                    os._exit(0)
                    break
            except brickpi3.SensorError as error:
                print(error)

            time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

    except KeyboardInterrupt:  # except the program gets interrupted by Ctrl+C on the keyboard.
        BP.reset_all()


tRun = threading.Thread(target=run())
tStop = threading.Thread(target=stop())

tRun.start()
tStop.start()
