import bottle, model

vislice = model.Vislice()

#Ta igra je namenjena testiranju
#id_testne_igre = vislice.nova_igra()
#(testna_igra, poskus) = vislice.igre[id_testne_igre]
#
##Dodajmo teste v testno
#testna_igra.ugibaj("a")
#testna_igra.ugibaj("b")
#testna_igra.ugibaj("c")


@bottle.get('/')
def prva_stran():
    return bottle.template('index.tpl')

@bottle.post('/igra/')
def zacni_novo_igro():
    #Naredi novo igro
    id_igre = vislice.nova_igra()
    #Preusmeri na naslov za igranje nove igre
    bottle.redirect('/igra/{}'.format(id_igre))

@bottle.get('/igra/<id_igre:int>')
def prikazi_igro(id_igre):
    (igra, poskus) = vislice.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra, id_igre = id_igre, poskus=poskus)

@bottle.post('/igra/<id_igre:int>')
def ugibaj_crko(id_igre):
    crka = bottle.request.forms.getunicode('poskus')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/{}'.format(id_igre))

bottle.run(debug=True, reloader=True)