import datetime
import time

# Stocker les couleurs d'affichages:
red = "\033[0;31m"
white = "\033[0m"

# Obtenir le temps actuel en secondes depuis l'époque:
second = time.time()
second_str = str(second)

# Recupere la date actuel:
current_date = datetime.datetime.now()

# Formate et affiche la date:
print(f"{red}Seconds since January 1, 1970:{white} ", end="")
print(f"{second_str[0]},{second_str[1:4]},{second_str[4:7]},{second_str[7:15]}", end="")
print(" or {0:.2e} in scientific notation".format(second))

print(current_date.strftime("%B %d %Y"))
