person = {"name": "John", "age": 30, "city": "New York"}

person["name"] = 'PappuKurla'
person['age'] = 56
person["city"] = "Kurla"
for key,value in person.items():
    print(key, ":", value)