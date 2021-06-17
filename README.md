# VW-SDK : An Efficient Convolutional Weight Mapping Algorithm Using Shifted and Duplicated Kernel with Variable Windows.
---
## Abstract
...
<!-- In processing-in-memory (PIM) architectures forconvolutional neural network (CNN) inference, the mappingscheme of the CNN weights to the PIM array decides the numberof computing cycles, which determines the computational latencyand energy. A recent study proposed shifted and duplicatedkernel (SDK) mapping that reuses the input feature mapswith a unit of a parallel window, which is convolved withduplicated kernels to obtain multiple output elements in parallel.However, the existing SDK-based mapping algorithm does notalways provide optimal mapping because it maps a square-shaped parallel window having the entire channels at one cycle.In this paper, we introduce a novel mapping algorithm calledvariable-window SDK (VW-SDK), which adaptively determinesthe shape of the parallel window that leads to the minimumcomputing cycles for a given convolutional layer and PIM array.By allowing rectangular-shaped windows with partial channels,VW-SDK better utilizes PIM array, thereby reducing the numberof inference cycles. The simulation with a 512×512 PIM arrayand Resnet-18 shows that VW-SDK improves the computingspeed by 2.78×compared to the existing SDK algorithm. -->

## Requirements
+ python

## Usage
You have to input the parameters like image size, kernel size, the number of channels, and so on ...

### example1
With list, you can input the parameters.

    """
    Resnet18
    """
    Res_image = [112, 56, 28, 28, 14, 14, 7, 7]
    Res_kernel = [7, 3, 3, 3, 3, 3, 3, 3]
    Res_channel = [3, 64, 64, 128, 128, 256, 256, 512, 512]
<!--     n_layers = [1, 4, 2, 2, 2, 2, 2, 2] -->

    image = Res_image
    kernel = Res_kernel
    channel = Res_channel
    
end code block 

### main.ipynb
* This code calculates the computing cycle according to the mapping methods (im2col, SDK, VW-SDK).
* You have to input the information such as the network, array size, and so on...

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

---
## Convolutional Neural Network (CNN)
### VGGnet
You can read the original pdf [here](https://arxiv.org/abs/1409.1556)


### Resnet
You can read the original pdf [here](https://ieeexplore.ieee.org/document/8246704)


