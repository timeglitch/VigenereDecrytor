import numpy
import string
cyphertext = "ZYPMLYTXYHYBYNMDEYVTMPDMCTINCACTYECIVHYNYQTLOQINTLIVCEOCCOMVMPOVPMLEITOMVTXYKCKINEIVVYLMPCYVHOVGIQMEEKVOQITOMVSICZADLOBITYEYCCYVGYL"

alphasize = 26
cypherlength = len(cyphertext)

letterFrequency = {'E' : 12.0,
'T' : 9.10,
'A' : 8.12,
'O' : 7.68,
'I' : 7.31,
'N' : 6.95,
'S' : 6.28,
'R' : 6.02,
'H' : 5.92,
'D' : 4.32,
'L' : 3.98,
'U' : 2.88,
'C' : 2.71,
'M' : 2.61,
'F' : 2.30,
'Y' : 2.11,
'W' : 2.09,
'G' : 2.03,
'P' : 1.82,
'B' : 1.49,
'V' : 1.11,
'K' : 0.69,
'X' : 0.17,
'Q' : 0.11,
'J' : 0.10,
'Z' : 0.07 }

chartoint = dict.fromkeys(string.ascii_uppercase, 0)
tempcount = 0
for key in chartoint:
    chartoint[key] = tempcount
    tempcount += 1
inttochar = list(chartoint)


def frequency(inputtext):
    intext = inputtext.replace(" ", "")
    dictionary = dict.fromkeys(string.ascii_uppercase, 0)
    for char in intext:
        if(char not in dictionary.keys()):
            pass #dictionary[char] = 0
        dictionary[char] = dictionary[char] + 1
    #dictionary = ({k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])})
    for key in dictionary:
        dictionary[key] = dictionary[key]/len(intext) * 100
    return dictionary

def incidenceofcoincidence(dictionary):
    ic = 0
    for key in dictionary:
        na = dictionary[key]
        ic = ic + (na/cypherlength*(na-1)/(cypherlength-1)) 
    ic = ic * alphasize
    #print(ic)
    #print(chartoint)

def affine(a, b, text):
    converted = texttoint(text)
    for i in range(len(converted)):
        converted[i] = (converted[i]*a + b) % alphasize
    return inttotext(converted)

def texttoint(text):
    out = []
    for char in text:
        out.append(chartoint[char])
    return out

def inttotext(ints):
    out = ""
    for num in ints:
        out = out + inttochar[num]
    return out

#pass in two dicts, compares letter frequency against english, smaller out is greater similarity
def similarity(frequencies):
    out = 0
    for char in frequencies:
        #print(char, frequencies[char], letterFrequency[char])
        out = out + abs(frequencies[char] - letterFrequency[char])
    return out

#retuns a decrypted string and prints out a rough index of coincidence of the decryption with english
def counter(inputtext):
    shifts = {}
    for a in range(alphasize):
        for b in range(alphasize):
            temp = affine(a,b,inputtext)
            temp = frequency(temp)
            shifts[similarity(temp)] = [a,b]
    #shifts = dict(sorted(shifts.items()))
    print(min(shifts.keys()))
    minval = shifts[min(shifts.keys())]
    #print(affine(minval[0], minval[1], inputtext))
    return affine(minval[0], minval[1], inputtext)

#counter(cyphertext)