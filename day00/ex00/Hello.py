ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
ft_tuple = list(ft_tuple)
ft_tuple[1] = "France!"
ft_tuple = tuple(ft_tuple)
ft_set = list(ft_set)
ft_set[0] = "Hello"
ft_set[1] = "Paris!"
ft_set = set(ft_set)
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
