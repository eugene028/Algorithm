


msg1=input("소중한 것?")
msg2=input("소중한 것?")
msg3=input("소중한 것?")
msg4=input("소중한 것?")
msg5=input("소중한 것?")
msg6=input("소중한 것?")
msg7=input("소중한 것?")

print("@내게 소중한 것 7가지?")
print(msg1,end=' ')
print(msg2,end=' ')
print(msg3,end=' ')
print(msg4,end=' ')
print(msg5,end=' ')
print(msg6,end=' ')
print(msg7,end=' ')

msg1,msg2,msg3,msg4,msg5,msg6,msg7=input("7가지 소중한 것?").split()
print("@내게 소중한 것 7가지")
print("{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(msg1,msg2,msg3,msg4,msg5,msg6,msg7))


msg="오래참고 온유하며 자랑하지아니하며 교만하지아니하며 무례히행하지아니하며 자기의유익을구하지아니하며"
msg1,msg2,msg3,msg4,msg5,msg6=msg.split(' ')
print("사랑은 %s" %msg1)
print("사랑은 %s" %msg2)
print("사랑은 %s" %msg3)
print("사랑은 {}".format(msg4))
print("사랑은 {}".format(msg5))
print("사랑은 {}".format(msg6))