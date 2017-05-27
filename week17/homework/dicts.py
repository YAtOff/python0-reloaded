# -*- coding: utf-8 -*-

def count_words(words):
    """
    Напишете функция `count_words(words)`, която:

        * Взима списък от низове `words`
        * Връща речник, който има следния вид:

        ```
        {
        "word": count_of_that_word
        }
        ```

    За всеки елемент от списъка, се пази броят на неговите срещания в `words`.

    >>> counts = count_words(["words", "are", "meaningful", "words", "words", "are"])
    >>> counts == {"words": 3, "are": 2, "meaningful": 1}
    True

    Правете разлика между думи с главна и с малка буква.
    """
    pass


def count_vowels_consonants(word):
    """
    Напишете функция `count_vowels_consonants(word)`, която:

        * Взима един низ `word`
        * Връща речник, в който има два ключа - `"vowels"` и `"consonants"`
        * Срещу всеки ключ, трябва да стои съответния брой на гласни и съгласни букви в думата.

    Бройте както главните, така и малките гласни и съгласни букви:

        * Гласните са `"aeiouyAEIOUY"`
        * Съгласните са `"bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"`

    >>> counts = count_vowels_consonants("aaaAcccD")
    >>> counts == {"vowels": 4, "consonants": 4}
    True
    """
    pass


def status_count(students):
    """
    Напишете функция `status_count(students)`, която:

        * Взима списък от ученици (речници) `students`.
          Всеки речник в списъка има два ключа - `"name"` и `"status"`,
          като статусът може да е `"finalized"` или `"not_finalized"`.
        * Връща речник, които има два ключа - `"finalized"` и `"not_finalized"`.
          Срещу всеки речник стои списък от имената на студентите,
          които имат дадения статус в `students`

    >>> students = [
    ...     {
    ...         "name": "RadoRado",
    ...         "status": "not_finalized"
    ...     },
    ...     {
    ...         "name": "Ivo",
    ...         "status": "finalized"
    ...     },
    ...     {
    ...         "name": "Genadi",
    ...         "status": "finalized"
    ...     }
    ... ]
    >>> grouped_stuednts = status_count(students)
    >>> grouped_stuednts == {
    ...    "finalized": ["Ivo", "Genadi"],
    ...    "not_finalized": ["RadoRado"]
    ... }
    True
    """
    pass
