.. role:: raw-html-m2r(raw)
   :format: html


MrS SpELliNgS
=============

a micro utility to procedurally generate plausible misspellings


.. raw:: html

   <div align="center">
     <a href="https://badge.fury.io/py/mrs-spellings"><img src="https://badge.fury.io/py/mrs-spellings.svg" alt="PyPI version" height="18"></a>
   <a href="https://codecov.io/gh/CircArgs/mrs_spellings">
     <img src="https://codecov.io/gh/CircArgs/mrs_spellings/branch/master/graph/badge.svg" />
   </a>

   <img alt="Build Status" src="https://github.com/CircArgs/mrs_spellings/workflows/test/badge.svg">
   <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
   <img alt="Language Python" src="https://img.shields.io/badge/language-Python-blue">
   </div>


----

`Table of Contents <#table-of-contents>`_
=============================================


* `MrS SpELliNgS <#mrs-spellings>`_
* `Install <#install>`_

  * `from pypi <#from-pypi>`_
  * `from source <#from-source>`_

* `Use Cases <#use-cases>`_
* `Usage <#usage>`_
* `Methods <#methods>`_

  * `deletion <#deletion>`_
  * `swapping <#swapping>`_
  * `qwerty distance (taxi-cab) based swapping <#qwerty-distance-taxi-cab-based-swapping>`_
  * `What is QWERTY distance? <#what-is-qwerty-distance>`_

----

Install
=======

from pypi
^^^^^^^^^

``pip install mrs-spellings``

from source
^^^^^^^^^^^

``python -m pip install git+https://github.com/CircArgs/mrs_spellings.git``

Use Cases
=========


* Generate misspellings to replace during the text cleaning process with low overhead
* Replace words with their potential misspellings as an augmentation during

  * training to make your model less susceptible to misspellings
  * during test time as part of TTA

* Supplement an existing solution for out-of-vocabulary words/ words that do not appear in an existing replacement dictionary

Usage
=====

There are 3 primary methods currently supported:


* `deletion <#deletion>`_
* `swapping <#swapping>`_
* `qwerty distance (taxi-cab) based swapping <#qwerty-distance-taxi-cab-based-swapping>`_
  ```python
  In [1]: from mrs_spellings import MrsWord, MrsSpellings\ :raw-html-m2r:`<br>`
  #methods return MrsSpellings
  In [2]: MrsWord("hello").swap()\ :raw-html-m2r:`<br>`
  Out[2]: {'ehllo', 'hello', 'helol', 'hlelo'}

In [3]: MrsWord("hello").delete(number_deletes=1)\ :raw-html-m2r:`<br>`
Out[3]: {'ello', 'hell', 'helo', 'hllo'}

In [4]: MrsWord("hello").qwerty_swap(max_distance=1)\ :raw-html-m2r:`<br>`
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

simply chain methods
====================

In [5]: MrsWord("hello").swap().delete()\ :raw-html-m2r:`<br>`
Out[5]: 
{'ehll',
 'ehlo',
 'ello',
  ...
 'hllo',
 'hlol',
 'lelo'}

MrsWord is a string
===================

In [6]: MrsWord("Hello") + " " + MrsWord("World")\ :raw-html-m2r:`<br>`
Out[6]: 'Hello World'

In [7]: MrsWord("Hello {}").format("world")\ :raw-html-m2r:`<br>`
Out[7]: 'Hello world'

MrsSpellings work as sets
=========================

In [8]: MrsWord("hello").swap().union(MrsWord("world").delete())\ :raw-html-m2r:`<br>`
Out[8]: {'ehllo', 'hello', 'helol', 'hlelo', 'orld', 'wold', 'word', 'worl', 'wrld'}

In [9]: MrsWord("hello").delete(1)-MrsWord("hello").delete(1)\ :raw-html-m2r:`<br>`
Out[9]: set()

In [10]: " ".join(MrsWord("Hello").qwerty_swap())\ :raw-html-m2r:`<br>`
Out[10]: 'Helko Hdllo Yello He,lo Helll Hellp Hel,o Nello Heklo Hrllo H3llo Gello Heolo He:lo Helli Hell9 Heloo Hel:o Jello Hwllo'

.. code-block::


   # Methods

   ## deletion
   ```python
   Signature: MrsWord.delete(number_deletes=1)
   Docstring:
   delete some number `number_deletes` from this word

   Args:
       number_deletes (int): number of deletions to perform

   Returns:
       MrsSpellings (set): all possible misspellings that form as a result of `number_deletes` deletions

swapping
--------

.. code-block:: python

   Signature: MrsWord.swap()
   Docstring:
   swap some consecutive characters

   Args:

   Returns:
       MrsSpellings (set): all possible misspellings that form as a result of swapping consecutive characters

qwerty distance (taxi-cab) based swapping
-----------------------------------------

.. code-block:: python

   Signature: MrsWord.qwerty_swap(max_distance=1)
   Docstring:

   swap characters with their qwerty neighbors

   Args:
       max_distance (int): the max distance (taxi-cab) of keys on the keyboard to swap
                           e.g. `max_distance=1` then "g" could become one of ["f", "h"]
                               `max_distance=2` then "g" could become one of ['f', 'h', 't', 'y', 'v', 'b']
                               Note: The number of swaps possible increases with distance however the increase is not always uniform.
                               For example, the 3rd set of keys from g is ['6', 'd', 'j'] while the second was ['t', 'y', 'v', 'b']
   Returns:
       MrsSpellings (set): all possible misspellings that form as a result of swapping characters with qwerty neighbors

what is qwerty distance?
^^^^^^^^^^^^^^^^^^^^^^^^

Qwerty distance is the distance between keys on the typical keyboard. For the purposes of this package, the following assumptions are made:


* each row has half a key offset
* the l1 distance is a good estimate of the natural travel distance between keys on the keyboard
* the shift key can add distance by virtue of requiring a hold-down

Here is an example of the results of these assumptions. The closest keys grouped by equal distance (groups in ascending order to furthest distance) to the ``g`` key are:

.. code-block:: python

   [['f', 'h'],
    ['t', 'y', 'v', 'b'],
    ['6', 'd', 'j'],
    ['r', 'u', 'c', 'n'],
    ['^', '5', '7', 's', 'k'],
    ['e', 'i', 'x', 'm'],
    ['%', '&', '4', '8', 'a', 'l'],
    ['w', 'o', 'z', '<'],
    ['$', '*', '3', '9', ':'],
    ['q', 'p', ','],
    ['#', '(', '2', '0', ';'],
    ['[', '>'],
    ['@', ')', '1', '-', '"'],
    [']', '.'],
    ['!', '_', '`', '=', "'"],
    ['\\', '?'],
    ['~', '+', '{'],
    ['/'],
    ['}'],
    ['|']]
