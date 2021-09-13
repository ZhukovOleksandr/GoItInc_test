def encrypt(text, n):
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

# def decrypt(encrypted, n):


if __name__ == '__main__':
    my_str = 'Abcdefghij'
    a = encrypt(my_str, 10)
    p = len(a)/2


    # enc_text = 'bdfhjAcegi'