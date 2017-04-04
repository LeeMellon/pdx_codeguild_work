"""
    sure we'll be dong something soon....
    I'll let you know as soon as I know something
    write a fucntion that checks to see if a string
    is a palindrome.
    if yea, print to that effect.
    if nea, mock the user mercilessly
"""
#
# def greet():
#     nm = input('what is you name: ')
#     if nm == 'Chris':
#         print('Hello {} !'.format(nm))
#     if nm != 'Chris':
#         print('You\'re not Chris!')
#
#
# greet()

# def pala(word):                           #palindorme test
#     if word != test [::-1]:
#         print('boo')
#     elif word == test [::-1]:
#         print('yay')
#
# test  = input('word: ')
# pala(test)
#
# compil = []                                     #snake ot camel
# s_c = input('snake_case_phrase: ')
# c_c = s_c.split("_")
# for i in c_c:
#     compil.append(i.capitalize())
# done = ''.join(compil)
# print(done)


string = 'HelloHowAreYouToday'                  #camel to snake
string_list = []
last_index = 0
for i in range(len(string)):
    if string[i].isupper():
        if i != 0:
            string_list.append(string[last_index:i])
            last_index = i
print('_'.join(string_list).lower())
