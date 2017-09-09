import math

def labdis(lab1,lab2):
    Dlab = math.sqrt(pow((lab2[0]-lab1[0]),2)+pow((lab2[1]-lab1[1]),2)+pow((lab2[2]-lab1[2]),2))

    return Dlab

if __name__ == "__main__":
    print("二色をLabで色の差を求めます")
    L1 = input('L1:')
    a1 = input('a1:')
    b1 = input('b1:')
    L2 = input('L2:')
    a2 = input('a2:')
    b2 = input('b2:')
    
    lab1 = [int(L1),int(a1),int(b1)]
    lab2 = [int(L2),int(a2),int(b2)]

    dis = labdis(lab1,lab2)
    
    print(dis)
