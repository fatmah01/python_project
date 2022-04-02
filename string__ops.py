
#(1)
string=input('plz enter string ')
substring=input('plz enter substring ')
occurrence=int(input('plz enter no. '))
def find_nth_occurrence(string,substring,occurrence=1):
    try:
        n= 1
        r=string.find(substring)
        while occurrence>n and r > -1:
            n= n + 1
            r=string.find(substring, r + 1)
        return r
    except Exception as e:
        print("got it in the function :-) ", e)
print(find_nth_occurrence(string,substring,occurrence))
#(2)
a=input('plz enter word')
b=input('plz enter word')
def solve(a,b):
    try:
        if a == b: return True
        elif '*' not in a: return False
        elif a == '*': return True
        else:
            al = list(a)
            bl = list(b)
            al.remove('*')
            for i in al:
                c = True
                for j in bl:
                    if i == j and c == True:
                        bl.remove(i)
                        c = False
            n = str(''.join(bl))
            c = a.replace('*', n)
            if c == b:
                return True
            else:
                return False
    except Exception as e:
        print("got it in the function :-) ", e)
print(solve(a,b))
#(3)
s=input('plz enter word')
def is_palindrome1(s):
    try:
        s=s.lower()
        i = 0
        ln=len(s)// 2
        for  i in range  (ln):
            if ln<1:
                return True
            elif s[i] != s[(len(s) - 1) - i]:
                return False
            i += 1
        return True
    except Exception as e:
        print("got it in the function :-) ", e)
print(is_palindrome1(s))
#(3)
t=input('plz enter word')
def is_palindrome(t):
    try:
        t=t.lower()
        if t==t[::-1]:
            return True
        else:
            return False
    except Exception as e:
        print("got it in the function :-) ", e)
print(is_palindrome(t))
#bouns
w=input('plz enter word')
def f(w):
    try:
        l=list(w)
        mylist = list(dict.fromkeys(l))
        n=str(''.join(mylist))
        x=w.count(n)
        return (n,x)
    except Exception as e:
        print("got it in the function :-) ", e)
print(f(w))
