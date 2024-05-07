ipz = [1, 0, 0, 7, 8, 0, 0, 0, 9, 1] # Input array.

output = [] # another empty array.
for number in ipz: # gets numbers through the array.
    if number > 0: # if number is greater than 0.
        output.append(number) # appends the positive numbers to the output array.

size = len(ipz) # defining size for ipz.
sizeop = len(output) # defining size for output.

for i in range(size - sizeop): # appending 0 to the end of the output array.
    output.append(0)

for number in output: # getting numbers from the output array and printing.
    print(number)
