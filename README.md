# VW-SDK : An Efficient Convolutional Weight Mapping Algorithm Using Shifted and Duplicated Kernel with Variable Windows.
---

## This code calculates the computing cycle according to the mapping methods (im2col, SDK, VW-SDK).

### main.ipynb
You have to input the information such as the network, array size, and so on...

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
### utils.ipynb
Functions for calculating the computing cycle.

---
## Mapping methods

### Im2col (Image to column)
You can read the original pdf [here](https://dl.acm.org/doi/10.1145/2964284.2967243)

Each kernel with size KxKxIC (where K is kernel, IC is input channel) is unrolled into the column. A kernel-sized window in an input feature map (IFM) is convolved with the kernel.


### SDK (Shift and Duplicate kernel)
You can read the original pdf [here](https://ieeexplore.ieee.org/document/9104658)

This mapping computes multiple windows instead of single window simultaneously in each cycle. To reuses the input data, this method forms the parallel window that is a set of windows. Thus, it obtains multiple output feature maps (OFMs) by utilizing the PIM array.

<!-- ### VW-SDK
 -->
---

<!-- This is a normal paragraph: -->

<!--     this is a code -->
  
<!-- end code block -->
