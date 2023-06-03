print("Witaj w konwerterze plików [.xml], [.json], oraz [.yml]!")
x = input("\nPodaj ścieżkę pliku (wraz z jego rozszerzeniem): ")
y = input("\nPodaj ścieżkę pliku oraz rozszerzenie w jakim chciał(a) byś aby plik został zapisany: ")
file_name, file_extension = os.path.splitext(x)  # wypisuje ścieżkę pliku i jego rozszerzenie
file_name_new, file_extension_new = os.path.splitext(y)  # nowa ścieżka wygenerowanego pliku


def checkfile():
    file = os.path.isfile(x)  # Sprawdza czy ścieżka pliku jest poprawna
    if file == False:
        print("\nPodałeś złą ścieżkę pliku! Spróbuj ponownie.")
    else:
        print("\nPodałeś prawidłową ścieżkę pliku. Konwertowanie...")
    return x, y
