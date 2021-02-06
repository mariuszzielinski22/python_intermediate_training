from oop_sda_1.cat import Cat


def main():
    cat_object = Cat("Filemon")
    sound: str = cat_object.make_sound()
    print(sound)

if __name__ == "__main__":
    main()
