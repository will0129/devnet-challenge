### Exercise 1 : types and loop control
### Find the 2 fixes for the below to get it to print 
### router btp 65000 -> router bgp 65005 on different lines 
### router bgp 65000
### router bgp 65001
### router bgp 65002... etc. -> 65005
for AS in range(65000,65005):
    print("router bgp "+AS)   ############# This will give an error. it is expected, it is the flag.