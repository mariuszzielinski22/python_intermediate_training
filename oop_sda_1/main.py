from oop_sda_1.cat import Cat
from oop_sda_1.dog import Dog


def main():
    cat_object = Cat("Filemon")
    cat_object_2 = Cat("Mruczek", "miałmiał")
    cat_object_3 = Cat("Pipak")
    cat_object_4 = Cat("Jarosław")
    dog_object = Dog("Burek", "Hauhau")

    # cats = [cat_object, cat_object_2, cat_object_3, cat_object_4]
    animals = []
    animals.append(cat_object)
    animals.append(cat_object_2)
    animals.append(cat_object_3)
    animals.append(cat_object_4)
    animals.append(dog_object)

    for animal in animals:
        sound = animal.make_sound()
        print(sound)

    # cat_object.eat_mouse()
    # cat_object.eat_mouse()
    # cat_object.eat_mouse()

    # print("Teraz będzie żarł drugi kot")

    # cat_object_2.eat_mouse()


# zmienna sound jest stringiem

if __name__ == "__main__":
    main()
