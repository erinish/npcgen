"""RESTful API for NPC Generation
"""
import os
import sys
import re
CURDIR = os.path.dirname(os.path.abspath(__file__))
BASEDIR = os.path.split(CURDIR)[0]
sys.path.insert(0, BASEDIR)
from flask import Flask, request, render_template
from jinja2 import evalcontextfilter, Markup, escape
from utils.core import gen_hitpoints, calc_baseattack,\
calc_save, gen_stats
from db.sqlite import get_database

_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')
APP = Flask(__name__)

@APP.template_filter()
@evalcontextfilter
def nl2br(eval_ctx, value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') \
        for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result


@APP.route('/npcgen/<npcclass>/<level>')
def npcgen(npcclass, level):
    """Generate an npc given uri"""
    skills = []
    abilities = []
    c = get_database('%s/npcgen.db' % BASEDIR)
    print(npcclass)
    template = c.execute("SELECT * FROM classes WHERE name=?;", (npcclass,))
    for row in template:
        _, _, _, hitdie, skillranks, babmod, fortmod,\
        refmod, willmod = row
    classskills = c.execute("SELECT name FROM skills WHERE %s=1"\
    % npcclass.lower())
    for row in classskills:
        skills.append(row[0])
    classabilities = c.execute("SELECT name, type, desc FROM "\
    "abilities WHERE %s > 0 AND %s <=?"\
    % (npcclass.lower(), npcclass.lower()), (level,))
    for abil in classabilities:
        abilities.append(abil)

    level = int(level)
    stats = gen_stats()
    hp = gen_hitpoints(hitdie, level)
    bab = calc_baseattack(babmod, level)
    fort = calc_save(int(fortmod, 2), level)
    ref = calc_save(int(refmod, 2), level)
    will = calc_save(int(willmod, 2), level)
    skillpoints = (skillranks * level)

    return render_template('npcgen.html', classname=npcclass, hp=hp,\
                            stats=stats, bab=bab, fort=fort, ref=ref,\
                            will=will, skillpoints=skillpoints,\
                            skills=sorted(skills), abilities=abilities)
if __name__ == '__main__':
    APP.run(debug=True)
