# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alamizan <alamizan@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/10 15:59:07 by alamizan          #+#    #+#              #
#    Updated: 2024/09/10 16:06:31 by alamizan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ft_package import count_in_list

def main() -> int:
    """
    Fonction programme principal
    """

    print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
    print(count_in_list(["toto", "tata", "toto"], "tata")) # output: 0
    return (0)


if __name__ == "__main__":
    main()
