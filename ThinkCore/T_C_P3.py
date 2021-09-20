# for taking User input
def takeInput(n):
    data = []
    for i in range(n):
        temp = []
        name = input("Enter Name : ")
        temp.append(name)

        w = float(input("Enter Weight in KG : "))
        temp.append(w)

        h = float(input("Enter Height in CM : "))
        temp.append(h)

        data.append(temp)
    return data

# calculate BMI and store in the list
def calBMI(data):
    for i in range(n):
        data[i].append(data[i][2] / (data[i][2] * data[i][2]))
    return data

# check by weight is sorted or not
def checkByWeight(data):
    sort1 = sorted(data, key=lambda x: x[1])
    flag = 0
    i = 1
    while i < len(sort1):
        if(sort1[i][1] < sort1[i-1][1]):
            flag = 1
        i += 1
    if flag == 0 :
        return True
    else :
        return False

# checking by BMI is sorted or not
def checkByBMI(data):
    sort1 = sorted(data, key=lambda x: x[3])
    flag = 0
    i = 1
    while i < len(sort1):
        if(sort1[i][3] < sort1[i - 1][3]):
            flag = 1
        i += 1
    if flag == 0 :
        return True
    else :
        return False

# finally is not sorted then sort the list by name
def sortFinal(data):
    if checkByWeight(data):
        return data
    elif checkByBMI(data):
        return data
    else:
        sort1 = sorted(data, key=lambda x: x[0])
        return sort1

# main function to manage all the function
def Main():
    n = int(input("Enter number of person : "))
    data = takeInput(n)
    data = calBMI(data)
    data = sortFinal(data)
    print("Name\t\t Weight\t\t Height\t\t BMI")
    for i in range(n):
        for j in range(4):
            print(data[i][j],end="\t ")

# finally call the main function
Main()   
            

