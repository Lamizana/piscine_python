# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alamizan <alamizan@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/10 10:44:00 by alamizan          #+#    #+#              #
#    Updated: 2024/09/10 10:58:28 by alamizan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(1000)):
  sleep(0.005)
print()

for elem in tqdm(range(1000)):
  sleep(0.005)
print()