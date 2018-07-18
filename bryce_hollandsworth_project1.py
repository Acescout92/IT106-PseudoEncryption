#-------------------------------------------------------------------------------
# Student Name: Bryce Hollandsworth
# Assignment: Project #1
# Submission Date: April 1, 2018
# Python version: 3.6
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Textbook, Python Documentation
#-------------------------------------------------------------------------------
# Notes: Any general comments to the grader
#-------------------------------------------------------------------------------
# Pseudocode:
"""
    Main function takes standard input user_input(Code to be encoded)
    Main calls function encode_decode, sending user input as main argument
    Step 1-2:
        Using the user input, we first build two arrays and one empty string
        arrays: u_pref and encrypted_tuples
        string: holding
        We use a for loop to iterate over each character in user_input
        If the character does not exist in the u_pref array, we append the character to the array, 
        along with the index position of the string that is currently in "holding".
        The trick to the above is that we check the value of the holding string PLUS the next value in the user input before we append both to u_pref.
        This gives us (1, 'B'), in the instance of 'AB', for example
        Otherwise, we hold the letter in holding. We continue to hold subsequent letters until we obtain a unique prefix, at which point we take the index
        position of holding and add the index value, plus the next value in the string, to a tuple, which we then append to the array "encrypted_tuples"
        Reset holding at the end of the loop

    
    Step 3:
        Create a variable: index, set this to 0
        Create an empty array: encrypted_binary_list
        Start a for loop, using 2 variables
        We must first find value n, which will be the number of 0s to add to our index value once converted to binary
        Use formula: floor(index/2 + 1) for n
        Check to see if the second variable, val2, is equal to ''. This will indicate a duplicate string, and thus only requires 
        appending to encrypted_binary_list the value of the index position. This will help avoid errors down the line.
        When appending the binary-converted index values, we must use 2 tricks to ensure proper results: First, we must slice off the first two positions, as they will be 0b 
        (a quirk of the bin function).
        Next, we must also use the zfill function to add 0's according to the n-value. We use .zfill(n) to make sure this happens.
        We repeat the same steps for cases where val != '', only this time we also append the binary-converted ascii value of val2, zfill'ed to 8
        In both cases, we must first assign both the binary-converted index value and the binary-converted character value to a tuple, t, which we then append to 
        encrypted_binary_list
        Add 1 to index at the end of the for loop

        Lastly, we create a string, final_binary, which accepts the string converted values of both the index positions and character values, resulting in a literal
        binary string

    Step 4:
        Start by making a copy of your final_binary string, working_string
        We'll start by breaking up that copy into a list of individual numbers, decrypted_list
        Create an empty list, decryted_list, and an index counter, this_index
        Start a while loop for while there is still data inside our decrypted_list
        Using a reverse method to step 3, we first find the n-value (index length) using floor(index/2 + 1)
        Assign a variable, prefix_index, we find the binary value of our prefix via: [0:n]
        A null value will cause an error, so throw a condition for when our prefix_index = '' and break. This will help prevent serious errors.
        Convert the prefix index to an integer using the int() function
        Slice out the index value by reassigning the working list to start from the last value of the index
        Our prefix string will then logically be the next 8 bits, so make a slice for [0:8]
        Considering we have null values for strings in the case of duplicates, throw an if statement and convert our string to its ascii value, then remove that binary string
        from the working_string
        Assing both converted index value and character to a tuple, which will then be appended to the decrypted_list
        Iterate index by 1

    Step 5:
        Create a list, final_list ["], and empty string, holding.
        We take the decrypted_list and begin to iterate through it using a single variable, val.
        Val is a tuple, so calling val[0] will give us the index number and val[-1] will give us the character value
        Using this logic, we say that if val[0] == 0 we simply append to our final_list val[-1]
        Otherwise, we assign holdingto be the string converted values of val[0] concatonated with val[-1], with val[0] calling the appropriate index value of final list.
        For example: tuple (1, B) is val, and ["",A,B,AB,A] is currently in final_list. final_list[val[0]] will give index position 1 of final_list, giving us A, 
        turning (1,B) into 'A' + 'B'
        Lastly, we join final list, and output the decrypted string

        print the following:
        u_pref
        encrypted_tuples
        final_binary
        decryted_list
        final_list
"""
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------



import math


def main():
    user_input = input("Input initial string: ")
    encode_decode(user_input)


def encode_decode(user_input):
    # Steps 1 - 2:
    #Finding unique prefixes and indexes
    u_pref = ['']
    holding = ''
    encrypted_tuples = []
    for val in user_input:
        if (holding + val) in u_pref:
            holding += val
        else:
            t = (u_pref.index(holding), val)
            encrypted_tuples.append(t)
            u_pref.append(holding + val)
            holding = ''

    if len(''.join(u_pref)) < len(user_input): #Checks for a duplicate character or string at the tail of the user input
        last_chars = user_input[len(''.join(u_pref)):len(user_input)] #logically, any duplicates will happen at the tail. Use len to determine what's missing.
        t = (u_pref.index(last_chars), '')
        encrypted_tuples.append(t) #To be output; conclusion of step 2

    # Step 3:
    index = 0
    encrypted_binary_list = []
    for val, val2 in encrypted_tuples:
        n = int(math.floor(index/2+1)) #We get our n-vale, which is the length our index prefix should be once encoded. Basically how many zeros are added to the start.
        if val2 == '':
            t = (bin(val)[2:].zfill(n), '') 
            encrypted_binary_list.append(t)
        else:
#A lot of fancy programming magic tricker where I simultaneously slice off the 0b from bin() conversion and break characters down to their ASCII values before converting them to binary
            t = (bin(val)[2:].zfill(n), bin(ord(val2))[2:].zfill(8)) #Shove it all in a tuple.
            encrypted_binary_list.append(t) 
        index+=1
    final_binary = ''
    for val,val2 in encrypted_binary_list:
        final_binary += str(val) + str(val2) #Basic concatination, converting binary values to string values. 


    # Step 4:
    # Begin decoding
    working_list = final_binary
    decryption_list = list(working_list)
    decrypted_list = []
    this_index = 0
    while decryption_list:
        prefix_index_length = math.floor(this_index / 2 + 1)
        prefix_index = working_list[0: prefix_index_length]
        if prefix_index == '':
            break
        prefix_index = int(prefix_index, 2)
        working_list = working_list[prefix_index_length:] 
        prefix_string = working_list[0:8]

        if len(prefix_string) > 0:
            prefix_string = chr(int(prefix_string, 2))
            working_list = working_list[8:]
        t = (prefix_index, prefix_string)
        decrypted_list.append(t)
        this_index +=1
    #Fun facts, step 4 drove me insane :D


    #Step 5: LAST PUSH!!!
    final_list = ['']
    holding = ''
    for val in decrypted_list:
        if val[0] == 0: # I don't know why this was needed, it kept throwing index errors otherwise
            final_list.append(val[-1])
        else:
            holding = final_list[val[0]] + str(val[-1])
            final_list.append(holding)
    final_list = ''.join(final_list) #let's just reassign the whole list as a string I'm sure nothing will go wrong

    print("Step 1: ", u_pref)
    print("Step 2: ", encrypted_tuples)
    print("Encrypted Binary List: ", encrypted_binary_list)
    print("Step 3: ", final_binary)
    print("Step 4: ", decrypted_list)
    print("Step 5: ", final_list)


main()
