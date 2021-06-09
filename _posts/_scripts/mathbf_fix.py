import re 
from pprint import pprint
import sys

# fp = "/Users/maksim/dev_projects/makslevental.github.io/_posts/2021-06-09-conjugate_gradients.md"
fp = sys.argv[1]
p = re.compile(r"([^\$])\$([^\$]+)\$")
pp = re.compile(r"& (.*) &")
with open(fp, "r+") as f:
    data = f.read()
    r_data = p.sub(r'\1$$\2$$', data)
    r_data = pp.sub(r'&\1', r_data)
    r_data = r_data.replace("aligned", "align")
    r_data = r_data.replace("**Proof", "\n**Proof")
    r_data = r_data.replace("**Lemma", "\n**Lemma")
    r_data = r_data.replace("**Theorem", "\n**Theorem")
    r_data = r_data.replace("$$\\blacksquare$$", "\n■\n")
    f.seek(0)
    f.write(r_data)
    f.truncate()
