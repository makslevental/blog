---
layout: post
title: Kidane's algorithm
published: true
---

```python
from functools import reduce
from random import randomint

nums = [randomint(-100, 100) for _ in range(10)]
mmax = max(
    reduce(
        lambda acc, x: acc+[max(x, acc[-1]+x)], A[1:], [A[0]])
    ) 
```
