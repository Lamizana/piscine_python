#####################################################################
# Programme Python Type                                             #
# auteur : A.Lamizana, Angouleme, 2224                              #
# OOP/ex10/main.py                                                  #
#####################################################################
from S1E7 import Baratheon, Lannister

def main() -> int:
    """
    Fonction programme principal.
    """

    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", False)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")


#####################################################################
if __name__ == "__main__":
    main()