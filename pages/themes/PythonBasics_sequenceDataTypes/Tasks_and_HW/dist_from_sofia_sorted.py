from operator import itemgetter

distances_from_sofia = [
    ("Bansko", 97),
    ("Brussels", 1701),
    ("Alexandria", 1403),
    ("Nice", 1307),
    ("Szeged", 469),
    ("Dublin", 2479),
    ("Palermo", 987),
    ("Moscow", 1779),
    ("Oslo", 2098),
    ("London", 2019),
    ("Madrid", 2259),
]

selected_distances = []
for t in distances_from_sofia:
    if(t[1] < 1500):
        selected_distances.append(t)

print("Distances bellow 1500 km from Sofia are:")
for t in sorted(selected_distances, key=itemgetter(1)):
    print("{} - {}".format(t[0], t[1]))
