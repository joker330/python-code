# break 的建议范例
# n=0
# while n<5:
#     if n==3:
#         break
#     print(n) # 印出会圈中的 n
#     n+=1
# print("最后的 n: ",n) # 印出回圈结束后的 n

# continue 的简单范例
# n=0
# for x in [0,1,2,3]:
#     if x%2==0: # x 是偶数
#         continue
#     print(x)
#     n+=1
# print("最后的 n: ",n)    
# else 的简单范例
# sum=0
# for n in range(16):
#     sum+=n
# else:
#     print(sum) # 印出 0+1+2....+10 的结果
# 综合范例: 找出整数平方根
# 输入 9，得到 3
# 输入 11，得到【没有】整数的平方根
n=input("输入一个正整数:")
n=int(n)
for i in range(n)
    if i*i==n:
        print("整数次方根")   
        break
    else:
        print("没有整数次方根")
