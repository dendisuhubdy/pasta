#!/usr/bin/python3

# This checks the cases k = 1 and k = 2 needed to complete the proof of the
# injectivity lemma in Appendix C of <https://eprint.iacr.org/2019/1021>.

from itertools import product
from collections import namedtuple

cd_pair = namedtuple('cd_pair', ['c', 'd'])

def c_d():
    yield cd_pair(-1,  0)
    yield cd_pair( 1,  0)
    yield cd_pair( 0, -1)
    yield cd_pair( 0,  1)

def sums_mod4(cd):
    return ((2**(k+1) + sum([cd[j].c * (2**j) for j in range(k)])) % 4,
            (2**(k+1) + sum([cd[j].d * (2**j) for j in range(k)])) % 4)

for k in (1, 2):
    M_k = [list(s) for s in product(c_d(), repeat=k)]
    assert(len(M_k) == 4**k)

    for cd in M_k:
        print("%r -> %r" % (cd, sums_mod4(cd)))

    for (cd, cd_dash) in product(M_k, repeat=2):
        if cd[0] != cd_dash[0]:
            assert(sums_mod4(cd) != sums_mod4(cd_dash))

print("QED")
