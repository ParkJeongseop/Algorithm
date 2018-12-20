building, street = map(int, input().split())

streets = []

for i in range(street+1):
    streets.append(list(map(int, input().split())))

low_k = 0
high_k = 1000

while True:
    is_visited = [False for i in range(building)]
    location = 0
    