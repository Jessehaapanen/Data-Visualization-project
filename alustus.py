import traceback


class Alustus():

    """Luokka Alustus luo olion ja valmistelee kaiken tarvittavan kuvaajan piirtämistä varten ohjelman käyttäjän antamien syötteiden perusteella."""

    def __init__(self):
        self.otsikko = None #Kuvion otsikko
        self.piirtook = 1 #1 jos kuvio voidaan piirtää, muuten 0
        self.tunniste = None #Kuvion "yleisnimi" (joko viiva-, pylväs- tai ympyrädiagrammi)
        self.grid = None #Joko Kyllä tai Ei riippuen haluaako käyttäjä piirtää kuvaajaan Gridin
        self.gridSkaalaus = 1 #Käyttäjän antaman gridin skaalauskerroin
        self.dataNimi = None #Käyttäjän antama datan nimi/polku
        self.dataFile = None #Avattu tiedosto
        self.xakseli = None #Käyttäjän antama X-akselin selite
        self.yakseli = None #Käyttäjän antama Y-akselin selite
        self.xasteikko = None #Käyttäjän antama X-akselin asteikon selite
        self.yasteikko = None #Käyttäjän antama Y-akselin asteikon selite
        self.data = None #Listamuodossa oleva siistitty data
        self.keskiarvo = None #Datan Y-arvojen keskiarvo
        self.keskihajonta = None #Datan Y-arvojen keskihajonta
        self.minmax_x = None #X-arvojen maximi ja minimi. Muodossa: (min,max)
        self.minmax_y = None #Y-arvojen maximi ja minimi. Muodossa: (min,max)
        self.viivakoko = 600 #Kuvion koko
        self.skaalaus = None #Datan perusteella laskettu skaalauskerroin
        self.xarvot = [] #Kuviossa X-akselin kohdilla olevien väkästen arvot
        self.yarvot = [] #Kuviossa Y-akselin kohdilla olevien väkästen arvot
        self.grid_valit = [] #Kohdat kuviossa joihin gridin viivat piirretään
        self.ympyra_osuudet = [] #Ympyrädiagrammin eri lohkojen koot asteina, muotoa (x-arvo, osuus, y-arvo)

    """Avaa ja asettaa halutun tiedoston olion kenttään."""
    def avaaTiedosto(self, nimi):
        try:
            file = open(nimi)
            self.dataFile = file
            self.piirtook = 1
        except:
            self.piirtook = 0
            TypeError

    """Käy annetun tiedoston datan läpi, muodostaa siitä listan."""
    def lueData(self, data):
        self.data = []
        try:
            for line in data:
                line = line.strip().split(" ")
                try:
                    if self.tunniste == "Viivadiagrammi":
                        lisays = (float(line[0]), float(line[1]))

                    elif self.tunniste == "Pylväsdiagrammi" or self.tunniste == "Ympyrädiagrammi":
                        lisays = (str(line[0]), float(line[1]))

                    self.data.append(lisays)
                except:
                    pass
        except:
            pass

    """Laskee annetusta datasta y-arvojen keskiarvon."""
    def laskeKa(self, data):
        sum = 0
        try:
            for line in data:
                sum += line[1]
            ka = sum / len(data)
            self.keskiarvo = ka

        except:
            pass

    """Laskee annetusta datasta y-arvojen keskihajonnan."""
    def laskeKeskihajonta(self, data, keskiarvo):
        sum = 0
        try:
            for line in data:
                sum += (line[1] - keskiarvo)**2
            hajonta = (sum / (len(data)-1))**(1/2)
            self.keskihajonta = hajonta

        except:
            pass

    """Etsii annetusta datasta x ja y -arvojen minimin sekä maksimin ja asettaa nämä olion kenttiin."""
    def maxmin(self, data):
        try:
            if self.tunniste == "Viivadiagrammi":
                max_x = data[0][0]
                min_x = data[0][0]
                max_y = data[0][1]
                min_y = data[0][1]

                for line in data:
                    if line[0] > max_x:
                        max_x = line[0]

                    if line[0] < min_x:
                        min_x = line[0]

                    if line[1] > max_y:
                        max_y = line[1]

                    if line[1] < min_y:
                        min_y = line[1]

                self.minmax_x = (min_x, max_x)
                self.minmax_y = (min_y, max_y)

            elif self.tunniste == "Pylväsdiagrammi" or "Ympyrädiagrammi":
                max_y = data[0][1]
                min_y = data[0][1]

                for line in data:
                    if line[1] >= max_y:
                        max_y = line[1]

                    if line[1] <= min_y:
                        min_y = line[1]
                self.minmax_y = (min_y, max_y)

        except:
            pass

    """Laskee annetun datan minimien ja maksimien perusteella skaalauskertoimen kuvaajan piirtämistä varten."""
    def laskeSkaalaus(self, minmaxx, minmaxy):
        try:
            koko = self.viivakoko
            if self.tunniste == "Viivadiagrammi":
                erotus_x = minmaxx[1] - minmaxx[0]
                erotus_y = minmaxy[1] - minmaxy[0]
                skaalaus_x = koko / erotus_x
                skaalaus_y = koko / erotus_y
                self.skaalaus = (skaalaus_x, skaalaus_y)

            elif self.tunniste == "Pylväsdiagrammi":
                skaalaus_x = koko / len(self.data)
                if self.minmax_y[0] > 0:
                    skaalaus_y = koko / self.minmax_y[1]

                elif self.minmax_y[0] < 0 and self.minmax_y[1] > 0:
                    erotus = self.minmax_y[1] - self.minmax_y[0]
                    skaalaus_y = koko / erotus

                elif self.minmax_y[1] < 0:
                    skaalaus_y = -(koko / self.minmax_y[0])

                self.skaalaus = (skaalaus_x, skaalaus_y)

        except:
            pass

    """Laskee käyttäjän antaman skaalauskertoimen avulla välit, joihin gridin viivat tullaan piirtämään"""
    def laskeGridSkaalaus(self):
        self.grid_valit = []
        try:
            vali = self.viivakoko / (10 * self.gridSkaalaus)
            if self.tunniste == 'Viivadiagrammi' and self.gridSkaalaus >0:
                sumvali = 0
                while sumvali <= self.viivakoko:
                    self.grid_valit.append(sumvali)
                    sumvali += vali

            elif self.tunniste == "Pylväsdiagrammi" and self.gridSkaalaus >0:
                if self.minmax_y[0] < 0:
                    sumvali = 0
                    while sumvali <= self.viivakoko:
                        self.grid_valit.append(sumvali)
                        sumvali += vali
                else:
                    sumvali = 0
                    while sumvali <= self.viivakoko:
                        self.grid_valit.append(sumvali)
                        sumvali += vali
        except:
            pass

    """Laskee annetusta datasta arvot, jotka näkyvät piirretyssä diagrammissa x ja y-akselien pienten väkästen kohdilla
    (helpottavat piirrettyjen arvojen suuruuden havainnointia)."""
    def akselienArvot(self, minmaxx, minmaxy):
        self.xarvot = []
        self.yarvot = []
        try:
            kpl = self.viivakoko / 100 + 1
            jakaja = self.viivakoko / 100
            if self.tunniste == "Viivadiagrammi":
                erotus_x = minmaxx[1] - minmaxx[0]
                erotus_y = minmaxy[1] - minmaxy[0]
                valix = erotus_x / jakaja
                valiy = erotus_y / jakaja
                for n in range(0, int(kpl)):
                    self.xarvot.append(round(minmaxx[0] + valix*n,2))
                    self.yarvot.append(round(minmaxy[0] + valiy*n,2))

            elif self.tunniste == "Pylväsdiagrammi":
                if self.minmax_y[0] > 0:
                    valiy = self.minmax_y[1]/jakaja
                    for n in range(0,int(kpl)):
                        self.yarvot.append(round(minmaxy[1] - valiy*n,2))

                elif self.minmax_y[0] < 0 and self.minmax_y[1] > 0:
                    erotus = minmaxy[1] - minmaxy[0]
                    valiy = erotus / jakaja
                    for n in range(0,int(kpl)):
                        self.yarvot.append(round(minmaxy[1] - valiy*n,2))

                elif self.minmax_y[1] < 0:
                    valiy = -(self.minmax_y[0] / jakaja)
                    for n in range(0, int(kpl)):
                        self.yarvot.append(round(minmaxy[0] + valiy * n, 2))
        except:
            pass

    """Laskee jokaista datan y-arvon suuruutta vastaavan asteen ympyrydiagrammia varten (lisää mukaan sekä positiiviset että negatiiviset arvot)."""
    def ympyraOsuudet(self, data):
        self.ympyra_osuudet = []
        sum = 0
        try:
            for line in data: #Lasketaan kaikki datan arvot yhteen
                try:
                    if line[1] >0:
                        sum += line[1]
                    else:
                        sum -= line[1]
                except:
                    pass

            for line in data:
                try:
                    if line[1] >0:
                        osuus = (360/sum)*line[1]
                        self.ympyra_osuudet.append((line[0],osuus, line[1])) #Lisätään listaan mukaan myös X-arvo, helpottaa jatkotoimenpiteitä kuviota piirrettäessä.
                    else:
                        osuus = (360/sum)*(-line[1])
                        self.ympyra_osuudet.append((line[0],osuus, line[1])) #Lisätään listaan mukaan myös X-arvo, helpottaa jatkotoimenpiteitä kuviota piirrettäessä.
                except:
                    pass
        except:
            pass


