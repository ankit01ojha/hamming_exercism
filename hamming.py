dna1 = raw_input("enter first dna strads \t")
dna2 = raw_input("enter second dna strads\t")
cnt = 0
if(len(dna1)!=len(dna2)):
        print("they can't be compared")
        
if(len(dna1)==len(dna2)):    
    for i in range(0,len(dna1)):
        if(dna1[i]!=dna2[i]):
            cnt +=1 
    print(cnt)
