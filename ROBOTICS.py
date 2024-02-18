#ΕΙΣΑΓΩΓΗ ΑΝΑΓΚΑΙΩΝ ΒΙΒΛΙΟΘΗΚΩΝ 
import tkinter as tk 
from tkinter import simpledialog 
from tkinter import messagebox 
import math
from win32api import GetSystemMetrics
from graphics import*

#ΚΑΘΟΡΙΣΜΟΣ ΜΕΓΕΘΟΥΣ ΚΑΙ ΣΥΝΤΕΤΑΓΜΕΝΩΝ ΑΝΑΔΥΟΜΕΝΟΥ ΠΑΡΑΘΥΡΟΥ ΕΡΓΑΣΙΑΣ
screenWidth = GetSystemMetrics(0) * 0.60 
screenHeight = GetSystemMetrics(1) * 0.60
win = GraphWin(width=screenWidth, height=screenHeight)
win.setCoords((screenWidth/2) * -1, (screenHeight/2) * -1, screenWidth/2, screenHeight/2) 
win.setBackground('grey')

#ΚΑΘΟΡΙΣΜΟΣ ΧΡΩΜΑΤΩΝ ΒΑΣΙΚΩΝ ΧΑΡΑΚΤΗΡΙΣΤΙΚΩΝ KAI ΣΤΑΘΕΡΩΝ
ColorCartesian = "green"
ColorOfElbow = "blue"
ColorOfArms = "blue"
ColorMove = "red"
ColorBackround= "green"
radius = 200
orioepsilon = 0.001

#ΣΥΝΑΡΤΗΣΕΙΣ ΓΙΑ ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ ΜΕ ΑΝΑΔΥΟΜΕΝΑ ΠΑΡΑΘΥΡΑ
def InputPositiveIntegerFromPopUp(message): 
    while True:
        try:
            ROOT = tk.Tk()
            ROOT.withdraw() 
            USER_INP = simpledialog.askstring(title="Είσοδος δεδομένων",prompt=message)
            a = int(USER_INP)
            if a >= 0: break #ΤΑ ΜΗΚΗ ΠΡΕΠΕΙ ΝΑ ΕΙΝΑΙ ΘΕΤΙΚΑ 
        except ValueError:
            print('Παρακαλώ πληκτρολογήστε ένα θετικό ακέραιο!')
    return int(a) 
def InputPositiveIntegerFromPopUp2(message2): 
    while True:
        try:
            ROOT = tk.Tk()
            ROOT.withdraw() 
            USER_INP = simpledialog.askstring(title="Είσοδος δεδομένων",prompt=message2) #ΟΙ ΣΥΝΤΕΤΑΓΜΝΕΣ ΜΠΟΡΟΥΝ ΝΑ ΕΙΝΑΙ ΕΙΤΕ ΑΡΝΗΤΙΚΕΣ ΕΙΤΕ ΘΕΤΙΚΕΣ ΑΛΛΑ ΑΚΕΡΑΙΕΣ
            b = int(USER_INP); break 
        except ValueError:
            print('Παρακαλώ πληκτρολογήστε έναν ακέραιο!')
    return int(b) 

while True:
#ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ L1,L2 - ΕΠΙΘΥΜΗΤΟ ΜΗΚΟΣ ΡΟΜΠΟΤΙΚΩΝ ΜΕΛΩΝ
    L1 = InputPositiveIntegerFromPopUp("Παρακαλώ, πρόσθεσε το επιθυμητο μήκος L1 του 1ου μέλους του ρομποτικού βραχίονα:") 
    L2 = InputPositiveIntegerFromPopUp("Παρακαλω προσθέσε το επιθυμητό μήκος L2 του 2ου μέλους του ρομποτικού βραχίονα:")
#ΚΑΘΟΡΙΣΜΟΣ ΦΑΚΕΛΩΝ ΕΡΓΑΣΙΑΣ ΡΟΜΠΟΤΙΚΟΥ ΒΡΑΧΙΟΝΑ 
    #Ο ΡΟΜΠΟΤΙΚΟΣ ΒΡΑΧΙΟΝΑΣ ΜΠΟΡΕΙ ΝΑ ΕΡΓΑΖΕΤΑΙ ΕΝΤΟΣ ΤΟΥ ΕΞΩΤΕΡΙΚΟΥ ΚΑΙ ΕΚΤΟΣ ΤΟΥ ΕΣΩΤΕΡΙΚΟΥ ΦΑΚΕΛΟΥ
    if (radius >= abs(L1-L2)) and (radius <= L1+L2) == True : break 
    else: print("ΕΚΤΟΣ ΦΑΚΕΛΩΝ ΕΡΓΑΣΙΑΣ ΔΟΚΙΜΑΣΕ ΝΕΑ ΜΗΚΗ")

#ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ Χ2,Υ2 - ΕΠΙΘΥΜΗΤΟ ΣΗΜΕΙΟ ΔΕΥΤΕΡΟΥ ΜΕΛΟΥΣ ΒΡΑΧΙΟΝΑ
while True:
    X2 = InputPositiveIntegerFromPopUp2("Παρακαλώ, πρόσθεσε συντεταγμενη Χ2:") 
    Y2 = InputPositiveIntegerFromPopUp2("Παρακαλω προσθέσε συντεταγμενη Υ2:")
    if ((X2**2+Y2**2) >= abs((L1-L2)**2)) and ((X2**2+Y2**2) <= ((L1+L2)**2)) ==True : break
    else: print("ΜΗ ΑΠΟΔΕΚΤΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ Χ2,Υ2 ΕΚΤΟΣ ΦΑΚΕΛΩΝ ΔΟΚΙΜΑΣΕ ΝΕΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ")


#ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ Α Ή Δ - ΑΡΙΣΤΕΡΟΣΤΡΟΦΗ Η ΔΕΞΙΟΣΤΡΟΦΗ ΛΥΣΗ
while True: 
    try: 
        result = messagebox.askyesno("Προσοχή", "ΝΑΙ αν θέλεις αριστερόστροφη ή ΟΧΙ αν θέλεις δεξιόστροφη λύση")  
        if result == True: 
            LR=0 
        else: 
            LR=1 
    except WindowsError as win_err: 
        print("An error occurred:\n{}".format(win_err)) 
    if (LR == 0 or LR == 1) == True: break


#ΔΗΜΙΟΥΡΓΙΑ ΑΝΑΓΚΑΙΩΝ ΣΥΝΑΡΤΗΣΕΩΝ 
def DrawLine(Xtel,Ytel,X2,Y2,win,width, color): 
    line = Line(Point(Xtel, Ytel), Point(X2, Y2))
    line.setWidth(width); line.setFill(color)
    line.draw(win)
def DrawCircle(Xtel,Ytel,radius,win,width,color,fillcolor=''): 
    aCircle = Circle(Point(Xtel,Ytel), radius)
    aCircle.setWidth(width);aCircle.setOutline(color)
    if fillcolor !='': aCircle.setFill(fillcolor)
    aCircle.draw(win)
def DesginAxes (color, width, height, win): 
    DrawLine(-width / 2, 0, width / 2, 0, win, 2, color)
    DrawLine(0, -height / 2, 0, height / 2, win, 2, color)  
def atn2(Xa,Ya):
    if abs(Xa) < orioepsilon:
        if Ya>0:
            return math.pi/2
        else:
            return 3*math.pi/2
    else:
        if Xa>0 and Ya>=0 :
            return math.atan(Ya/Xa)
        elif Xa>0 and Ya<0:
            return math.atan(Ya/Xa) + 2*math.pi
        else: 
            return math.atan(Ya/Xa) + math.pi
        
#ΒΑΣΙΚΗ ΣΧΕΔΙΑΣΗ ΑΝΑΔΥΟΜΕΝΟΥ ΠΛΑΙΣΙΟΥ - ΑΞΟΝΕΣ ΚΑΙ ΠΕΡΙΟΧΗ ΕΡΓΑΣΙΑΣ
DrawCircle (0, 0, radius, win, 2, 'black','white')
DesginAxes(ColorCartesian, screenWidth, screenHeight, win) 
DrawCircle(0,0,abs(L1-L2),win,2,'black','orange')

def arm(X2,Y2,L1,L2,LR):
    #ΕΥΡΕΣΗ ΛΥΣΕΩΝ ΑΠΟ ΕΙΣΑΓΟΜΕΝΑ ΔΕΔΟΜΕΝΑ
        #ΕΥΡΕΣΗ Χ1,Υ1 - ΠΡΩΤΟ ΣΗΜΕΙΟ ΣΤΟ ΡΟΜΠΟΤΙΚΟ ΜΕΛΟΣ
    c = (Y2**2+X2**2+L1**2-L2**2)/2
    if abs(X2) > orioepsilon :
        D = 4*(c**2)*(Y2**2) - (4*((Y2**2)+(X2**2))*((c**2)-(L1**2)*(X2**2)))
        if   ( D > 0 or D == 0 ) : 
            Ya = (2*c*Y2 + math.sqrt(D)) / (2 * (X2**2+Y2**2))
            Yarnit = (2*c*Y2 - math.sqrt(D)) / (2 *(X2**2+Y2**2))
            Xa = (c - Y2*Ya)/X2
            Xarnit = (c - Y2*Yarnit)/X2
        elif D < 0 :
            print("ΑΔΥΝΑΤΗ ΛΥΣΗ")
    elif abs(X2) < orioepsilon :
        if abs(Y2) < orioepsilon :
            print("ΚΑΤΑΣΤΡΟΦΗ ΤΟΥ ΡΟΜΠΟΤ")
        elif abs(Y2) > orioepsilon : 
            Ya = c / Y2 
            Yarnit = Ya
            Xarnit = math.sqrt(L1**2 - ((c**2)/(Y2**2))) 
            Xa= - math.sqrt((L1**2) - ((c**2)/(Y2**2)))
    
    #ΔΙΕΡΕΥΝΗΣΗ ΤΗΣ ΓΩΝΙΑΣ Q2 - ELBOW-ARM
    #ΕΛΕΓΧΟΣ ΤΟΥ ΘΕΤΙΚΟΥ ΖΕΥΓΟΥΣ ΜΕ ΑΡΙΣΤΕΡΗ ΠΕΡΙΣΤΡΟΦΗ
    Q11 = atn2(Xa,Ya)
    X2t = X2*math.cos(Q11) - Y2*math.sin(Q11) # ΟΙ ΣΥΝΤΕΤΑΓΜΕΝΕΣ ΜΕΤΑΚΙΝΗΣΗΣ 
    Y2t = X2*math.sin(Q11) + Y2*math.cos(Q11) 
    Q21 = atn2(X2t,Y2t)*(180/math.pi)
    if Q21>=0 and Q21<180:
        if LR==1: #ΔΕΞΙΑ
            Xtel=Xa
            Ytel=Ya
        else:
            Xtel=Xarnit
            Ytel=Yarnit
    else:
        if LR==0: #ΑΡΙΣΤΕΡΗ
            Xtel=Xa
            Ytel=Ya
        else:
            Xtel=Xarnit
            Ytel=Yarnit
    #ΣΧΕΔΙΑΣΗ ΒΡΑΧΙΟΝΑ ΜΕ ΒΑΣΗ ΤΙΣ ΕΠΙΛΟΓΕΣ ΤΟΥ ΧΡΗΣΤΗ
    DrawLine (0, 0, Xtel, Ytel, win, 2 , ColorOfArms)
    DrawCircle(Xtel, Ytel, 2 , win, 2 ,'orange') 
    DrawLine (Xtel, Ytel, X2, Y2, win, 2, ColorOfElbow)
    DrawCircle(X2, Y2, 2 , win, 2, 'orange')

#ΚΛΗΣΗ ΠΡΩΤΗΣ ΣΥΝΑΡΤΗΣΗΣ ΓΙΑ ΤΗΝ ΣΧΕΔΙΑΣΗ ΤΗΣ ΕΡΓΑΣΙΑΣ
ARMCALCULATIONS = arm(X2,Y2,L1,L2,LR)

#ΕΛΕΓΧΟΣ ΓΙΑ ΔΥΝΑΤΟΤΗΤΑ ΝΑ ΠΡΑΓΜΑΤΟΠΟΙΗΘΕΙ ΚΙΝΗΣΗ
#ΕΙΣΑΓΩΓΗ ΣΗΜΕΙΟΥ ΜΕΤΑΚΙΝΗΣΗΣ ΒΡΑΧΙΟΝΑ   
while True: 
    X3 = InputPositiveIntegerFromPopUp2("Παρακαλώ, για μετακίνηση πρόσθεσε συντεταγμενη για Χ3:") 
    Y3 = InputPositiveIntegerFromPopUp2("Παρακαλω, για μετακίνηση προσθέσε συντεταγμενη Υ3:") 
    if ((X3**2+Y3**2) >= abs((L1-L2)**2)) and ((X3**2+Y3**2) <= ((L1+L2)**2)) ==True : break
    else: print("ΜΗ ΑΠΟΔΕΚΤΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ Χ2,Υ2 ΕΚΤΟΣ ΦΑΚΕΛΩΝ ΔΟΚΙΜΑΣΕ ΝΕΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ")

#ΕΛΕΓΧΟΣ ΑΝ ΤΟ ΕΥΘΥΓΡΑΜΜΟ ΤΜΗΜΑ P2P3 ΔΕΝ ΤΕΜΝΕΙ ΤΟΝ ΕΣΩΤΕΡΙΚΟ ΦΑΚΕΛΟ ΕΡΓΑΣΙΑΣ

def possible(X2,Y2,X3,Y3):
    if X2==X3:
        if abs(X2)>abs(L1-L2):
            print("Εφικτή κίνηση με Χ2=Χ3, πληκτρολόγησε 1")
            DrawLine(X2,Y2,X3,Y3,win,2,'red')
        else:
            XS1 = XS2 = X2
            YS1 = math.sqrt((L1-L2)**2-XS1**2)
            YS2 = -math.sqrt((L1-L2)**2-XS1**2)
            DP2P3 = math.sqrt((Y3-Y2)**2+(X3-X2)**2)
            DP2S1 = math.sqrt((YS1-Y2)**2+(XS1-X2)**2)
            DP2S2 = math.sqrt((YS2-Y2)**2+(XS2-X2)**2)
            DP3S1 = math.sqrt((YS1-Y3)**2+(XS1-X3)**2)
            DP3S1 = math.sqrt((YS2-Y3)**2+(XS2-X3)**2)
            Dmin0 = min(DP2S1,DP2S2)
            Dmin1 = min(DP2S2,DP2S2)
            Dmax = max(Dmin0,Dmin1)
            if Dmax > DP2P3:
                InputPositiveIntegerFromPopUp("Η κίνηση είναι εφικτή, πληκτρολόγησε 1")
                DrawLine(X2,Y2,X3,Y3,win,2,'red')
            else:
                while True:
                    X3 = InputPositiveIntegerFromPopUp2("Παρακαλώ,πληκτρολόγησε νέο Χ3:") 
                    Y3 = InputPositiveIntegerFromPopUp2("Παρακαλω, πληκτρολόγσε νέο Υ3:") 
                    if ((X3**2+Y3**2) >= abs((L1-L2)**2)) and ((X3**2+Y3**2) <= ((L1+L2)**2)) ==True : break
                    else: print("ΜΗ ΑΠΟΔΕΚΤΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ Χ2,Υ2 ΕΚΤΟΣ ΦΑΚΕΛΩΝ ΔΟΚΙΜΑΣΕ ΝΕΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ")
    else:
        a=(Y3-Y2)/(X3-X2)
        b=Y3-a*X2
        D2=4*(a**2)*(b**2)-4*(a**2+1)*(b**2-((L1-L2)**2))
        if D2<0 or D2==0:
            InputPositiveIntegerFromPopUp("Η κίνηση είναι εφικτή, πληκτρολόγησε 1") 
            DrawLine(X2,Y2,X3,Y3,win,2,'red')
        else:
            InputPositiveIntegerFromPopUp("Η κίνηση δεν είναι εφικτή σε κάθε περίπτωση θα γίνει διευρεύνηση, πληκτρολόγησε 1")
            XS1= -2*a*b+math.sqrt(D2)/(2*(a**2+1))
            XS2= -2*a*b-math.sqrt(D2)/(2*(a**2+1))
            YS1 = a*XS1+b
            YS2 = a*XS2+b
            DP2P3 = math.sqrt((Y3-Y2)**2+(X3-X2)**2)
            DP2S1 = math.sqrt((YS1-Y2)**2+(XS1-X2)**2)
            DP2S2 = math.sqrt((YS2-Y2)**2+(XS2-X2)**2)
            DP3S1 = math.sqrt((YS1-Y3)**2+(XS1-X3)**2)
            DP3S1 = math.sqrt((YS2-Y3)**2+(XS2-X3)**2)
            Dmin0 = min(DP2S1,DP2S2)
            Dmin1 = min(DP2S2,DP2S2)
            Dmax = max(Dmin0,Dmin1)
            if Dmax > DP2P3:
                InputPositiveIntegerFromPopUp("Η κίνηση είναι εφικτή, πληκτρολόγησε 1")
                DrawLine(X2,Y2,X3,Y3,win,2,'red')
            else:
                while True:
                    X3 = InputPositiveIntegerFromPopUp2("Παρακαλώ,πληκτρολόγησε νέο Χ3:") 
                    Y3 = InputPositiveIntegerFromPopUp2("Παρακαλω, πληκτρολόγσε νέο Υ3:") 
                    if ((X3**2+Y3**2) >= abs((L1-L2)**2)) and ((X3**2+Y3**2) <= ((L1+L2)**2)) ==True : break
                    else: print("ΜΗ ΑΠΟΔΕΚΤΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ Χ2,Υ2 ΕΚΤΟΣ ΦΑΚΕΛΩΝ ΔΟΚΙΜΑΣΕ ΝΕΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ")
               

#ANIMATION ΚΙΝΗΣΗΣ
MOVE = possible(X2,Y2,X3,Y3)
Duration = 2
Rate = 20
Points = int(Duration*Rate)
DelaySec = 1/Rate
for i in range(0, Points + 1):
    #ΥΠΟΛΟΓΙΖΩ ΤΑ ΣΗΜΕΙΑ ΜΕΤΑΒΑΣΗΣ ΕΩΣ ΤΟ Χ3,Υ3
    xp = float((X3 - X2) * i / Points + X2) 
    yp = float((Y3 - Y2) * i / Points + Y2)
    #ΣΧΕΔΙΑΖΩ ΤΗΝ ΕΥΘΕΙΑ ΤΗΣ ΚΙΝΗΣΗΣ
    DrawLine (X2, Y2, X3, Y3, win, 2, ColorMove) 
    #ΚΑΘΥΣΤΕΡΩ ΓΙΑ ΝΑ ΠΡΟΛΑΒΕΙ ΝΑ ΤΗΝ ΔΕΙ Ο ΧΡΗΣΤΗΣ
    time.sleep(DelaySec) 
    DesginAxes(ColorCartesian, screenWidth, screenHeight, win)
    #ΣΒΗΝΩ ΤΗΝ ΑΠΛΗ ΓΡΑΜΜΗ
    DrawLine (X2, Y2, xp, yp, win, 2, ColorBackround) 
    #ΣΧΕΔΙΑΖΩ ΤΟΝ ΒΡΑΧΙΟΝΑ ΣΕ ΚΑΘΕ ΣΗΜΕΙΟ ΠΟΥ ΠΕΡΝΑ ΕΩΣ ΤΟ Χ3,Υ3 
    NEWARMCALCUALTIONS = arm(X3,Y3,L1,L2,LR) #ΔΕΙΧΝΩ ΤΗΝ ΤΕΛΙΚΗ ΘΕΣΗ 
    NEWARMCALCUALTIONS = arm(xp,yp,L1,L2,LR) #ΤΑΞΙΔΕΥΩ ΩΣ ΕΚΕΙ


win.getMouse() 
win.close()

      
