import re 
from pprint import pprint

fp = "/Users/maksim/dev_projects/makslevental.github.io/_posts/2021-06-09-conjugate_gradients.md"
p = re.compile(r"([^\$])\$([^\$]+)\$")

with open(fp, "r+") as f:
    data = f.read()
    r_data = p.sub(r'\1$$\2$$', data)
    f.seek(0)
    f.write(r_data)
    f.truncate()
