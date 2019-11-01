'''
Two bicyclist start moving from different cities heading to meet each other somewhere in the middle (not exactly since they travel with different speed).

The road is laid in straight line between two cities.

You will be given the distance between cities S (in kilometers) and speed values for two bicyclists (A and B in kilometers per hour). Your task is to find their meeting point (its distance from the first of cities).

Input data will have the number of test-cases in the first line.
Next lines will contain three values each S A B.
Answer should contain the distances between first city and rendezvous point (i.e. distance travelled by first cyclist before they meet), separated with spaces.



***If have other process lets share***
'''



def bicycle_race():
    x = input()
    for i in range(int(x)):
        a = input()
        b = a.split(' ')
        c = int(b[0])/(int(b[1])+int(b[2]))
        d = int(b[0])-c*(int(b[1])+int(b[2]))
        e = d/(int(b[1])+int(b[2]))
        print((c+e)*int(b[1]),end=' ')

bicycle_race()
