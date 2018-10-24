
prices = {
    'apple' : 30,
    'orange' : 60,
    'banana' : 11
}

print(prices['apple']) # can raise error !

del prices['apple']
print(prices)

print(prices.get("XD")) # returns default
print(prices.keys())
print(prices.values())
