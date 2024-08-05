def TransposeSparseMatrix(sp_r,n,cl,nz_el):
    print("Transpose of SParse matrix: ")
    trans_sp=[0]*(nz_el+1)
    ct=[0]*cl
    trans_sp[0]=[cl,n,nz_el]
    for i in range(1,nz_el+1):
        ct[sp_r[i][1]]=ct[sp_r[i][1]]+1
    index=[1]*(cl+1)
    for i in range(1,cl+1):
        index[i]=index[i-1]+ct[i-1]
    for i in range(1,nz_el+1):
        x=index[sp_r[i][1]]
        trans_sp[x]=[sp_r[i][1],sp_r[i][0],sp_r[i][2]]
        index[sp_r[i][1]]=index[sp_r[i][1]]+1
    for i in range(0,nz_el+1):
        print(trans_sp[i])


n=int(input("Enter the number of row:"))
cl=int(input("Enter the number of column:"))
sp=[]
nz_el=0
sp_r=[]
sp_r.append([n,cl,0])

for i in range(n):
    spl=[]
    print("enter the elements of",i+1,"the row")
    for j in range(cl):
        x=int(input(""))
        if(x!=0):
            sp_r.append([i,j,x])
            nz_el=nz_el+1
        spl.append(x)
    sp.append(spl)

sp_r[0][2]=nz_el
print("sparse matrix is:")
for i in range(0,nz_el+1):
    print([sp_r[i]])


TransposeSparseMatrix(sp_r,n,cl,nz_el)
