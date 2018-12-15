# miltiple inheritance in python but not in java
# son access both father's and mother's feature, so it ia multiple inheritance
# MRO = method resolution order
# GoF
# if call from object by default self is pass
# if call from class then have to pass object, eg Mother.speak(s)

class Father:
    def speak(self):
        return 'Nepali'

    def bp(self):
        return True


class Mother:
    def speak(self):
        return 'Newari'


class Son(Father, Mother):  # here first Son class -> Father class -> Mother class ,
    pass


# class Son2(Mother, Father):  # here first Son class -> Mother class -> Father class
#     pass


s = Son()
print(s.speak())
print(s.bp())
print(Son.mro())
print(Mother.speak(s))
print(Father.speak(s))

# s2 = Son()
# print(s2.speak())
# print(s2.bp())
# print(Son2.mro())
