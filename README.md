# VW-SDK : An Efficient Convolutional Weight Mapping Algorithm Using Shifted and Duplicated Kernel with Variable Windows.
---

## This code calculates the computing cycle according to the mapping methods (im2col, SDK, VW-SDK).
## requirements
+ python

### main.ipynb
You have to input the information such as the network, array size, and so on...

## Results
These tables show the computing cycles according to the convolutional layer.
We set the array size to 512x512, bit precision to 1.

### * VGG13

| **Image size** | **Conv layer** | **Im2col** | **SDK** | **VW-SDK** | **Optimal parallel window** |
|:---:|:---:|---:|---:|---:|:---:|
| 224x224 | 3x3x3x64 | 49284 | 12321 | 5328 | 34x3x3x16 |
| 224x224 | 3x3x64x64 | 98568 | 24642 | 23976 | 10x3x17x64 |
| 112x112 | 3x3x64x128 | 24200 | 6050 | 6050 | 4x4x32x128 |
| 112x112 | 3x3x128x128 | 36300 | 36300 | 12100 | 4x4x32x128 |
| 56x56 | 3x3x128x256 | 8748 | 8748 | 5832 | 4x3x42x256 |
| 56x56 | 3x3x256x256 | 14580 | 14580 | 10206 | 4x3x42x256 |


### * Resnet-18

| **Image size** | **Conv layer** | **Im2col** | **SDK** | **VW-SDK** | **Optimal parallel window** |
|:---:|:---:|---:|---:|---:|:---:|
| 112x112 | 7x7x3x64 | 11236 | 2809 | 1272 | 22x7x3x32 |
| 56x56 | 3x3x64x64 | 5832 | 1458 | 1458 | 10x3x17x64 |
| 28x28 | 3x3x64x128 | 1352 | 338 | 338 | 4x4x32x128 |
| 28x28 | 3x3x128x128 | 2028 | 2028 | 676 | 4x4x32x128 |
| 14x14 | 3x3x128x256 | 432 | 432 | 288 | 4x3x42x256 |
| 14x14 | 3x3x256x256 | 720 | 720 | 504 | 4x3x42x256 |

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
