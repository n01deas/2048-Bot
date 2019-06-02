# Automatisierter Bot für das Spiel 2048
# http://2048game.com/

from PIL import ImageGrab, ImageOps
import pyautogui

# Array welches unser Feld mit den entsprechenden Werten
aktuellesFeld = [0, 0, 0, 0
                 0, 0, 0 ,0
                 0, 0, 0, 0
                 0, 0, 0, 0]

# Koordinaten der Felder auf halben Bildschrim
class Feldkoordinaten:
    feld11 = (170, 270)
    feld12 = (270, 270)
    feld13 = (370, 270)
    feld14 = (470, 270)

    feld21 = (170, 370)
    feld22 = (270, 370)
    feld23 = (370, 370)
    feld24 = (470, 370)

    feld31 = (170, 470)
    feld32 = (270, 470)
    feld33 = (370, 470)
    feld34 = (470, 470)

    feld41 = (170, 570)
    feld42 = (270, 570)
    feld43 = (370, 570)
    feld44 = (470, 570)

    # Array mit den ganzen Felder, um später drüber iterieren zu können
    felderArray = [ feld11, feld12, feld13, feld14,
                    feld21, feld22, feld23, feld24,
                    feld31, feld32, feld33, feld34,
                    feld41, feld42, feld43, feld44]

# Funktion die uns das Feld übergibt und in das globale Array speichert
def getFeld():
    # Farbe in dem Feld bestimmen
    image = ImageGrab.grab() # Screenshot von dem Screen
    # Das Bild in grayscale Konvertieren um später nur einen Integer zu haben
    grayImage = ImageOps.grayscale(image)



    
    for index, Feldkoordinaten in enumerate (.........
        pixel = grayImage.getpixel(Feldkoordinaten)
        print(pixel)

# Klasse in der die Pixelwerte ihren Felder zugewiesen werden
class PixelWerte:
    leer = 195
    zwei = 229
    vier = 225
    acht = 190
    sechzehn = 172 
    zweiundreisig = 157
    vierundsechzig = 135
    hundertachtundzwanzig = 205
    zweihundertsechundfünzig = 201
    fünfhundertzwölf = 197
    tausendundzwölf = 193
    zweitausendachtundvierzig = 189

    werteArray = [  leer, zwei, vier, acht, sechzehn, zweiundreisig, 
                    vierundsechzig,hundertachtundzwanzig, zweihundertsechundfünzig,
                    fünfhundertzwölf, tausendundzwölf, zweitausendachtundvierzig]