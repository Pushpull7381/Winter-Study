# # # n=1
# # # s=0
# # # while s<100 :
# # #     s+=n
# # #     n+=1
# # # print(s)

# # n=2
# # count=0
# # while True :
# #    n*=2
# #    count+=1
# #    if 8 < count :
# #        print('2를 10번 곱한 값:',n)
# #        break 

# for i in range(1,11):
#     if(i%2==0): continue
#     print(i,end=' ')

for i in range(1,10):
    for j in range(1,10):
        n=i
        n*=j
        print(n, end=' ')
    print('\n', end='')