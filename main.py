import matplotlib
from numpy import block
import counter

#load and remove spaces from cypher text
ctext = "ZUNEH TDTHR IFTAD JBFCA TWHHZ TSKXK ZRPED BCTIX TBVGJ KDGVS JJIWF NJUPS UDSCN TETXV CYVCH VEFJH JUDSK DYYTS VMYXT SVGFK XTEHT WRWVP YLGJJ LMRIX KPYVB JEIBF JQURT EIFZC YYTRF HYZCK FGRRI NFCNE IMVUJ NTXKL TISXZ QJCXJ MTNKX XKWJR ITDXH YNUFI MVHNJ DWKWJ RITDX HWPHK DWNWF KTAVG DFJBZ HMKDH RAQZI YYPYR AQKWN EVXRG JDPIV DKRIT DHQZI YCTUR GYZRQ VHYYP YDDAV PWFJS UXSGT WGTYL PQDDY ZDSRI YIPHK XSXTF TWTKW JILMV CYYTD RGJRA NKIQV SNJIF ERJRE FIIGL IWVEJ CANEV ZGDSS TNEVX HJJVO JUITX TYYTW ZCYYP YFCJJ TSKTS TTDFJ BZAQJ TJKWJ ITNJP SVCTI BTLHF DDZEI TWXSW DWDPY ZDSRQ TLIYY TBFGQ UXKAJ XKPQZ IYCTN DPLZC FKXTE PSUIM ZCPZC LRGJR EUCXJ U"
ctext = ctext.replace(" ", "")

def repeatfinder(length: int, ctext: str) -> dict:
    output = {}
    for i in range(len(ctext) - length):
        block = ctext[i:i+length]
        if block in output:
            output[block] += 1
        else:
            output[block] = 1
    #return output
    return valcull({k: v for k, v in sorted(output.items(), key=lambda item: item[1])})

def valcull(input: dict) -> dict:
    return {key:val for key, val in input.items() if val != 1}

def kasiskicounter(ctext: str, blocks: list) -> list:
    out = []
    for block in blocks:
        #print(block)
        locations = []
        i = 0
        while True:
            i = ctext.find(block, i, len(ctext)) + 1
            #print(i)
            if i != 0:
                locations.append(i)
            else:
                break
        out.append(locations)
    #return out
    diffs = []
    for values in out:
        for i in range(len(values) - 1):
            #print(values[i+1] - values[i])
            diffs.append(values[i+1] - values[i])
    return diffs

#find individual keys after determining block length
def affinesolve(blocksize: int, cyphertext: input):
    out = [None] * len(cyphertext)
    for i in range(blocksize):
        temp = counter.counter(cyphertext[i:len(cyphertext):blocksize])
        for c in range(len(temp)):
            #print(c)
            #print(i)
            out[i + blocksize * c] = temp[c]
    print(str(out))
    sout = ""
    for c in out:
        sout = sout + c
    return sout

repeatedvals = (repeatfinder(5, ctext))
print(str(repeatedvals))
valindices = kasiskicounter(ctext, list(repeatedvals.keys()))
print(str(valindices))
blocksize = int(input("Input Probable Block Size: "))
#for i in range(1,151):
#    counter.counter(ctext[0:-1:i])
print(affinesolve(blocksize, ctext))
    
