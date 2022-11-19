
def fibo_eterative(num):
    stepCount = 2
    if num <= 1:
        return num
    else:
        a ,b =0, 1
        for i in range(1,num):
            stepCount+=1
            c = a+b
            a = b
            b = c
        print("Step count = ",stepCount)
        return b



def fibo_recursive(num):
    
    if(num<=1):
        return num
    else :
        return fibo_recursive(num-1) + fibo_recursive(num-2)

n = 15      
print(n,"th fibonaci number using eterative method is",fibo_eterative(n))
print(n,"th fibonaci number using recursive method is",fibo_recursive(n))
