print(1,2,3,4,5,sep='')

st=[1,2,3]
st+=[4,5]
print(st)

st=[1,2,3]
st*=2
print(st)

st=[1,2,3,4,5]
n1=st[0]
n2=st[3]
print(n1, n2)

st=[1,3,3,4,5]
st[1]=2
print(st)

st=[1,2,3,4,5,6,7,8,9,10]
st2=st[3:6]
print(st2)

st=[1,2,3,4,5,6,7,8,9,10]
st[:3]=[0,0,0,0]
print(st)

st=[1,2,3,4,5,6,7,8,9,10]
st[5:]=[0,0,0,0,0,0]
print(st)

st=[1,2,3,4,5,6,7,8,9,10]
st[:]=[]
print(st)

st=[1,2,3,4,5,6,7,8,9,10]
st2=st[0:5:2]
print(st2)

st1="hello"
st2="world"

print(st1, st2)

st3=st1*2
print(st3)

print(st1[2])

st4=st1[1:3]
print(st4)

print(len("Hello"))
print(len([1,2,3]))

