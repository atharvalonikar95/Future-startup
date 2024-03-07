# def count_ways_to_climb_stairs(n):
#     if n <= 1:

def ways(n):
    if n<=1:
        return 1
        
    return ways(n-1)+ ways(n-2)

stairs=int(input("Enter number of stairs"))
print(ways(stairs))