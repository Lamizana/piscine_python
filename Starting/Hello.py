
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# your code here
world = "World!"
country_of_your_campus = "France!"
city_of_your_campus = "Angouleme!"
name_of_your_campus = "42Angouleme!"

ft_list.pop()
ft_list.append(world)

ft_tuple = ("Hello", country_of_your_campus)

ft_set.discard('tutu!')
ft_set.add(city_of_your_campus)

ft_dict['Hello'] = name_of_your_campus

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)