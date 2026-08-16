items = {"apple", "banana"}

items.add("orange")
#adds orange in the set(items)
print(items)

items.update(["mango", "peach"])
#adds multiple values(mango and peach) in the set(items)
print(items)

#in set the values are added in the set on it's own means randomly no order is defined for the values to be added in the set

basket = {"apple", "banana", "tomato", "brinjal"}

basket.remove("banana")
#removes value(banana) from the set(basket)
#gives error for the wrong spelling of value(banana) inserted
print(basket)

basket.discard("bananae")
#it also removes values from the set(basket)
#but if wrong spelling of value is inserted in the command like(bananae)
#it will not remove any value from the set(basket)
#also it will not give any error in output for wrong spelling(bananae)
print(basket)

basket.pop()
#removes any value from the set(basket) randomly
print(basket)

a = basket.pop()
print(basket)
print(a)
#this also removes any value from the set(basket) but this command gives the value in output that which value is removed from the set(basket) in terms of a

print(len(basket))
#gives length of the set(basket)

basket.clear()
#clears the whole set(basket)
print(basket)