from db.sqlite import *
from utils.core import *

def main():
    create_database('npcgen.db')
    c = get_database('npcgen.db')
    barb = c.execute("SELECT * FROM classes WHERE name='Barbarian';")
    for row in barb:
        name, desc, align, hitdie, skillranks, babmod, fortmod, refmod, willmod = row

    LEVEL = 19
    STATS = gen_stats()
    HP = gen_hitpoints(hitdie, LEVEL)
    BAB = calc_baseattack(babmod, LEVEL)
    FORT = calc_save(int(fortmod, 2), LEVEL)
    REF = calc_save(int(refmod, 2), LEVEL)
    WILL = calc_save(int(willmod, 2), LEVEL)
    SKILLPOINTS = (skillranks * LEVEL)

    print("Level %s:" % LEVEL)
    print("Stats: %s:" % STATS)
    print("Hitpoints: %s" % HP)
    print("Base Attack: %s" % BAB)
    print("Fort Save: %s" % FORT)
    print("Reflex Save: %s" % REF)
    print("Will Save: %s" % WILL)
    print("Skillpoints: %s" % SKILLPOINTS)

if __name__ == '__main__':
    main()
