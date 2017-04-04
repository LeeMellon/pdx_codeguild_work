# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# print(fib(10))

# a = {'key':'value'}
# print(a['key'])                 #prints the value.

a = ['key': [1,2,3]]
print(a['key'][1])                 #prints the value at index 1

inp = input("enter something")
a[inp]  = "we just added a key called {}".format(inp)
print(a)
