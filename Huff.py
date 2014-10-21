from heapq import heappush, heappop, heapify
from collections import defaultdict
 
def HuffEncode(freq_dict):
    """Return a dictionary which maps keys from the input dictionary freq_dict
       to bitstrings using a Huffman code based on the frequencies of each key"""

    # Your Beautiful Code Here #
    heap = [[wt, [sym, ""]] for sym, wt in freq_dict.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    huff = heappop(heap)[1:]
    toReturn = {}
    for elem in huff:
        toReturn[elem[0]] = elem[1]
    return toReturn
    
    
english_freq_dict = {'!': 0.0008, "'": 0.0004, ' ': 0.1033, ',': 0.0011,\
             '.': 0.0011, '?': 0.0006, 'a': 0.069, 'c': 0.027000000000000003,\
             'b': 0.013999999999999999, 'e': 0.1, 'd': 0.039, 'g': 0.021, 'f': 0.022000000000000002,\
             'i': 0.06, 'h': 0.048, 'k': 0.008, 'j': 0.0014000000000000002, 'm': 0.025,\
             'l': 0.043, 'o': 0.065, 'n': 0.06, 'q': 0.0017000000000000001, 'p': 0.02,\
             's': 0.055999999999999994, 'r': 0.052000000000000005, 'u': 0.027000000000000003,\
             't': 0.083, 'w': 0.017, 'v': 0.0108, 'y': 0.018000000000000002, 'x': 0.0036, 'z': 0.0012}
             
             
letters2bits = {'!': '11101', "'": '11111', ' ': '11010', ',': '11100', \
            '.': '11011', '?': '11110', 'a': '00000', 'c': '00010', 'b': '00001', 'e': '00100', \
            'd': '00011', 'g': '00110', 'f': '00101', 'i': '01000', 'h': '00111', 'k': '01010',\
            'j': '01001', 'm': '01100', 'l': '01011', 'o': '01110', 'n': '01101', 'q': '10000', \
            'p': '01111', 's': '10010', 'r': '10001', 'u': '10100', 't': '10011', 'w': '10110', 'v': '10101',\
            'y': '11000', 'x': '10111', 'z': '11001'}

def reverse_dict(original_dict):
    # create a new dict with the keys of original_dict as values and the values of original_dict as keys
    new_dict = {}
    for key in original_dict:
        new_dict[original_dict[key]] = key
    return new_dict

bits2letters = reverse_dict(letters2bits)


letters2huff = HuffEncode(english_freq_dict)
huff2letters = reverse_dict(letters2huff)


def encode_string(string, letters2huff):
    """Return a bitstring encoded according to the Huffman code defined in the dictionary letters2huff.
       If your resulting bitstring does not have a length which is a multiple of five, add the binary for
       SPACE characters until it is."""
    
    # Your Beautiful Code Here
    encoded_string = ""
    for letter in string:
        encoded_string += letters2huff[letter]
    while len(encoded_string) % 5 != 0:
        encoded_string += letters2huff[" "]
    toReturn = ""
    for i in range(0, len(encoded_string), 5):
        toReturn += bits2letters[encoded_string[i:i+5]]
    return toReturn



def decode_string(coded_string, huff2letters):
    """Translate from a Huffman coded string to a regular string"""
    
    # Your Code Here #
    counter = 0
    decoded_string = ""
    for i in range(len(coded_string)):
        decoded_string += letters2bits[coded_string[i]]
    toReturn = ""
    while counter < len(decoded_string):
        end_counter = 1
        while decoded_string[counter:counter + end_counter] not in huff2letters:
            end_counter += 1;
        toReturn += huff2letters[decoded_string[counter:counter + end_counter]]
        counter += end_counter   
    return toReturn
