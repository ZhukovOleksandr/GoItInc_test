def encrypt(text, n):
    """ Encrypts the given text using the 'n' attribute as number of iterations
    of concatenation even and odd indexes in the string  """
    if n > 0 and text:
        even = []
        odd = []
        encrypted = [text]
        iter_count = 0

        while iter_count < n:
            elem = encrypted[-1]
            [even.append(elem[i]) for i in range(len(elem)) if i % 2 == 0]
            [odd.append(elem[i]) for i in range(len(elem)) if i % 2 != 0]
            encrypted.append(''.join(odd) + ''.join(even))
            even.clear()
            odd.clear()
            iter_count += 1
        return encrypted[-1]
    else:
        return text


def decrypt(encrypted, n):
    """ Decrypts previously encrypted text using the sum of  'n' attribute
    and the number required to complete the permutation cycle """
    if encrypted and n > 0:
        len_text = len(encrypted)
        if len_text % 2 == 0:
            enc_numb = len_text - n
        else:
            enc_numb = (len_text - n) - 1
        result = encrypt(encrypted, enc_numb)
        return result
    else:
        return encrypted


if __name__ == '__main__':
    my_str = 'Abcdefghij'
    result_text = encrypt(my_str,3)
    print(result_text)
    print(decrypt(result_text,3))
    print(decrypt(None, 3))
