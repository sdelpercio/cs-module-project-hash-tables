# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
most_frequent = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
tally = {}
decode_key = {}

def crack_caesar(text):
    with open(f'./applications/crack_caesar/{text}') as f:
        data = f.read()
        
    # build up tally dictionary
    for char in data:
        if char < 'A' or char > 'Z':
            continue
        if char in tally:
            tally[char] += 1
        else:
            tally[char] = 1
            
    # sort tally dictionary
    sorted_tally = sorted(tally.items(), key = lambda x: x[1], reverse=True)

    # assign encoded most frequent to general use most frequent
    counter = 0
    for key,value in sorted_tally:
        decode_key[key] = most_frequent[counter]
        counter += 1
        
    # decode 
    decoded_string = ''
    for char in data:
        if char < 'A' or char > 'Z':
            decoded_string += char
            continue
        
        decoded_string += decode_key[char]
        
    print(decoded_string)
    
crack_caesar('ciphertext.txt')