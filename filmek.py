from Film import Film

def fajlbeolvasas():
    slista = []
    fajlom = open("film.txt", "r", encoding = "UTF-8")
    fajlom.readline()
    lista = fajlom.readlines()
    fajlom.close()
    for i in range(0, len(lista), 1):
        aktsor: int = lista[i].strip()
        print(aktsor)
        sor_lista = aktsor.strip()
        sor_lista = aktsor.split(";")
        print(sor_lista[0])
        print(sor_lista[1])
        print(sor_lista[2])
        print(sor_lista[3])
        print(sor_lista[4])
        film = Film(sor_lista[0], sor_lista[1], sor_lista[2], sor_lista[3], sor_lista[4])
        slista.append(film)

    for i in range(0, len(slista), 1):
        print(f"{slista[i].snev}, {slista[i].srendezo}, {slista[i].sfoszereplo}, {slista[i].sev}, {slista[i].sperc}")
    return slista

def legrovidebb_film(lista):
    for i in range(0, len(lista), 1):
        x = min(lista[i].sperc)
        film = lista[i].snev
    print(x, film)
    return lista[i]

def film110(lista):
    for i in range(0, len(lista), 1):
        