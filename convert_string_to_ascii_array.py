#This script converts a string into an array of ascii characters, and outputs it as an 8-bit vector net with a depth equal to the string length.
#The output can then be copied into a verilog module.
#The original purpose for this script was to make ascii arrays than can be used when communicating over UART with the Basys 3 FPGA board



#instructions:
#- input name for the array when prompted
#-input the string you want to convert when prompted
#-copy the output between dashed lines
#-paste in verilog module



characters = ['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ','.' ,':','!','[',']','{','}','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
name = input("enter array name: ")
user_str = input("Enter the string you would like to convert to ASCII code: ");
length  = len(user_str)
output_str =[None]*length
for x in range(len(user_str)):
    for i in range(len(characters)):
     if user_str[x] == characters[i]:
        # print("\nMATCH",i)
         num = bin(ord(characters[i]))
         binary = (num.replace("0b", "8'b0"))
       #  print(binary)
         output_str[x] = binary
print("copy the following output between dashed lines into verilog module as array:")
print("----------------------------------------------------------------")
print("reg[7:0]" + name +"[0:",length-1,"];",end="")
print("\n")
print("initial begin")
for j in range(len(output_str)):
    print(name+"[",j,"]="+output_str[j]+";")
print("end")
print("----------------------------------------------------------------")
