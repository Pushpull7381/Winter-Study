# st=[1,2,3,4,5,6,7,8,9,10]
# st.append(10)
# print(st)

# st=[1,2,3,4,5,6,7,8,9,10]
# st.extend([11,12,13])
# print(st)

# st=[1,2,3,4,5,6,7,8,9,10]
# st.clear()
# print(st)

# st=[1,2,3,4,5,6,7,8,9,10]
# st.insert(3, 999)
# print(st)

# st=[1,2,3,4,5,6,7,8,9,10]
# st.pop(2)
# print(st)

# st=[1,2,2,3,4,5,6,7,8,9,10]
# st.remove(2)
# print(st)

# st=[1,2,1,4,1,1,7,8,9,10]
# st.count(1)
# print(st)

# st=[1,2,3,4,5,6,7,8,9,10]
# st.index(4)
# print(st)

st="PushPull"
print(len(st))

st="ABCDEGAR"
print(min(st))

st="ABCDEGAR"
print(max(st))

st="PushPull"
print(st.count("P"))

st="Push Pull"
st1=st.lower()
print(st1)

st="PushPull"
st1=st.upper()
print(st1)

st=" Push Pull "
st1=st.lstrip()
print(st1)

st=" Push Pull "
st1=st.rstrip()
print(st1)

st="PushPull"
st1=st.replace("Pull", "Pull :D")
print(st1)

st="Push_Pull"
li=st.split('_')
print(li)

st="There are many things^~^ to study during winter vacation.^~^"
print(st.find('^~^'))
print(st.rfind('^~^'))