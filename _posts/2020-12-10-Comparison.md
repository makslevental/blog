---
layout: post
title: Comparing the costs of abstraction for DL frameworks
published: true
---

  High level abstractions for implementing, training, and testing Deep Learning (DL) models abound.
  Such frameworks function primarily by abstracting away the implementation details of arbitrary neural architectures, thereby enabling researchers and engineers to focus on design.
  In principle, such frameworks could be ``zero-cost abstractions'';
  in practice, they incur translation and indirection overheads.
  We study at which points exactly in the engineering life-cycle of a DL model the highest costs are paid and whether they can be mitigated.
  We train, test, and evaluate a representative DL model using PyTorch, LibTorch, TorchScript, and cuDNN on representative datasets, comparing accuracy, execution time and memory efficiency.

{% include abstraction_comparison.html %}
