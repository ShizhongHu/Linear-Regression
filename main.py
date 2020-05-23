mainarray = []
array = []
arrayone = [[], []]
arraytwo = []

numberofcoordinates = int(input("How many coordinates are there? "))

i = 0

while i < numberofcoordinates:
    xcoordinate = int(input("Enter the x coordinate of a point: "))
    array.append(xcoordinate)
    ycoordinate = int(input("Enter the y coordinate of a planet "))
    array.append(ycoordinate)
    mainarray.append(array)
i += 1


summationofx = 0
summationofxsquared = 0
summationofy = 0
summationofxy = 0

for y in range(len(mainarray)):
    summationofx += mainarray[y][0]
    summationofxsquared += (mainarray[y][0])*(mainarray[y][0])
    summationofy += mainarray[y][1]
    summationofxy += mainarray[y][0]*mainarray[y][1]


arrayone[0].append(numberofcoordinates)
arrayone[0].append(summationofx)
arrayone[1].append(summationofx)
arrayone[1].append(summationofxsquared)

arraytwo.append(summationofy)
arraytwo.append(summationofxy)

# arrayone[0][0]*b + arrayone[0][1]*c = arraytwo[0]
# arrayone[1][0]*b + arrayone[1][1]*c = arraytwo[1]
# Solve for b and c
# y = cX + b , where c is the gradient and b is the y-intercept of the best fit line.








