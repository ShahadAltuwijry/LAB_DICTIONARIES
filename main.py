dict1 = {
    1111111111: "amal",
    2222222222: "mohammed",
    3333333333: "khadija",
    4444444444: "abdullah"
}   
def findNum(num):
    
    if type(num) == str:
        print("This is invalid number: not numbers")
    else:    
        i = num
        j = str(i)
        length = len(j)
        vals = list(dict1.keys())
        if num in vals:
            if length > 10 or length < 10:
                print("This is invalid number: length")
            else:
                x = dict1[i]
                print(x)
        else:
            print("Sorry, the number is not found")
            

# findNum(2222222222)

#----------------------------------

def getList(arLst):
    
     
    for x in arLst:
        if x == 0:
            y= arLst.count(x)
            arLst.remove(x)
            zLst = [0]*y
            arLst.append(zLst)
        print(arLst)
    
getList([1, 3, 5, 0, 3, 0])