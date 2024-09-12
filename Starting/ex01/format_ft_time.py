import datetime
import time

# Obtenir le temps actuel en secondes depuis l'époque:
second = time.time()
sec = str(second)

# Recupere la date actuel:
current_date = datetime.datetime.now()

# Formate et affiche la date:
print("Seconds since January 1, 1970: ", end="")
print(f"{sec[0]},{sec[1:4]},{sec[4:7]},{sec[7:15]}", end="")
print(" or {0:.2e} in scientific notation".format(second))

print(current_date.strftime("%b %d %Y"))
