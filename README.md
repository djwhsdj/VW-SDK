# VW-SDK (Variable-window SDK)
---

## This code calculates the computing cycle according to the mapping methods (im2col, SDK, VW-SDK).

### main.ipynb
You have to input the information such as the network, array size, and so on...


### utils.ipynb
Functions for calculating the computing cycle.

---
## Mapping methods

### Im2col (Image to column)
You can read the original pdf [here](https://dl.acm.org/doi/10.1145/2964284.2967243)

Each kernel with size KxKxIC (where K is kernel, IC is input channel) is unrolled into the column. A kernel-sized window in an input feature map (IFM) is convolved with the kernel.


### SDK (Shift and Duplicate kernel)
You can read the original pdf [here](https://ieeexplore.ieee.org/document/9104658)

+ [2] Y.  Zhang,  G.  He,  G.  Wang,  and  Y.  Li,  “Efficient  and  robust  rram-based convolutional weight mapping with shifted and duplicated kernel,”IEEE Transactions on Computer-Aided Design of Integrated Circuitsand Systems, 2020.

### VW-SDK

---

<!-- This is a normal paragraph: -->

<!--     this is a code -->
  
<!-- end code block -->
