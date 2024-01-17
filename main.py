import filmek


filmek_lista = filmek.fajlbeolvasas()

legrov = filmek.legrovidebb_film(filmek_lista)
print(f"A legrövidebb film címe: {legrov}")