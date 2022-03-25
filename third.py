import csv
a= []
print("\n the given training data set \n")
with open('gg_3.csv','r') as csvfile:
    reader= csv.reader(csvfile)
    for row in reader:
        a.append(row)
        print(row)
num_attributes= len(a[0])-1
print("\n the initial value of hypothesis:")
S=['0']*num_attributes
G=['?']*num_attributes
print("\n the most specific hypothesis S0:[0,0,0,0,0,0] \n")
print("\n the most general hypothesis G0:[?,?,?,?,?,?] \n")
for j in range(0,num_attributes):
    S[j]=a[0][j];
print("\n Candidate elimination algorithm hypothesis version space computation \n")
temp= []
for i in range(0,len(a)):
    if a[i][num_attributes]=='1':
            for j in range(0,num_attributes):
                if a[i][j]!=S[j]:
                    S[j]='?'
            for j in range(0,num_attributes):
                for k in range(0,len(temp)):
                    if temp[k][j]!='?' and temp[k][j]!=S[j]:
                        del temp[k]
            print("For training example no :{0} the hypothesis is S{0}".format(i+1),S)
            if (len(temp)==0):
                print("For training example no :{0} the hypothesis is G{0}".format(i+1),G)
            else:
                print("For training example no :{0} the hypothesis is G{0}".format(i+1),temp)
                
    if a[i][num_attributes]=='0':
         for j in range(0,num_attributes):
                if S[j]!=a[i][j] and S[j]!='?':
                    G[j]=S[j]
                    temp.append(G)
                    G = ['?'] * num_attributes
         print("For training example no :{0} the hypothesis is S{0}".format(i+1),S)
         print("For training example no :{0} the hypothesis is G{0}".format(i+1),temp)
                                            
