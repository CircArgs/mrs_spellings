# MrS SpELliNgS
a micro utility to generate plausible misspellings

<div align="center">
  <a href="https://badge.fury.io/py/mrs-spellings"><img src="https://badge.fury.io/py/mrs-spellings.svg" alt="PyPI version" height="18"></a>
<a href="https://codecov.io/gh/CircArgs/mrs_spellings">
  <img src="https://codecov.io/gh/CircArgs/mrs_spellings/branch/master/graph/badge.svg" />
</a>
 
<img alt="Build Status" src="https://github.com/CircArgs/mrs_spellings/workflows/test/badge.svg">
<img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
<img alt="Language Python" src="https://img.shields.io/badge/language-Python-blue">
</div>

---

# Install

### from pypi

`pip install mrs_spellings`

### from source

`python -m pip install git+https://github.com/CircArgs/mrs_spellings.git`

# What?

Use this library to generate potential misspellings of words. This is useful for natural language processing tasks that require a quick substition during cleaning.

# Usage

There are 3 primary methods currently supported:
```python
In [1]: from mrs_spellings import MrsWord, MrsSpellings                                                                                                                                                            
#methods return MrsSpellings
In [2]: MrsWord("hello").swap()                                                                                                                                                                      
Out[2]: {'ehllo', 'hello', 'helol', 'hlelo'}

In [3]: MrsWord("hello").delete(number_deletes=1)                                                                                                                                                    
Out[3]: {'ello', 'hell', 'helo', 'hllo'}

In [4]: MrsWord("hello").qwerty_swap(max_distance=1)                                                                                                                                                 
Out[4]: 
{'gello',
 'h3llo',
 'hdllo',
 'he,lo',
 'he:lo',
  ...
 'jello',
 'nello',
 'yello'}
# simply chain methods
In [5]: MrsWord("hello").swap().delete()                                                                                                                                                             
Out[5]: 
{'ehll',
 'ehlo',
 'ello',
  ...
 'hllo',
 'hlol',
 'lelo'}
 
# MrsWord is a string
In [6]: MrsWord("Hello") + " " + MrsWord("World")                                                                                                                                                        
Out[6]: 'Hello World'

In [7]: MrsWord("Hello {}").format("world")                                                                                                                                                      
Out[7]: 'Hello world'

# MrsSpellings work as sets
In [8]: MrsWord("hello").swap().union(MrsWord("world").delete())                                                                                                                        
Out[8]: {'ehllo', 'hello', 'helol', 'hlelo', 'orld', 'wold', 'word', 'worl', 'wrld'}

In [9]: MrsWord("hello").delete(1)-MrsWord("hello").delete(1)                                                                                                                                        
Out[9]: set()

In [10]: " ".join(MrsWord("Hello").qwerty_swap())                                                                                                                                                     
Out[10]: 'Helko Hdllo Yello He,lo Helll Hellp Hel,o Nello Heklo Hrllo H3llo Gello Heolo He:lo Helli Hell9 Heloo Hel:o Jello Hwllo'
```

