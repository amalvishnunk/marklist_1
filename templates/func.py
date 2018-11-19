def calc_per(mark,total):
    K=int((mark/total)*100)
    return (K)

def grade(percent):
    if(percent>=95):
        return "s"
    elif(percent<95 and percent>=90):
        return "a+"
    elif(percent<90 and percent>=85):
        return "a"
    elif(percent<85 and percent>=80):
        return "b+"
    elif(percent<80 and percent>=75):
        return "b"
    elif(percent<75 and percent>=70):
        return "c+"
    elif(percent<70 and percent>=65):
        return "c"
    elif(percent<65 and percent>=60):
        return "d+"
    elif(percent<60 and percent>=55):
        return "d"
    else:
        return "f"

def check(grade1,grade2,grade3):
    if(grade1=='f'or grade2=='f'or grade3=='f'):
        return "Faied"
    else:
        return "passed"   