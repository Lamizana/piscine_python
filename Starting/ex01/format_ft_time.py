import datetime
import time

# Obtenir le temps actuel en secondes depuis l'époque:
second = time.time()

second_str = str(second)
print(second)

print(f"Seconds since January 1, 1970: {second_str[0]},{second_str[1:4]},{second_str[5:8]},{second_str[9:11]}{second_str[12:16]} ")
print(" or {0:.2e} in scientific notation".format(second))

# Recupere la date actuel:
current_date = datetime.datetime.now()

# Formate et affiche la date:
print(current_date.strftime("%B %d %Y"))
