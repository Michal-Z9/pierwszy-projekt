

while True:
    a = float(input("podaj pierwsza liczbe:"));
    b = float(input("podaj druga liczbe:"));
    d = input("podaj typ działania:");
    if d=="+":
        k=a+b;

    elif d=="-":
        k=a-b;

    elif d=="*":
        k=a*b;

    elif d=="/":
        if b!=0:
            k=a/b;
        else:
            print("nie mozna wykonac zadania")
    else:
        k=("nie znane dzialanie")
    print(a,d,b,"=",k);


