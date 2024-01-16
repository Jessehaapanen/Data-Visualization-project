import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from alustus import Alustus

class Grafiikka(QWidget):

    """Luokka Grafiikka kysyy käyttäjältä syötteitä graafin piirtämistä varten ja asettaa nämä tiedot Alustus luokan olioon graafin piirtämistä varten."""

    def __init__(self):
        super().__init__()

    """Metodi kysySyöte piirtää käyttäjälle näkymän, jota hyväksi käyttäen voidaan asettaa halutut tiedot graafin piirtämistä varten."""
    def kysySyöte(self):
        ikkunaotsikko = "Diagrammin valmistelu"
        self.setWindowTitle(ikkunaotsikko)

        self.label_kuvio = QLabel("Minkä kuvion haluat piirtää?")
        self.rb1 = QRadioButton("Viivadiagrammi",self)
        self.rb4 = QRadioButton("Pylväsdiagrammi",self)
        self.rb5 = QRadioButton("Ympyrädiagrammi",self)
        self.rbgroup1 = QButtonGroup()
        self.rbgroup1.addButton(self.rb1)
        self.rbgroup1.addButton(self.rb4)
        self.rbgroup1.addButton(self.rb5)
        self.rb1.clicked.connect(self.kuvionValinta)
        self.rb4.clicked.connect(self.kuvionValinta)
        self.rb5.clicked.connect(self.kuvionValinta)

        self.label_grid = QLabel("Haluatko piirtää kuvaajaan gridin (ruudukko)?")
        self.rb2 = QRadioButton("Kyllä",self)
        self.rb3 = QRadioButton("Ei",self)
        self.rbgroup2 = QButtonGroup()
        self.rbgroup2.addButton(self.rb2)
        self.rbgroup2.addButton(self.rb3)
        self.rb2.clicked.connect(self.gridValinta)
        self.rb3.clicked.connect(self.gridValinta)

        self.label_grid_skaala = QLabel("Anna positiivinen gridin skaalauskerron numerisessa muodossa.")
        self.kentta4 = QLineEdit()
        self.kentta4.textChanged[str].connect(self.skaalausValinta)

        self.label_data = QLabel("Anna datan sijainti ja nimi tekstikenttään.")
        self.kentta1 = QLineEdit()
        self.kentta1.textChanged[str].connect(self.datanValinta)

        self.label_otsikko = QLabel("Anna kuvaajan otsikko (ei pakollinen).")
        self.kentta5 = QLineEdit()
        self.kentta5.textChanged[str].connect(self.otsikonValinta)

        self.label_xakseli = QLabel("Anna X-akselin selite (ei pakollinen).")
        self.kentta2 = QLineEdit()
        self.kentta2.textChanged[str].connect(self.xakselinValinta)

        self.label_yakseli = QLabel("Anna Y-akselin selite (ei pakollinen).")
        self.kentta3 = QLineEdit()
        self.kentta3.textChanged[str].connect(self.yakselinValinta)

        self.label_xaste = QLabel("Anna X-akselin asteikon selite (ei pakollinen).")
        self.kentta6 = QLineEdit()
        self.kentta6.textChanged[str].connect(self.xasteikonValinta)

        self.label_yaste = QLabel("Anna Y-akselin asteikon selite (ei pakollinen).")
        self.kentta7 = QLineEdit()
        self.kentta7.textChanged[str].connect(self.yasteikonValinta)

        self.gridke_hidden = True
        if self.gridke_hidden: #Piilottaa osan graafisesta syötekentän valinnoista mikäli niiden ominaisuuksia ei tarvita valitun kuvion piirtämisessä.
            self.label_grid.hide()
            self.rb2.hide()
            self.rb3.hide()

        self.grid_hidden = True
        if self.grid_hidden: #Piilottaa osan graafisesta syötekentän valinnoista mikäli niiden ominaisuuksia ei tarvita valitun kuvion piirtämisessä.
            self.label_grid_skaala.hide()
            self.kentta4.hide()

        self.xselite_hidden = True
        if self.xselite_hidden: #Piilottaa osan graafisesta syötekentän valinnoista mikäli niiden ominaisuuksia ei tarvita valitun kuvion piirtämisessä.
            self.label_xakseli.hide()
            self.kentta2.hide()

        self.yselite_hidden = True
        if self.yselite_hidden: #Piilottaa osan graafisesta syötekentän valinnoista mikäli niiden ominaisuuksia ei tarvita valitun kuvion piirtämisessä.
            self.label_yakseli.hide()
            self.kentta3.hide()

        self.xaste_hidden = True
        if self.xaste_hidden: #Piilottaa osan graafisesta syötekentän valinnoista mikäli niiden ominaisuuksia ei tarvita valitun kuvion piirtämisessä.
            self.label_xaste.hide()
            self.kentta6.hide()

        self.yaste_hidden = True
        if self.yaste_hidden: #Piilottaa osan graafisesta syötekentän valinnoista mikäli niiden ominaisuuksia ei tarvita valitun kuvion piirtämisessä.
            self.label_yaste.hide()
            self.kentta7.hide()

        """Asetetaan luodut widgetit graafiseen näkymään halutussa järjestyksessä."""
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_kuvio)
        self.layout.addWidget(self.rb1)
        self.layout.addWidget(self.rb4)
        self.layout.addWidget(self.rb5)

        self.layout.addWidget(self.label_grid)
        self.layout.addWidget(self.rb2)
        self.layout.addWidget(self.rb3)

        self.layout.addWidget(self.label_grid_skaala)
        self.layout.addWidget(self.kentta4)

        self.layout.addWidget(self.label_data)
        self.layout.addWidget(self.kentta1)
        self.layout.addWidget(self.label_otsikko)
        self.layout.addWidget(self.kentta5)

        self.layout.addWidget(self.label_xakseli)
        self.layout.addWidget(self.kentta2)
        self.layout.addWidget(self.label_yakseli)
        self.layout.addWidget(self.kentta3)

        self.layout.addWidget(self.label_xaste)
        self.layout.addWidget(self.kentta6)
        self.layout.addWidget(self.label_yaste)
        self.layout.addWidget(self.kentta7)

        self.setGeometry(50,50,300,300)
        self.setLayout(self.layout)
        self.pb1 = QPushButton("Piirrä kuvaaja", self)
        self.layout.addWidget(self.pb1)
        self.pb1.clicked.connect(self.valmistelu)
        self.pb1.clicked.connect(self.kuvioPiirto)

        self.pb2 = QPushButton("Sulje ohjelma",self)
        self.layout.addWidget(self.pb2)
        self.pb2.clicked.connect(self.close)
        self.pb2.clicked.connect(GraafiView.close)

        self.show()

    """Asettaa Alustus luokan kenttään tiedon siitä, halutaanko piirtää grid. Mikäli haluaa piirtää gridin, tuo käyttäjälle esille
    tesktikentän, jonka avulla voidaan antaa haluttu gridin skaalakerroin."""
    def gridValinta(self):
        valinta = self.sender().text()
        alustus.grid = valinta
        if valinta == 'Kyllä':
            self.label_grid_skaala.show()
            self.kentta4.show()

        elif valinta == "Ei":
            self.label_grid_skaala.hide()
            self.kentta4.hide()

    """Asettaa valitun kuvion tunnisteen Alustus luokan kenttään, sekä piilottaa ja näyttää widgettejä sen mukaan mitä 
    ominaisuuksia käyttäjä on valinnut piirrettävän graafiin."""
    def kuvionValinta(self):
        valinta = self.sender().text()
        alustus.tunniste = valinta
        if valinta == "Viivadiagrammi":
            self.label_xakseli.show()
            self.kentta2.show()
            self.label_yakseli.show()
            self.kentta3.show()
            self.label_grid.show()
            self.rb2.show()
            self.rb3.show()
            self.label_xaste.show()
            self.kentta6.show()
            self.label_yaste.show()
            self.kentta7.show()

        elif valinta == "Pylväsdiagrammi":
            self.label_xakseli.hide()
            self.kentta2.hide()
            self.label_yakseli.show()
            self.kentta3.show()
            self.label_grid.show()
            self.rb2.show()
            self.rb3.show()
            self.label_xaste.show()
            self.kentta6.show()
            self.label_yaste.show()
            self.kentta7.show()

        elif valinta == "Ympyrädiagrammi":
            self.label_xakseli.hide()
            self.kentta2.hide()
            self.label_yakseli.hide()
            self.kentta3.hide()
            self.label_grid.hide()
            self.rb2.hide()
            self.rb3.hide()
            self.label_grid_skaala.hide()
            self.kentta4.hide()
            self.label_xaste.hide()
            self.kentta6.hide()
            self.label_yaste.hide()
            self.kentta7.hide()

    """Asettaa Alustus luokan kenttään käyttäjän antaman gridin skaalakertoimen."""
    def skaalausValinta(self, text):
        alustus.gridSkaalaus = 1
        try:
            text = float(text)
            alustus.gridSkaalaus = text
        except:
            pass

    """Asettaa annetun datan nimen Alustus luokan kenttään."""
    def datanValinta(self, text):
        alustus.dataNimi = text

    """Asettaa annetun graafin otsikon Alustus luokan kenttään."""
    def otsikonValinta(self, text):
        alustus.otsikko = text

    """Asettaa annetun x-akselin selitteen Alustus luokan kenttään."""
    def xakselinValinta(self, text):
        alustus.xakseli = text

    """Asettaa annetun y-akselin selitteen Alustus luokan kenttään."""
    def yakselinValinta(self, text):
        alustus.yakseli = text

    """Asettaa annetun x-akselin asteen selitteen Alustus luokan kenttään."""
    def xasteikonValinta(self, text):
        alustus.xasteikko = text

    """Asettaa annetun y-akselin asteen selitteen Alustus luokan kenttään."""
    def yasteikonValinta(self, text):
        alustus.yasteikko = text

    """Valmistelee Alustus luokan diagrammin piirtämistä varten."""
    def valmistelu(self):
        alustus.avaaTiedosto(alustus.dataNimi)
        alustus.lueData(alustus.dataFile)
        alustus.laskeKa(alustus.data)
        alustus.laskeKeskihajonta(alustus.data, alustus.keskiarvo)
        alustus.maxmin(alustus.data)

        if alustus.tunniste == "Ympyrädiagrammi":
            alustus.ympyraOsuudet(alustus.data)

        else:
            alustus.laskeSkaalaus(alustus.minmax_x, alustus.minmax_y)
            alustus.laskeGridSkaalaus()
            alustus.akselienArvot(alustus.minmax_x, alustus.minmax_y)

    """Kutsuu luokkaa GraafiView diagrammin piirtämistä varten."""
    def kuvioPiirto(self):
        if alustus.tunniste == "Viivadiagrammi":
            print(alustus.piirtook, alustus.data)
            if alustus.piirtook == 1 and len(alustus.data) > 1:
                self.g = GraafiView()
                self.g.show()
        else:
            if alustus.piirtook == 1 and len(alustus.data) > 0:
                self.g = GraafiView()
                self.g.show()

class GraafiItem(QGraphicsItem):

    """Luokka GraafiItem luo piirrettävät elementit (viivat, ympyrät yms.) graafiin sen mukaan mikä kuvion on valittu piirrettäväksi."""

    def __init__(self):
        super().__init__()

    """Asettaa rajat piirrettävälle näkymälle."""
    def boundingRect(self):
        if alustus.tunniste == "Viivadiagrammi":
            return QRectF(alustus.minmax_x[0]*alustus.skaalaus[0],-alustus.minmax_y[1]*alustus.skaalaus[1],alustus.viivakoko, alustus.viivakoko)

        elif alustus.tunniste == "Pylväsdiagrammi":
            if alustus.minmax_y[0] > 0 or (alustus.minmax_y[0] < 0 and alustus.minmax_y[1] > 0):
                return QRectF(0,-alustus.minmax_y[1] * alustus.skaalaus[1],alustus.viivakoko,alustus.viivakoko)
            elif alustus.minmax_y[1] < 0:
                return QRectF(0,0,alustus.viivakoko, alustus.viivakoko)

        elif alustus.tunniste == "Ympyrädiagrammi":
            return QRectF(0,0,alustus.viivakoko,alustus.viivakoko)


    """Piirtää annetun datan perusteella diagrammin viivat ja ympyrät."""
    def paint(self, painter, option, widget):
        data = alustus.data

        if alustus.tunniste == "Viivadiagrammi":
            skaalausx = alustus.skaalaus[0]
            skaalausy = alustus.skaalaus[1]
            yk = 10 #Ympyrän koko

            """Mikäli grid halutaan piirtää, piirtää gridit."""
            if alustus.grid == 'Kyllä':
                painter.setPen(Qt.gray)
                for i in alustus.grid_valit:
                    line = QLineF(alustus.minmax_x[0] * skaalausx + i, -alustus.minmax_y[0] * skaalausy + 10, alustus.minmax_x[0] * skaalausx + i, -alustus.minmax_y[1] * skaalausy-10)
                    painter.drawLine(line)
                    line = QLineF(alustus.minmax_x[0] * skaalausx - 10, -alustus.minmax_y[0] * skaalausy - i, alustus.minmax_x[1] * skaalausx+10, -alustus.minmax_y[0] * skaalausy - i)
                    painter.drawLine(line)

            """Piirtää datapisteet ympyröinä ja näiden välille viivat."""
            for n in range(len(data)):
                pen = QPen()
                pen.setColor(Qt.red)
                pen.setWidth(2)
                painter.setPen(pen)
                painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))

                if n + 1 < len(data):
                    ellips = QRectF(data[n][0] * skaalausx - yk / 2, -data[n][1] * skaalausy - yk / 2, yk, yk)
                    painter.drawEllipse(ellips)
                    line = QLineF((data[n][0]) * skaalausx, -(data[n][1]) * skaalausy, (data[n + 1][0]) * skaalausx,
                                  -(data[n + 1][1]) * skaalausy)
                    painter.drawLine(line)
                else:
                    ellips = QRectF(data[n][0] * skaalausx - yk / 2, -data[n][1] * skaalausy - yk / 2, yk, yk)
                    painter.drawEllipse(ellips)
                    line = QLineF((data[n - 1][0]) * skaalausx, -(data[n - 1][1]) * skaalausy,
                                  (data[n][0]) * skaalausx, -(data[n][1]) * skaalausy)
                    painter.drawLine(line)

            ellips = QRectF(alustus.minmax_x[1]*skaalausx+220,-(alustus.minmax_y[1]*skaalausy)/2+18,yk,yk)
            painter.drawEllipse(ellips) #Piirtää seliteympyrän

            """Piirtää x ja y -akselit."""
            pen = QPen()
            pen.setColor(Qt.black)
            pen.setWidth(4)
            painter.setPen(pen)
            painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
            line1 = QLineF(alustus.minmax_x[0]*skaalausx-10,-alustus.minmax_y[1]*skaalausy-10,alustus.minmax_x[0]*skaalausx-10,-alustus.minmax_y[0]*skaalausy+10)
            line2 = QLineF(alustus.minmax_x[1]*skaalausx+10,-alustus.minmax_y[0]*skaalausy+10,alustus.minmax_x[0]*skaalausx-10,-alustus.minmax_y[0]*skaalausy+10)
            painter.drawLine(line1)
            painter.drawLine(line2)

            """Piirtää pienet väkäset x ja y -akseleille."""
            for i in range(0,alustus.viivakoko+100,100):
                line = QLineF(alustus.minmax_x[0]*skaalausx+i,-alustus.minmax_y[0]*skaalausy+10,alustus.minmax_x[0]*skaalausx+i, -alustus.minmax_y[0]*skaalausy+20)
                painter.drawLine(line)
                line = QLineF(alustus.minmax_x[0]*skaalausx-10,-alustus.minmax_y[0]*skaalausy-i,alustus.minmax_x[0]*skaalausx-20,-alustus.minmax_y[0]*skaalausy-i)
                painter.drawLine(line)

        elif alustus.tunniste == "Pylväsdiagrammi":
            skaalausy = alustus.skaalaus[1]

            """Mikäli grid halutaan piirtää, piirtää gridit."""
            if alustus.grid == 'Kyllä':
                painter.setPen(Qt.gray)
                for i in alustus.grid_valit:
                    if alustus.minmax_y[0] > 0:
                        line = QLineF(0, - i, alustus.viivakoko, - i)
                    elif (alustus.minmax_y[0] < 0 and alustus.minmax_y[1] > 0) or alustus.minmax_y[1] < 0:
                        line = QLineF(0, -alustus.minmax_y[0] * skaalausy - i, alustus.viivakoko, -alustus.minmax_y[0] * skaalausy - i)
                    painter.drawLine(line)

                    if alustus.minmax_y[0] < 0:
                        line = QLineF(i,-alustus.minmax_y[0]*skaalausy,i,-alustus.minmax_y[1]*skaalausy)
                        painter.drawLine(line)

            """Piirtää x ja y -akselit."""
            pen = QPen()
            pen.setColor(Qt.black)
            pen.setWidth(4)
            painter.setPen(pen)
            painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
            if alustus.minmax_y[0] > 0:
                line1 = QLineF(0, 0, 0, -alustus.minmax_y[1]*skaalausy -20)

            elif alustus.minmax_y[0] < 0 and alustus.minmax_y[1] > 0:
                line1 = QLineF(0,-alustus.minmax_y[0]*skaalausy + 20,0,-alustus.minmax_y[1]*skaalausy - 20)

            elif alustus.minmax_y[1] < 0:
                line1 = QLineF(0,0,0,-alustus.minmax_y[0]*skaalausy +20)

            line2 = QLineF(0, 0, alustus.viivakoko +10, 0)
            painter.drawLine(line1)
            painter.drawLine(line2)

            """Piirtää pienet väkäset y -akseleille."""
            for i in range(0, alustus.viivakoko + 100, 100):
                if alustus.minmax_y[0] > 0 or (alustus.minmax_y[0] < 0 and alustus.minmax_y[1] > 0):
                        line = QLineF(0, -alustus.minmax_y[1]*skaalausy + i, -20, -alustus.minmax_y[1]*skaalausy + i)
                        painter.drawLine(line)

                elif alustus.minmax_y[1] < 0:
                        line = QLineF(0, -alustus.minmax_y[0]*skaalausy - i, -20, -alustus.minmax_y[0]*skaalausy - i)
                        painter.drawLine(line)

            """Piirtää pylväät."""
            pen = QPen()
            pen.setColor(Qt.black)
            pen.setWidth(3)
            painter.setPen(pen)
            painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
            x = 0
            for n in range(len(data)):
                rect = QRectF(x,0,alustus.skaalaus[0],-data[n][1]*skaalausy)
                painter.drawRect(rect)
                x += alustus.skaalaus[0]

        elif alustus.tunniste == "Ympyrädiagrammi":
            varit = [Qt.red, Qt.blue, Qt.gray, Qt.green, Qt.yellow, Qt.black, Qt.magenta, Qt.cyan, Qt.darkRed, Qt.darkBlue, Qt.darkGray, Qt.darkGreen, Qt.darkYellow, Qt.darkMagenta, Qt.darkCyan] #Värit joilla värjätään lohkot
            yk = alustus.viivakoko #ympyrän koko
            r = yk / 2 #Ympyrän säde

            """Luodaan lista asteista ympyrällä joihin viivat tullaan piirtämään. Aloitetaan 90 asteesta, sillä tällöin 
            ensimmäinen viiva saadaan ympyrän keskipisteestä suoraan ylöspäin."""
            asteet = []
            summa = 0
            asteet.append(90)
            for i in alustus.ympyra_osuudet:
                summa += i[1]
                asteet.append(90-summa)

            """Värittää viivojen väliin jäävän osuuden eri väreillä - ympyrän eri segmentit."""
            pen = QPen()
            pen.setWidth(4)
            v = 0
            kpl = 500
            for n in range(len(asteet)):
                vari = varit[v]
                if n < len(asteet)-1:
                    for i in range(0,kpl,1):
                        pen.setColor(vari)
                        painter.setPen(pen)
                        line = QLineF(r,r,0,0)
                        line.setLength(r)
                        line.setAngle(asteet[n] - ((asteet[n]-asteet[n+1])/kpl)*i)
                        painter.drawLine(line)
                if v < len(varit)-1:
                    v += 1
                else:
                    v = 0

            """Piirtää ääriviivat ympyrälle ja rajat eri arvojen väleille (jakaa ympyrän osiin)."""
            pen = QPen()
            pen.setColor(Qt.black)
            pen.setWidth(4)
            painter.setPen(pen)
            painter.drawEllipse(0,0,yk,yk)

            n = 0
            for i in alustus.ympyra_osuudet:
                line = QLineF(r,r,0,0)
                line.setLength(r)
                line.setAngle(90-n)
                painter.drawLine(line)
                n += i[1]

            """Piirretään käytettyjen värien tunnisteet kuvaajaan."""
            i = 0
            v = 0
            s = 0
            pen = QPen()
            pen.setWidth(1)
            while i < len(alustus.ympyra_osuudet):
                vari = varit[v]
                pen.setColor(vari)
                painter.setPen(pen)
                painter.setBrush(QBrush(vari, Qt.SolidPattern))
                rect = QRectF(650, s, 15, 15)
                painter.drawRect(rect)

                if v < len(varit) - 1:
                    v += 1
                else:
                    v = 0
                i += 1
                s += 25

class GraafiView(QGraphicsView):

    """Luokka GraafiView luo näkymän kuvaajalle, lisää siihen luokan GraafiItem elementit ja lisää kuvaajaan siihen
    tulevat tekstiosuudet (otsikko, selitteet akseleille yms.)"""

    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.graafi = GraafiItem()
        self.scene.addItem(self.graafi)
        otsikkoteksti = "Piirretty graafi"
        self.setWindowTitle(otsikkoteksti)

        if alustus.tunniste == 'Viivadiagrammi':
            skaalausx = alustus.skaalaus[0]
            skaalausy = alustus.skaalaus[1]
            n = 0
            fontti = QFont()
            fontti.setPixelSize(15)
            metrics = QFontMetrics(fontti)
            y_merkki_max = metrics.boundingRect(str(alustus.yarvot[0])).width()

            """Asettaa x ja y -akselien väkästen kohdille niitä vastaavat numeriset arvot."""
            for i in range(0,alustus.viivakoko+100,100):
                x_merkki = str(alustus.xarvot[n])
                y_merkki = str(alustus.yarvot[n])

                x_merkin_pituus = metrics.boundingRect(x_merkki).width()
                y_merkin_pituus = metrics.boundingRect(y_merkki).width()

                tekstix = QGraphicsSimpleTextItem()
                tekstix.setText(x_merkki)
                tekstix.setFont(fontti)
                tekstix.setPos(alustus.minmax_x[0]*skaalausx+i - x_merkin_pituus/2,-alustus.minmax_y[0]*skaalausy+30)
                self.scene.addItem(tekstix)

                tekstiy = QGraphicsSimpleTextItem()
                tekstiy.setText(y_merkki)
                tekstiy.setFont(fontti)
                tekstiy.setPos(alustus.minmax_x[0]*skaalausx-30 - y_merkin_pituus,-alustus.minmax_y[0]*skaalausy-i-10)
                self.scene.addItem(tekstiy)
                n += 1

                if y_merkin_pituus > y_merkki_max: #Etsitään pisimmän Y-merkin pituus, jotta voidaan jatkossa asettaa Y-akselin selite oikealle kohdelle niin, että se ei peitä selitteitä.
                    y_merkki_max = y_merkin_pituus

            fontti = QFont()
            fontti.setPixelSize(20)
            metrics = QFontMetrics(fontti)

            """Asettaa graafiin y-arvojen keskiarvon"""
            if alustus.keskiarvo != None:
                keskiarvo_teksti = 'y-arvojen keskiarvo: ' + str(round(alustus.keskiarvo,2))
                ka = QGraphicsSimpleTextItem()
                ka.setText(keskiarvo_teksti)
                ka.setFont(fontti)
                ka.setPos(alustus.minmax_x[1]*skaalausx+30,-(alustus.minmax_y[1]*skaalausy)/2-40)
                erotus = alustus.minmax_y[1] - alustus.minmax_y[0]
                self.scene.addItem(ka)

            """Asettaa graafiin y-arvojen keskihajonnan"""
            if alustus.keskihajonta != None:
                hajonta_teksti = 'y-arvojen keskihajonta: ' + str(round(alustus.keskihajonta,2))
                hajonta = QGraphicsSimpleTextItem()
                hajonta.setText(hajonta_teksti)
                hajonta.setFont(fontti)
                hajonta.setPos(alustus.minmax_x[1]*skaalausx+30,-(alustus.minmax_y[1]*skaalausy)/2-15)
                self.scene.addItem(hajonta)

            """Asettaa graafiin selitetekstin datapisteiden kuviolle (punaiset ympyrät)."""
            selite_teskti = 'Annetut datapisteet:'
            selite = QGraphicsSimpleTextItem()
            selite.setText(selite_teskti)
            selite.setFont(fontti)
            selite.setPos(alustus.minmax_x[1]*skaalausx+30,-(alustus.minmax_y[1]*skaalausy)/2+10)
            self.scene.addItem(selite)

            """Asettaa käyttäjän antaman x-akselin selitteen x-akselin kohdalle"""
            if alustus.xakseli is not None:
                xakseli = QGraphicsSimpleTextItem()
                xakseli.setText(alustus.xakseli)
                xakseli.setFont(fontti)
                w = metrics.boundingRect(alustus.xakseli).width() #x-merkin pituus
                xakseli.setPos(alustus.minmax_x[0]*skaalausx + alustus.viivakoko/2 - w/2,-alustus.minmax_y[0]*skaalausy+60)
                self.scene.addItem(xakseli)

            """Asettaa käyttäjän antaman y-akselin selitteen y-akselin kohdalle"""
            if alustus.yakseli is not None:
                yakseli = QGraphicsSimpleTextItem()
                yakseli.setText(alustus.yakseli)
                yakseli.setFont(fontti)
                w = metrics.boundingRect(alustus.yakseli).width() #y-merkin pituus
                yakseli.setPos(alustus.minmax_x[0]*skaalausx - y_merkki_max -70, -alustus.minmax_y[0]*skaalausy -alustus.viivakoko/2 + w/2)
                yakseli.setRotation(270)
                self.scene.addItem(yakseli)

            """Asettaa käyttäjän antaman x-akselin asteikon selitteen graafiin"""
            if alustus.xasteikko is not None:
                xasteikko = QGraphicsSimpleTextItem()
                xasteikko.setText(alustus.xasteikko)
                xasteikko.setFont(fontti)
                xasteikko.setPos(alustus.minmax_x[1]*skaalausx+25,-alustus.minmax_y[0]*skaalausy)
                self.scene.addItem(xasteikko)

            """Asettaa käyttäjän antaman y-akselin asteikon selitteen graafiin"""
            if alustus.yasteikko is not None:
                yasteikko = QGraphicsSimpleTextItem()
                yasteikko.setText(alustus.yasteikko)
                yasteikko.setFont(fontti)
                w = metrics.boundingRect(alustus.yasteikko).width()
                yasteikko.setPos(alustus.minmax_x[0]*skaalausx -w/2 -10,-alustus.minmax_y[1]*skaalausy-40)
                self.scene.addItem(yasteikko)

            """Asettaa otsikon graafille"""
            fontti = QFont()
            fontti.setPixelSize(30)
            metrics = QFontMetrics(fontti)
            otsikko = QGraphicsSimpleTextItem()
            otsikko.setText(alustus.otsikko)
            otsikko.setFont(fontti)
            w = metrics.boundingRect(alustus.otsikko).width() #otsikon pituus
            otsikko.setPos(alustus.minmax_x[0]*skaalausx + alustus.viivakoko/2 - w/2, -alustus.minmax_y[1]*skaalausy - 70)
            self.scene.addItem(otsikko)

            self.setWindowState(Qt.WindowMaximized) #Asettaa piirretyn kuvion rajat näytön reunoille

        elif alustus.tunniste == 'Pylväsdiagrammi':
            skaalausx = alustus.skaalaus[0]
            skaalausy = alustus.skaalaus[1]

            n = 0
            fontti = QFont()
            fontti.setPixelSize(15)
            metrics = QFontMetrics(fontti)
            y_merkki_max = metrics.boundingRect(str(alustus.yarvot[0])).width() #Alusutus pisimmästä Y-merkistä

            """Asettaa y -akselien väkästen kohdille niitä vastaavat numeriset arvot."""
            for i in range(0,alustus.viivakoko + 100, 100):
                y_merkki = str(alustus.yarvot[n])
                y_merkin_pituus = metrics.boundingRect(y_merkki).width()

                tekstiy = QGraphicsSimpleTextItem()
                tekstiy.setText(y_merkki)
                tekstiy.setFont(fontti)

                if alustus.minmax_y[0] > 0 or (alustus.minmax_y[0] < 0 and alustus.minmax_y[1] > 0):
                    tekstiy.setPos(-y_merkin_pituus - 25, -alustus.minmax_y[1]*skaalausy + i - 10)

                elif alustus.minmax_y[1] < 0:
                    tekstiy.setPos(-y_merkin_pituus - 25, -alustus.minmax_y[0] * skaalausy - i - 10)

                if y_merkin_pituus > y_merkki_max: #Etsitään pisin Y-merkki, jotta Y-akselin selitte ei piirry arvojen päälle
                    y_merkki_max = y_merkin_pituus

                self.scene.addItem(tekstiy)
                n += 1

            """Asettaa x-akselille jokaista pylvästä vastaavan selitteen (datan x arvot)"""
            i = skaalausx/2
            if skaalausx < 18:
                fontti = QFont()
                fontti.setPointSizeF(skaalausx/2.5)
                metrics = QFontMetrics(fontti)

            for line in alustus.data:
                x_merkki = str(line[0])
                x_merkki_pituus = metrics.boundingRect(x_merkki).width()
                tekstix = QGraphicsSimpleTextItem()
                tekstix.setText(x_merkki)
                tekstix.setFont(fontti)
                tekstix.setRotation(-45)
                if alustus.minmax_y[0] < 0:
                    tekstix.setPos(i - x_merkki_pituus*0.7,-alustus.minmax_y[0]*skaalausy + x_merkki_pituus*0.7 + 5)
                else:
                    tekstix.setPos(i - x_merkki_pituus*0.7, x_merkki_pituus*0.7 + 5)
                self.scene.addItem(tekstix)
                i += skaalausx

            """Asettaa graafiin y-arvojen keskiarvon"""
            fontti = QFont()
            fontti.setPixelSize(20)
            if alustus.keskiarvo != None:
                keskiarvo_teksti = 'y-arvojen keskiarvo: ' + str(round(alustus.keskiarvo, 2))
                ka = QGraphicsSimpleTextItem()
                ka.setText(keskiarvo_teksti)
                ka.setFont(fontti)
                if alustus.minmax_y[0] > 0:
                    ka.setPos(alustus.viivakoko + 20, (-alustus.minmax_y[1] * skaalausy) / 2)

                elif alustus.minmax_y[0] < 0 and alustus.minmax_y[1] > 0:
                    if -alustus.minmax_y[0] > alustus.minmax_y[1]:
                        ka.setPos(alustus.viivakoko + 20,(-alustus.minmax_y[0] * skaalausy) / 2)
                    elif -alustus.minmax_y[0] < alustus.minmax_y[1]:
                        ka.setPos(alustus.viivakoko + 20, (-alustus.minmax_y[1] * skaalausy) / 2)

                elif alustus.minmax_y[1] < 0:
                    ka.setPos(alustus.viivakoko + 20, (-alustus.minmax_y[0] * skaalausy)/2)
                self.scene.addItem(ka)

            """Asettaa graafiin y-arvojen keskihajonnan"""
            if alustus.keskihajonta != None:
                hajonta_teksti = 'y-arvojen keskihajonta: ' + str(round(alustus.keskihajonta, 2))
                hajonta = QGraphicsSimpleTextItem()
                hajonta.setText(hajonta_teksti)
                hajonta.setFont(fontti)
                if alustus.minmax_y[0] > 0:
                    hajonta.setPos(alustus.viivakoko + 20, (-alustus.minmax_y[1] * skaalausy) / 2 +30)

                elif alustus.minmax_y[0] < 0 and alustus.minmax_y[1] > 0:
                    if -alustus.minmax_y[0] > alustus.minmax_y[1]:
                        hajonta.setPos(alustus.viivakoko + 20,(-alustus.minmax_y[0] * skaalausy) / 2 +30)
                    elif -alustus.minmax_y[0] < alustus.minmax_y[1]:
                        hajonta.setPos(alustus.viivakoko + 20, (-alustus.minmax_y[1] * skaalausy) / 2 +30)

                elif alustus.minmax_y[1] < 0:
                    hajonta.setPos(alustus.viivakoko + 20, (-alustus.minmax_y[0] * skaalausy)/2 +30)
                self.scene.addItem(hajonta)

            """Asettaa käyttäjän antaman y-akselin selitteen y-akselin kohdalle"""
            if alustus.yakseli is not None:
                yakseli = QGraphicsSimpleTextItem()
                yakseli.setText(alustus.yakseli)
                yakseli.setFont(fontti)
                metrics = QFontMetrics(fontti)
                w = metrics.boundingRect(alustus.yakseli).width()  #Selitteen pituus
                if alustus.minmax_y[0] > 0:
                    yakseli.setPos(-y_merkki_max - 80, -alustus.minmax_y[1]*skaalausy/2 + w/2)
                elif alustus.minmax_y[0] < 0 and alustus.minmax_y[1] > 0:
                    yakseli.setPos(-y_merkki_max - 80, -alustus.minmax_y[0] * skaalausy - alustus.viivakoko / 2 + w / 2)
                elif alustus.minmax_y[1] < 0:
                    yakseli.setPos(-y_merkki_max - 80, -alustus.minmax_y[0]*skaalausy/2 + w/2)
                yakseli.setRotation(270)
                self.scene.addItem(yakseli)

            """Asettaa käyttäjän antaman x-akselin asteikon selitteen graafiin"""
            fontti = QFont()
            fontti.setPixelSize(20)
            metrics = QFontMetrics(fontti)
            if alustus.xasteikko is not None:
                xasteikko = QGraphicsSimpleTextItem()
                xasteikko.setText(alustus.xasteikko)
                xasteikko.setFont(fontti)
                xasteikko.setPos(alustus.viivakoko+20,-10)
                self.scene.addItem(xasteikko)

            """Asettaa käyttäjän antaman y-akselin asteikon selitteen graafiin"""
            if alustus.yasteikko is not None:
                yasteikko = QGraphicsSimpleTextItem()
                yasteikko.setText(alustus.yasteikko)
                yasteikko.setFont(fontti)
                w = metrics.boundingRect(alustus.yasteikko).width()
                if alustus.minmax_y[0] > 0 or (alustus.minmax_y[0] < 0 and alustus.minmax_y[1] > 0):
                    yasteikko.setPos(-w/2,-alustus.minmax_y[1]*skaalausy -50)
                elif alustus.minmax_y[1] < 0:
                    yasteikko.setPos(-w,-alustus.minmax_y[0]*skaalausy +20)
                self.scene.addItem(yasteikko)

            """Asettaa otsikon graafille"""
            fontti = QFont()
            fontti.setPixelSize(30)
            metrics = QFontMetrics(fontti)
            otsikko = QGraphicsSimpleTextItem()
            otsikko.setText(alustus.otsikko)
            otsikko.setFont(fontti)
            w = metrics.boundingRect(alustus.otsikko).width()  # otsikon pituus
            if alustus.minmax_y[0] > 0 or (alustus.minmax_y[0] < 0 and alustus.minmax_y[1] > 0):
                otsikko.setPos(alustus.viivakoko/2 - w/2, -alustus.minmax_y[1] * skaalausy - 80)
            elif alustus.minmax_y[1] < 0:
                otsikko.setPos(alustus.viivakoko / 2 - w / 2, - 80)
            self.scene.addItem(otsikko)

            if alustus.minmax_y[0] > 0 or (alustus.minmax_y[0] < 0 and alustus.minmax_y[1] > 0): #Asettaa graafin näkymän näytölle
                self.setWindowState(Qt.WindowMaximized) #Asettaa piirretyn kuvion rajat näytön reunoille

            elif alustus.minmax_y[1] < 0:
                self.setWindowState(Qt.WindowMaximized) #Asettaa piirretyn kuvion rajat näytön reunoille


        elif alustus.tunniste == "Ympyrädiagrammi":
            fontti = QFont()
            fontti.setPixelSize(15)
            metrics = QFontMetrics(fontti)

            """Asetetaan datan x-akselin ja y-akselin arvot kuvaajaan käytettyjen värien kohdalle."""
            s = 0
            for line in alustus.ympyra_osuudet:
                tunnistex = QGraphicsSimpleTextItem()
                tekstix = str(line[0]) + ","
                tunnistex.setText(tekstix)
                tunnistex.setFont(fontti)
                w = metrics.boundingRect(str(line[0])).width()

                tunnistey = QGraphicsSimpleTextItem()
                tekstiy = "Arvo: " + str(line[2])
                tunnistey.setText(tekstiy)
                tunnistey.setFont(fontti)
                tunnistex.setPos(670, s)
                tunnistey.setPos(680 + w, s)
                s += 25

                self.scene.addItem(tunnistex)
                self.scene.addItem(tunnistey)

            """Asettaa otsikon graafille"""
            fontti = QFont()
            fontti.setPixelSize(30)
            otsikko = QGraphicsSimpleTextItem()
            otsikko.setText(alustus.otsikko)
            otsikko.setFont(fontti)
            metrics = QFontMetrics(fontti)
            w = metrics.boundingRect(alustus.otsikko).width()
            otsikko.setPos((alustus.viivakoko-w)/2, -80)
            self.scene.addItem(otsikko)

            self.setWindowState(Qt.WindowMaximized) #Asettaa piirretyn kuvion rajat näytön reunoille

        self.setScene(self.scene)
        self.setWindowState(Qt.WindowMaximized) #Asettaa piirretyn kuvion rajat näytön reunoille
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    alustus = Alustus()
    gra = Grafiikka()
    gra.kysySyöte()
    sys.exit(app.exec_())

