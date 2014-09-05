import random
import math

def gen_stats(mods=[0,0,0,0,0,0]):
    """Generate random stat block w/mods
    
    Keyword arguments:

    mods -- optional racial modifiers
    """
    stats = [random.randint(3,18) for x in range(6)]
    stats = [sum(x) for x in zip(stats,mods)]
    return stats

def gen_hitpoints(hd, lvl, mod=0):
    hp = 0
    for x in range(0,lvl):
        hp += random.randint(1,hd) + mod
    return hp

def calc_baseattack(mod, lvl):
    """Returns base attack bonus for given level / mod)

    Keyword Arguments:

    mod -- float between 1.0 and 0.0 

    lvl -- character level

    >>> calc_baseattack(1.0, 15)
    15

    >>> calc_baseattack(0.75, 15)
    11
    """
    bab = math.floor(lvl * mod)
    return bab
    
def calc_save(mask, lvl):
    """Returns base save for a given level and quality

    Keyword Arguments:

    mask -- bitmask of save quality

    lvl --  level of character

    >>> calc_save(0b10, 10)
    7

    >>> calc_save(0b1, 10)
    3
    """
    good = 0b10
    bad = 0b1

    if bin(mask&good) == bin(good):
        save = math.floor((1/2 * lvl) + 2)
    elif bin(mask&bad) == bin(bad):
        save = math.floor((1/3 * lvl))
    else:
        raise ValueError
    return save

def sort_stats(stats, weights):
    """Sort stats based on provided weights

    Keyword Arguments:

    stats -- list of six ability scores

    weights -- list of indexes for sorting scores

    >>> sort_stats([10, 11, 12, 13, 14, 15], [0, 5, 4, 3, 2, 1])
    [15, 10, 11, 12, 13, 14]
    """
    stats = sorted(stats, reverse=True)
    weightedstats = [ None for x in range(6) ]
    mod = 0
    for stat in stats:
        indx = weights.index(mod)
        weightedstats[indx] = stat
        mod += 1

    return weightedstats
