def decode_word(encrypted_word, cipher):
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

    Напишетe функция, която по кодираната дума и речника,
    по който сме я кодирали, да получим истинката дума.

    >>> decode_word("mjriew", {'h': 'i', 'y': 'j', 'o': 'e', 't': 'r', 'n': 'w', 'p': 'm'})
    'python'
    >>> decode_word("rpf", {'m': 'p', 'o': 'r', 'g': 'f'})
    'omg'
    >>> decode_word("wfhsftzzuys", {'r': 'f', 'o': 'h', 'i': 'u', 'm': 'z', 'g': 's', 'a': 't', 'p': 'w', 'n': 'y'})
    'programming'
    >>> decode_word("bbbbbbbbbbbbbbbbbbbbbbbbbbb", {'a': 'b'})
    'aaaaaaaaaaaaaaaaaaaaaaaaaaa'

    """
    pass
