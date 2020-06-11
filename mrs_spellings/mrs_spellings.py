from .qwerty_caches.closest_dists_cache import qwerty_closest_dists


class MrsWord(str):
    """Create a new word on which to apply misspelling transforms

    Args:
        word (str): a string you wish to generate misspellings of

    Returns:
        MrsWord (str)
    """

    def __new__(cls, word):

        if isinstance(word, MrsWord):
            return word
        obj = str.__new__(cls, word)
        return obj

    def delete(self, number_deletes=1):
        """
        delete some number `number_deletes` from this word

        Args:
            number_deletes (int): number of deletions to perform

        Returns:
            MrsSpellings (set): all possible misspellings that form as a result of `number_deletes` deletions
        """
        ret = set()
        for i in range(len(self) - (number_deletes - 1)):
            temp = list(self)
            del temp[i : i + number_deletes]
            ret.add(MrsWord("".join(temp)))

        return MrsSpellings(ret)

    def swap(self):
        """
        swap some consecutive characters

        Args:

        Returns:
            MrsSpellings (set): all possible misspellings that form as a result of swapping consecutive characters
        """
        ret = set()
        for i in range(len(self) - 1):
            temp = list(self)
            t = temp[i]
            temp[i] = temp[i + 1]
            temp[i + 1] = t
            ret.add(MrsWord("".join(temp)))
        return MrsSpellings(ret)

    def qwerty_swap(self, max_distance=1):
        """
        swap characters with their qwerty neighbors

        Args:
            max_distance (int): the max distance (taxi-cab) of keys on the keyboard to swap
                                e.g. `max_distance=1` then "g" could become one of ["f", "h"]
                                    `max_distance=2` then "g" could become one of ['f', 'h', 't', 'y', 'v', 'b']
                                    Note: The number of swaps possible increases with distance however the increase is not always uniform.
                                    For example, the 3rd set of keys from g is ['6', 'd', 'j'] while the second was ['t', 'y', 'v', 'b']
        Returns:
            MrsSpellings (set): all possible misspellings that form as a result of swapping characters with qwerty neighbors
        """
        ret = set()
        for li, l in enumerate(self):
            is_upper = l.isupper()
            l = l.lower()
            for crop in qwerty_closest_dists[l][:max_distance]:
                for si, sl in enumerate(crop):
                    temp = list(self)
                    temp[li] = sl if not is_upper else sl.upper()
                    ret.add(MrsWord("".join(temp)))
        return MrsSpellings(ret)


class MrsSpellings(set):
    """Create a new set of words on which to apply misspelling transforms

    Args:
        spellings (iterable): an iterable of string instances (Note: MrsWord is a valid string instance)

    Returns:
        MrsWord (str)
    """

    def __new__(cls, spellings):

        obj = set.__new__(cls, [MrsWord(w) for w in spellings])
        return obj

    def to_list(self):
        """
        get a list of MrsWords in this MrsSpellings

        Args:

        Returns:
            list of MrsWords
        """
        return list(self)

    def delete(self, number_deletes=1):
        """
        delete some number `number_deletes` from this word

        Args:
            number_deletes (int): number of deletions to perform

        Returns:
            MrsSpellings (set): all possible misspellings that form as a result of `number_deletes` deletions
        """
        ret = None
        for word in self:
            temp = word.delete(number_deletes)
            if ret is None:
                ret = temp
            else:
                ret = ret.union(temp)
        return ret

    def swap(self):
        """
        swap some consecutive characters

        Args:

        Returns:
            MrsSpellings (set): all possible misspellings that form as a result of swapping consecutive characters
        """
        ret = None
        for word in self:
            temp = word.swap()
            if ret is None:
                ret = temp
            else:
                ret = ret.union(temp)
        return ret

    def qwerty_swap(self, max_distance=1):
        """
        swap characters with their qwerty neighbors

        Args:
            max_distance (int): the max distance (taxi-cab) of keys on the keyboard to swap
                                e.g. `max_distance=1` then "g" could become one of ["f", "h"]
                                    `max_distance=2` then "g" could become one of ['f', 'h', 't', 'y', 'v', 'b']
                                    Note: The number of swaps possible increases with distance however the increase is not always uniform.
                                    For example, the 3rd set of keys from g is ['6', 'd', 'j'] while the second was ['t', 'y', 'v', 'b']
        Returns:
            MrsSpellings (set): all possible misspellings that form as a result of swapping characters with qwerty neighbors
        """
        ret = None
        for word in self:
            temp = word.qwerty_swap(max_distance)
            if ret is None:
                ret = temp
            else:
                ret = ret.union(temp)
        return ret
