#Encoding / Decoding

# st = input("Enter your message: ")
st = ("Mahfujar is good")
words = st.split(" ")
coding = True
if(coding):
    nwords = []
    for word in words:        
        if (len(words)>=3):
            r1 = "asd"
            r2 = "jkl"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        # else:
        #   nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords = []
    for word in words:        
        if (len(words)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        # else:
        #   nwords.append(word[::-1])
    print(" ".join(nwords))