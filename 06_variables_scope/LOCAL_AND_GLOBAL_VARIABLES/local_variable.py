#CODE-1

x = 78          #global variable

def value():
    x = 62      #local variable
    print(x)

value()        #prints x = 62 due to local variable
print(x)       #prints x = 78 due to global variable


#CODE-2

x = 78          #global variable

def value():
    global x  #changes or modify the global variable value by local variable value
    x = 89    #local variable
    print(x)

value()       #prints x = 89
print(x)      #prints x = 89