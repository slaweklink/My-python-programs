#decodes a morse code message

morse = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.', 'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-',
'W':'.--','X':'-..-','Y':'-.--','Z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....',
'7':'--...','8':'---..','9':'----.','0':'-----',' / ':' '}


inversemorse = dict(list(zip(morse.values(),morse.keys()))) #inverses the values and keys

decoded_message = ""
sentence = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. " \
           "/ .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--"

sentence1 = sentence.split(" ")

for i in sentence1:
    if i == "/":
        decoded_message += " "
        continue
    decoded_message += inversemorse[i]

print(decoded_message)

