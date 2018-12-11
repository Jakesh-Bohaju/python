# these function call magic function

class Time:

    def __init__(self, hr, mins, sec):
        self.hr = hr
        self.mins = mins
        self.sec = sec

    def __str__(self):
        return '{}:{}:{}'.format(self.hr, self.mins, self.sec)

    def __add__(self, other):
        # print(self)
        # print(other)

        sec = self.sec + other.sec
        mins = self.mins + other.mins
        hr = self.hr + other.hr

        if sec > 60:
            mins = mins + 1
            sec = sec - 60

        if mins > 60:
            hr = hr + 1
            mins = mins - 60

        return Time(hr, mins, sec)

    def __sub__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __divmod__(self, other):
        pass


t1 = Time(1, 5, 3)
t2 = Time(10, 25, 3)
print(t1)
print(t2)
print(t1 + t2)
