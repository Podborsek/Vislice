import model

def izpis_igre(igra):
    znane = igra.pravilni_del_gesla()
    napacne = igra.nepravilni_ugibi()
    se = model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()
    #niz = "Neznana beseda: {} \nNapačni ugibi: {}\nImate še {} ugibov.".format(znane,napacne,se)
    niz = (
        "\n"
        "========================\n"
        "------------------------\n"
        "Neznana beseda: {} \n"
        "Napačni ugibi: {}\n"
        "Imate še {} ugibov.\n"
        "========================\n"
    ).format(znane,napacne,se)
    return niz

def izpis_zmage(igra):
    resitev = igra.geslo
    return "Čestitamo, pravilno ste uganili besedo {}!".format(resitev)

def izpis_poraza(igra):
    return "Ha ha, idiot, niti {} nisi uganil!".format(igra.geslo)

#Input
def zahtevaj_vnos():
    return input("Napiši črko da ugibaš:")

def prever_vnost(vnos):
    '''Funkcija vrne True ce je vnos primere, drugače False '''
    if len(vnos) != 1:
        print("Neveljaven vnost! Napiši točno eno črko")
        return False
    else:
        return True

#Izvajanje umesnika
def zazeni_umesnik():
    igra = model.nova_igra()

    while True:
        #Izpišemo stanje
        print(izpis_igre(igra))
        
        #Igralec ugiba
        poskus = zahtevaj_vnos() #Se pride
        igra.ugibaj(poskus)

        #Preverimo če je igre konec
        if igra.poraz():
            print(izpis_poraza(igra))
            return
        elif igra.zmaga():
            print(izpis_zmage(igra))
            return
    
    return



zazeni_umesnik()