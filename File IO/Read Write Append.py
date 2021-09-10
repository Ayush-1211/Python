# Read=r, Write=w, Read and Write=r+, Append=a

with open('text.txt', mode='r+') as my_file:
    text = my_file.write('Hey It\'s me!!')
    print(text)