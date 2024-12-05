#####################################################################
# Programme Python : Data class [Module Dot]                        #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################
# Importations de fonctions externes :
from new_student import Student


#####################################################################
# definitions locales de fonctions :
def main() -> int:
    """
    Fonction programme principal.
    """

    student = Student(name = "Edward", surname = "agle")
    print(student)
    return (0)


#####################################################################
if __name__ == "__main__":
    main()