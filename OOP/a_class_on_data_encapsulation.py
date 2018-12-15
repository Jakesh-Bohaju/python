# private
# public
# protected

class Father:
    def speak(self):
        return 'Nepali'

    def bp(self):
        return True


class Mother:
    def speak(self):
        return 'Newari'


class Son(Father, Mother):

    def __i_am_private(self):  # double underscore is default private
        return 'Yes I am'

    def hey_i_am_public(self):
        print(self.__i_am_private())


s = Son()
print(s.speak())
print(s.bp())
print(Son.mro())
print(Mother.speak(s))
# print(s.__i_am_private()) # it cant done because __i_am_private is private, private can only access on the same class
s.hey_i_am_public()  # its public so can access through object
