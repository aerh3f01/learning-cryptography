# Taken and modified from Joj Macho while learning enhanced principles
# https://joj-macho.github.io/workspace/cryptography/playfair-cipher
#
def create_playfair_square(keyword):
    # Create a Playfair Square based on the keyword
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    # Remove duplicates from keyword while preserving order
    seen = set()
    keyword_unique = ''
    for char in keyword.upper():
        if char not in seen and char.isalpha() and char != 'J':
            seen.add(char)
            keyword_unique += char
    
    # Add remaining alphabet letters
    key_matrix = keyword_unique
    for char in alphabet:
        if char not in seen:
            key_matrix += char
    
    playfair_square = [list(key_matrix[i:i + 5]) for i in range(0, 25, 5)]
    return playfair_square

def find_position(matrix, char):
    # Find the position of a character in the Playfair Square
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def playfair_cipher(text, keyword, mode='encrypt'):
    # Create the Playfair Square based on the keyword
    playfair_square = create_playfair_square(keyword)
    
    # Prepare the text by removing non-alphabetic characters, converting 'J' to 'I' and grouping into digraphs
    text = ''.join([c for c in text.upper() if c.isalpha()]).replace('J', 'I')
    text = [text[i:i + 2] for i in range(0, len(text), 2)]

    result = ''
    shift = 1 if mode == 'encrypt' else -1
    
    for digraph in text:
        a, b = digraph[0], digraph[1]
        a_row, a_col = find_position(playfair_square, a)
        b_row, b_col = find_position(playfair_square, b)

        if a_row == b_row:
            result += playfair_square[a_row][(a_col + shift) % 5] + playfair_square[b_row][(b_col + shift) % 5]
        elif a_col == b_col:
            result += playfair_square[(a_row + shift) % 5][a_col] + playfair_square[(b_row + shift) % 5][b_col]
        else:
            result += playfair_square[a_row][b_col] + playfair_square[b_row][a_col]

    return result


if __name__ == "__main__":
    enc_or_dec = input("Would you like to (e)ncode or (d)ecode a message? ").strip().lower()
    text = input("Enter the text: ").strip()
    keyword = input("Enter the keyword: ").strip()
    mode = 'encrypt' if enc_or_dec == 'e' else 'decrypt'
    output = playfair_cipher(text, keyword, mode)
    print(f"Output: {output}")

