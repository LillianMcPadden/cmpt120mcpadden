# Old_MacDonald.py
# This function prints the lyrics to Old McDonald had a farm
def farm():
    print('Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!')

def song(animal, noise):
    farm()
    print('And on the farm he had a ' + animal, 'Ee-igh, Ee-igh, Oh!')
    print('with a ' + noise + ', ' + noise + ' here and a ' + noise + ', ' + noise + ' there.' )
    print('Here a ' + noise + ', there a ' + noise + ', everywhere a ' + noise +', ' + noise) 
    farm()

def main():
    song('cow', 'moo')
    print()
    song('horse', 'neigh')
    print()
    song('pig', 'oink')
    print()
    song('duck', 'quack')
    print()
    song('sheep', 'baah')
    print ()

main()

