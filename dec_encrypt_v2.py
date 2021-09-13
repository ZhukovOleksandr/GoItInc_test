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
