
oed = {}
def clean(text):                                                            #defines the function#
    for punct in ',?.!@#$%^&*()+-=':                                            #names punctuation to replace#
    text = text.replace(punct, '')                                      #replaces punct with blank#
    phrase_1 = (text.lower())                                                 #converts all input to lower case
    words = phrase_1.split()
    print(words)

text = input('Please input your massive throbbing list of pulsating word magic now!: ')

clean(text)
