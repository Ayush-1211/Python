#Example 1
num = 10
string = "20"
result_1 = int(string) + num
print("int(20) + 10 is= ", result_1, "\n")

#Example 2
str = '100'
print("int(100) with base 2= ", int(str,2))
print("int(100) with base 4= ", int(str,4))
print("int(100) with base 8= ", int(str,8))
print("int(100) with base 16= ", int(str,16), "\n")

#Example 3
binaryString = "111"
Decimal = int(binaryString, 2)
print("Binary to Decimal is= ", Decimal)   #(111)₂ = (1 × 2²) + (1 × 2¹) + (1 × 2⁰) = (7)₁₀

octalString = "101"
Decimal = int(octalString, 8)
print("Octal to Decimal is= ", Decimal, "\n")   #101 = (1 × 8²) + (0 × 8¹) + (1 × 8⁰) = 65

