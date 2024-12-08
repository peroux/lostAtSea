def grade(a,b,c,d):
    if all(isinstance(x, (int, float)) for x in [a, b, c, d]):
        if (a <= 100 and b <= 100 and c <= 100 and d <= 100) and (a >= 0 and b >= 0 and c >= 0 and d >= 0):
            if (a+b+c+d)/4 >= 90:
                return "A"
            elif (a+b+c+d)/4 >= 80:
                return "B"
            elif (a+b+c+d)/4 >= 70:
                return "C"
            elif (a+b+c+d)/4 >= 60:
                return "D"
            else:
                return "F"
        else:
            return "Invalid input"


print(grade(100,90,90,89))