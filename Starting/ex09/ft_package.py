# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_package.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alamizan <alamizan@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/10 14:51:50 by alamizan          #+#    #+#              #
#    Updated: 2024/09/10 16:16:20 by alamizan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def count_in_list(lst: list, word: str) -> int:
    """
    Compte le nombre d element donne dans une liste
    """

    count = 0
    if (lst is None or word is None):
        return (count)
    
    for name in lst:
        if name == word:
            count += 1       
    return (count)
