def greet( name = "User", city = "Delhi"):     #default value of name and city are assigned
    print("Hello", name, city)

greet()
greet("Om Saini")
greet("Meerut", "Om Saini")  # this will print city in name and name in city so we have to give variable name in this case
greet(city = "Meerut", name = "Om Saini")  #by this no sequence matters as variables name are given