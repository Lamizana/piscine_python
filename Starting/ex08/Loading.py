# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alamizan <alamizan@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/10 10:12:56 by alamizan          #+#    #+#              #
#    Updated: 2024/09/10 10:24:30 by alamizan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_tqdm(lst: range) -> None:
    """
    Copie de la fonction tqdm avec l'opérateur yield
    """

    counter = 0
    total = len(lst)
    ncols = 64
    for i in lst:
        yield i
        counter += 1
        progress = counter / total
        bar_length = int(ncols * progress)
        bar = "=" * bar_length + "#" * (ncols - bar_length)
        print(f"\r{int(progress * 100)}%|[{bar}]| {counter}/{total}", end="")
