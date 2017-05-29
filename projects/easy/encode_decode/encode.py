def encode_word(word, cipher):
    """
    Измислили сме прост алгоритъм, с който може да замаскираме 1 дума:

    * За всяка буква в думата, заменяме я с друга буква, която не е в думата.
    * Пазим си речник, в който ключа е оригиналната буква, а стойността е новата буква.

    Например, ако имамe:

    * Думата `"python"`
    * Речникa:

    ```python
    {
        'p': 'm",
        'y': 'j',
        't': 'r',
        'h': 'i',
        'o': 'e',
        'n': 'w'
    }
    ```
    * То като резултат ще получим думата `"mjriew"`

    Напишетe функция, която кодира дума по даден речника.

    >>> encode_word("python", {'h': 'i', 'y': 'j', 'o': 'e', 't': 'r', 'n': 'w', 'p': 'm'})
    'mjriew'
    >>> decode_word("obg", {'m': 'p', 'o': 'r', 'g': 'f'})
    'rpf'
    >>> decode_word("programming", {'r': 'f', 'o': 'h', 'i': 'u', 'm': 'z', 'g': 's', 'a': 't', 'p': 'w', 'n': 'y'})
    'programming'
    wfhsftzzuys
    >>> decode_word("bbbbbbbbbbbbbbbbbbbbbbbbbbb", {'a': 'b'})
    'aaaaaaaaaaaaaaaaaaaaaaaaaaa'
    """
    pass
