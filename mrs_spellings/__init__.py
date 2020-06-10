__package__="mrs_spellings"

class Mrs_Speller:
    def __init__(self, n_swaps=1, max_deletes=1, minimal_space=False):
        self.n_swaps=n_swaps
        self.max_deletes=max_deletes
        self.minimal_space=minimal_space

    def delete(self, word, number_deletes=1):
        #TODO: preallocate ret
        ret=[]
        for i in range(len(word)-(number_deletes-1)):
            temp= list(word)
            del temp[i:i+number_deletes]
            ret.append("".join(temp))

        return ret

    def swap(self, word):
        #TODO: preallocate ret
        ret = []
        for i in range(len(word)-1):
            temp=list(word)
            t=temp[i]
            temp[i]=temp[i+1]
            temp[i+1]=t
            ret.append("".join(temp))
        return ret

    def __max_space_generate(self, word):
        ret=[]
        for i in range(self.max_deletes):
            ret+=self.delete(word, i)

        swapped = self.swap(word)
        ret+=swapped
        for w in swapped:
            ret+=self.delete(w)
        ret.append(word)

        return list(set(ret))

    def __min_space_generate(self, word):
        ret=set()
        for i in range(self.max_deletes):
            ret.union(set(self.delete(word, i)))

        swapped = self.swap(word)
        retret.union(set(swapped))
        for w in swapped:
            ret.union(set(self.delete(w)))
        ret.update(word)

        return list(ret)

    def generate(self, word):
        if self.minimal_space:
            return self.__min_space_generate(word)
        return self.__max_space_generate(word)