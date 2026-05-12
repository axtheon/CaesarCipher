def caesar(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not isinstance(shift, int):
        return 'The shift should be an integer!'

    if shift < 1 or shift > 25:
        return 'Shift should be between 1 and 25!'

    # Use negative shift for decryption
    if not encrypt:
        shift = -shift

    # Create shifted alphabet
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Create translation table for lowercase and uppercase letters
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # Translate the text using the table
    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


def get_text_and_shift(mode):
    text = input(f'Enter text to {mode}: ')

    try:
        shift = int(input('Enter shift value: '))
    except ValueError:
        return 'Invalid shift value!'

    if mode == 'encrypt':
        return encrypt(text, shift)
    else:
        return decrypt(text, shift)


while True:
    try:
        choice = int(input(
            '\nEncrypt = 1\n'
            'Decrypt = 2\n'
            'Exit = 0\n'
            'Enter your choice: '
        ))

        if choice == 0:
            print('Thanks for using this program!')
            break

        elif choice == 1:
            print(get_text_and_shift('encrypt'))

        elif choice == 2:
            print(get_text_and_shift('decrypt'))

        else:
            print('Invalid choice!')

    except ValueError:
        print('Invalid input!')