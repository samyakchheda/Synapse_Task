n=[
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 1],
]
def count_ones(i,j):
    c=0
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if n[x][y]==1:
                c+=1
    return c
n.reverse()
m=0
result=0
blast_coordinates=None
for i in range(1,len(n)-1):
    for j in range(1,len(n[i])-1):
        if n[i][j]==0:
            continue
        else:
            m=count_ones(i,j)
            if m>result:
                result=m
                blast_coordinates=[j,i]
                

if blast_coordinates:
    print(f"Blast at {blast_coordinates} with damaging {result} island")

else:
    print("No blast coordinates found.")
