print("Program starting")
print("")
Feed = input("insert starting point: ")
PointStart = int(Feed)
Feed = input("insert ending point: ")
PointStop = int(Feed)
Feed = input("Insert inspection point: ")
pointInspect = int(Feed)

Run = True

if(PointStart >= PointStop):
    print("Starting point value must be less than the stopping point value.")
    Run = False
if((PointStart > PointInspect) or (PointInspect > PointStop)):
    print("Inspection value must be within the range of start and stop.")
    Run = False

if(Run):
    print("First loop - inspection with break")
    for i in range(PointStart, PointStop):
        if(i == PointInspect):
            break
        else:
            print(i,  end=' ')
    print("")
    print("Second loop - inspection with continue:")
    for i in range(PointStart, PointStop):
        if(i == PointInspect):
            continue
        else:
            if(i == (PointStop-1)):
                print(i)
            else:
                print(i, end='')


print('')
print("Program ending.")