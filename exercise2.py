### To make the below print a ping script 
## for everything in range 10.1.1.1 - 10.1.3.254,
## we need to change TWO lines below. 
####### Flag

for octet3 in range(1,4):
  for octet4 in range(1,4):
    print('ping 10.1.'+str(octet3)+'.'+octet4)