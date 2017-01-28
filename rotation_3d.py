import math
from graphics import * 
import time #time.sleep

pi = 3.14159265359

def matrix_mult(matrix1, matrix2, matrix_fin): # [range][colonne]

    for i in range(len(matrix2[0])):# les colonnes de la matrice 2
        for j in range(len(matrix1)): # les rangés de la matrice 1
            
#   à partir de ce moment l'exosquelette de la matrice ce dessine
#   maintenant il faut calculer les valeurs de la matrice
            result = 0
            for k in range(len(matrix2)): # on assume que la matrice2 a le meme nombre de rangé que de colonne dans la matrice1
                result += matrix1[j][k] * matrix2[k][i]
            
            matrix_fin[j][i] = result






taille = [400,400]

c = 50
cube = [[-c,c,c], [c,c,c], [c,-c,c], [-c,-c,c], [-c,c,-c], [c,c,-c], [c,-c,-c], [-c,-c,-c] ]


#                    [-c,c,-c] [c,c,-c]

# [-c,c,c]  [c,c,c]  [-c,-c,-c] [c,-c,-c]
 
# [-c,-c,c] [c,-c,c]
center = [taille[0]//2, taille[1]//2]

angle_deg = 0
angle = 0

sommet = []
aLine = []

for i in range(8):
    sommet.append(Point(0,0))
for i in range(12):
    aLine.append(Line(Point(0,0),Point(0,0)))

win = GraphWin("Rotation 3d", taille[0], taille[1])
win.setBackground("white")
rotate = 0

MR = [[],[],[]]
MRF = [[],[],[]]
for i in range(3):
    for j in range(3):
        MR[j].append(0)
        MRF[j].append(0)

while True:
    #matrice de rotation
    R_x = [[1,0,0],
           [0,math.cos(angle), -math.sin(angle)],
           [0, math.sin(angle), math.cos(angle)]]
    
    R_y = [[math.cos(angle), 0, math.sin(angle)],
           [0,1,0],
           [-math.sin(angle), 0, math.cos(angle)]]
    
    R_z = [[math.cos(angle), -math.sin(angle), 0],
           [math.sin(angle), math.cos(angle), 0],
           [0,0,1]]

    matrix_mult(R_x, R_y, MR)
    matrix_mult(MR,R_z , MRF)
    
    
    for i in range(8):
        sommet[i] = Point(center[0] + MRF[0][0]*cube[i][0] + MRF[0][1]*cube[i][1] + MRF[0][2]*cube[i][2],
                          center[1] + MRF[1][0]*cube[i][0] + MRF[1][1]*cube[i][1] + MRF[1][2]*cube[i][2])

    
    

    aLine[0] = Line(sommet[0], sommet[1])
    aLine[0].setOutline("red")
    aLine[1] = Line(sommet[1], sommet[2])
    aLine[1].setOutline("blue")
    aLine[2] = Line(sommet[2], sommet[3])
    aLine[3] = Line(sommet[3], sommet[0])
    aLine[4] = Line(sommet[0], sommet[4])
    aLine[5] = Line(sommet[1], sommet[5])
    aLine[5].setOutline("green")
    aLine[6] = Line(sommet[2], sommet[6])
    aLine[7] = Line(sommet[3], sommet[7])
    aLine[8] = Line(sommet[4], sommet[5])
    aLine[9] = Line(sommet[5], sommet[6])
    aLine[10] = Line(sommet[6], sommet[7])
    aLine[11] = Line(sommet[7], sommet[4])

    
    
    for i in range(12):
        aLine[i].draw(win)
    time.sleep(0.1)
    for i in range(12):
        aLine[i].undraw()
        
    angle_deg += 7
    angle = angle_deg * pi / 180
    
    rotate +=1
    
    
win.close()
