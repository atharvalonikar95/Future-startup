class speederror(Exception):
    def __init__(self,msg) :
        super().__init__(msg)
        # print(msg)

def ridingspeed(speed):
    if speed>80:
        raise speederror("speed limit exceeded ")
    else:
        print("you are below speed limit")
print("start ride")
try:
    speed=int(input("Max speed reached is : "))

except ValueError:
    print("add integer data")
    speed=int(input("Max speed reached is: "))
    
try:
    ridingspeed(speed)
except speederror:
    print("please reduce speed")
try:
    try:
        speed=int(input("Reduced  speed  is: "))
        print("add integer data")
    except ValueError:
        print("add integer data")
        speed=int(input("Reduced  speed  is: "))

    ridingspeed(speed)
except speederror:
    print("End ride")
else:
    print("keep riding safely")

    