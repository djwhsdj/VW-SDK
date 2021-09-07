# VW-SDK : An Efficient Convolutional Weight Mapping Algorithm Using Shifted and Duplicated Kernel with Variable Windows.
---
## Abstract
...
<!-- In processing-in-memory (PIM) architectures forconvolutional neural network (CNN) inference, the mappingscheme of the CNN weights to the PIM array decides the numberof computing cycles, which determines the computational latencyand energy. A recent study proposed shifted and duplicatedkernel (SDK) mapping that reuses the input feature mapswith a unit of a parallel window, which is convolved withduplicated kernels to obtain multiple output elements in parallel.However, the existing SDK-based mapping algorithm does notalways provide optimal mapping because it maps a square-shaped parallel window having the entire channels at one cycle.In this paper, we introduce a novel mapping algorithm calledvariable-window SDK (VW-SDK), which adaptively determinesthe shape of the parallel window that leads to the minimumcomputing cycles for a given convolutional layer and PIM array.By allowing rectangular-shaped windows with partial channels,VW-SDK better utilizes PIM array, thereby reducing the numberof inference cycles. The simulation with a 512×512 PIM arrayand Resnet-18 shows that VW-SDK improves the computingspeed by 2.78×compared to the existing SDK algorithm. -->

## Requirements
+ python3.x+

## Usage

### main.ipynb
* This code calculates the computing cycle according to the mapping methods (im2col, SDK, VW-SDK).

### Example
With list, you have to input the PIM array size.
ex) [rows, columns]
![array](https://user-images.githubusercontent.com/57951442/132305459-7fb77663-9bec-4cea-a95e-596e45900b87.PNG)

And the, choice the network.
In these form, you can input other networks. 
![network](https://user-images.githubusercontent.com/57951442/132305634-ff83904b-a448-4314-af4e-ba06618cca92.PNG)

## Results
These tables show the computing cycles according to the convolutional layer.
We set the array size to 512x512, bit precision to 1.

### * VGG13

| **Image size** | **Conv layer** | **Im2col** | **SDK** | **VW-SDK** | **Optimal parallel window** |
|:---:|:---:|---:|---:|---:|:---:|
| 224x224 | 3x3x3x64 | 49284 | 12321 | 6216 | 10x3x3x16 |
| 224x224 | 3x3x64x64 | 98568 | 24642 | 24642 | 4x4x64x64 |
| 112x112 | 3x3x64x128 | 24200 | 6050 | 6050 | 4x4x32x128 |
| 112x112 | 3x3x128x128 | 36300 | 36300 | 12100 | 4x4x32x128 |
| 56x56 | 3x3x128x256 | 8748 | 8748 | 5832 | 4x3x42x256 |
| 56x56 | 3x3x256x256 | 14580 | 14580 | 10206 | 4x3x42x256 |


### * Resnet-18

| **Image size** | **Conv layer** | **Im2col** | **SDK** | **VW-SDK** | **Optimal parallel window** |
|:---:|:---:|---:|---:|---:|:---:|
| 112x112 | 7x7x3x64 | 11236 | 2809 | 1272 | 10x8x3x32 |
| 56x56 | 3x3x64x64 | 5832 | 1458 | 1458 | 4x4x32x64 |
| 28x28 | 3x3x128x128 | 2028 | 2028 | 676 | 4x4x32x128 |
| 14x14 | 3x3x256x256 | 720 | 720 | 504 | 4x3x42x256 |
---
## Mapping methods

### Im2col (Image to column)
You can read the original pdf [here](https://dl.acm.org/doi/10.1145/2964284.2967243)

Each kernel with size KxKxIC (where K is kernel, IC is input channel) is unrolled into the column. A kernel-sized window in an input feature map (IFM) is convolved with the kernel.


### SDK (Shift and Duplicate Kernel)
You can read the original pdf [here](https://ieeexplore.ieee.org/document/9104658)

This mapping computes multiple windows instead of single window simultaneously in each cycle. To reuses the input data, this method forms the parallel window that is a set of windows. Thus, it obtains multiple output feature maps (OFMs) by utilizing the PIM array.

---
## Convolutional Neural Network (CNN)
### VGGnet
You can read the original pdf [here](https://arxiv.org/abs/1409.1556)


### Resnet
You can read the original pdf [here](https://ieeexplore.ieee.org/document/8246704)


