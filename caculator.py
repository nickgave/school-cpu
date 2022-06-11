minus = lambda x, y: x-y
divide = lambda x, y: x/y
mod = lambda x, y: x%y
exp = lambda x, y: x**y
def plus(args):
    num=0
    for i in args: num+=i
    return num
def times(args):
    num=1
    for i in args:num*=i
    return num
def isint(x):
    return int(x)==x
def root(x, y):
    if x < 0 : return str((-x)**(1/y))+"i"
    else : return (x)**(1/y)
def factorial(x):
    num = 1
    if not isint(x) or x<0 : return "자연수만 입력해주십시오."
    for i in range(x,0,-1): num *= i
    return num
def permutation(x, y):
    return factorial(x)/factorial(x-y)
def combination(x, y):
    return permutation(x,y) * (1/factorial(y))
def prettyprint(des):
    print(f"{'='*80}\n{des}\n{'='*80}")

Sel = ["+", "-", "*", "/", "!", "^", "permutation", "combination", "root", "mod"]
while True:
    Input = input("연산자를 선택하십시오.\n{}\n{}\n{}\n".format("="*80,", ".join(Sel),"="*80))
    if Input in ["+", "*"]:
        nums = input("="*80+"\n이 연산자는 무수히 많은 수를 취합니다. 띄어쓰기로 구분하여 입력하여주십시오.\n"+"="*80+"\n").split(" ")
        for i in range(0, len(nums)): nums[i]=float(nums[i])
        if Input == "+": prettyprint(plus(nums))
        else: prettyprint(times(nums))
    if Input in ["-", "/", "^", "mod", "root"]:
        try : 
            num1, num2 = tuple(input("="*80+"\n이 연산자는 두 개의 수를 취합니다. 띄어쓰기로 구분하여 입력하여주십시오.\n"+"="*80+"\n").split(" "))
            if Input == "-": prettyprint(minus(float(num1), float(num2)))
            elif Input == "/": 
                if num2 == 0: print("0으로 나눌 수 없습니다.")
                else: prettyprint(divide(float(num1), float(num2)))
            elif Input == "^": prettyprint(exp(float(num1), float(num2)))
            elif Input == "mod": prettyprint(mod(float(num1), float(num2)))
            elif Input == "root": prettyprint(root(float(num1), float(num2)))
        except : prettyprint("두 개만, 그리고 숫자만 입력해 주십시오.")
    if Input in ["permutation", "combination"]:
        try:
            num1, num2 = tuple(input("="*80+"\n이 연산자는 두 개의 자연수를 취합니다. 띄어쓰기로 구분하여 입력하여주십시오.\n"+"="*80+"\n").split(" "))
            if int(num1)<int(num2): prettyprint("첫 번째는 수는 두 번째 수보다 커야합니다.")
            elif Input == "permutation": prettyprint(permutation(int(num1), int(num2)))
            elif Input == "combination": prettyprint(combination(int(num1), int(num2)))
        except: prettyprint("두 개만, 그리고 자연수만 입력해 주십시오.")
    if Input == "!":
        try: 
            num1 = int(input("="*80+"\n이 연산자는 한 개의 자연수를 취합니다. 입력해주십시오.\n"+"="*80+"\n"))
            prettyprint(factorial(num1))
        except: prettyprint("한 개만, 그리고 자연수만 입력해 주십시오.")

        
        