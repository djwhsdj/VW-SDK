# VW-SDK : An Efficient Convolutional Weight Mapping Algorithm Using Shifted and Duplicated Kernel with Variable Windows.
---

## This code calculates the computing cycle according to the mapping methods (im2col, SDK, VW-SDK).
## requirements
+ python

### main.ipynb
You have to input the information such as the network, array size, and so on...

## Results
### Resnet-18
This table shows the computing cycle according to the convolutional layer.
We set the array size to 512x512,bit precision to 1.

| Image size | Conv layer | Im2col | SDK | VW-SDK |
|---|---|:---:|---:|----:|
| 112x112 | 7x7x3x64 | 11236 | 2809 | 1272 |
| 56x56 | 7x7x3x64 | 5832 | 1458 | 1458 |
| 28x28 | 7x7x3x64 | 1352 | 338 | 338 |
| 28x28 | 7x7x3x64 | 2028 | 2028 | 676 |
| 14x14 | 7x7x3x64 | 432 | 432 | 288 |
| 14x14 | 7x7x3x64 | 720 | 720 | 504 |
| 7x7 | 7x7x3x64 | 125 | 125 | 125 |
| 7x7 | 7x7x3x64 | 225 | 225 | 225 |

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
