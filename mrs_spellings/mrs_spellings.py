from .qwerty_caches.closest_dists_cache import qwerty_closest_dists


class MrsWord(str):
    def __new__(cls, word):
        if isinstance(word, MrsWord):
            return word
        obj = str.__new__(cls, word)
        return obj

    def delete(self, number_deletes=1):
        ret = [None] * (len(self) - (number_deletes - 1))
        for i in range(len(self) - (number_deletes - 1)):
            temp = list(self)
            del temp[i : i + number_deletes]
            ret[i] = MrsWord("".join(temp))

        return MrsSpellings(set(ret))

    def swap(self):
        ret = [None] * (len(self) - 1)
        for i in range(len(self) - 1):
            temp = list(self)
            t = temp[i]
            temp[i] = temp[i + 1]
            temp[i + 1] = t
            ret[i] = MrsWord("".join(temp))
        return MrsSpellings(set(ret))

    def qwerty_swap(self, max_distance=1):
        ret = []
        for li, l in enumerate(self):
            for crop in qwerty_closest_dists[l][:max_distance]:
                temp_ret = [None] * len(crop)
                for si, sl in enumerate(crop):
                    temp = list(self)
                    temp[li] = sl
                    temp_ret[si] = MrsWord("".join(temp))
                ret += temp_ret
        return MrsSpellings(set(ret))


class MrsSpellings(set):
    def __new__(cls, spellings):
        obj = set.__new__(cls, spellings)
        return obj


    def to_list(self):
        return list(self)

    def delete(self, number_deletes=1):
        ret = None
        for word in self:
            temp = word.delete(number_deletes)
            if ret is None:
                ret = temp
            else:
                ret = ret.union(temp)
        return ret

    def swap(self):
        ret = None
        for word in self:
            temp = word.swap()
            if ret is None:
                ret = temp
            else:
                ret = ret.union(temp)
        return ret

    def qwerty_swap(self, max_distance=1):
        ret = None
        for word in self:
            temp = word.qwerty_swap(max_distance)
            if ret is None:
                ret = temp
            else:
                ret = ret.union(temp)
        return ret
