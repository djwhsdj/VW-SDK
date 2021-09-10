import math
from function import *
import argparse

parser = argparse.ArgumentParser(description='Set the parameters to operate VW-SDK')
parser.add_argument('--ar', default = 512, type = int, help = 'N of rows of the PIM array')
parser.add_argument('--ac', default = 512, type = int, help = 'N of columns of the PIM array')
parser.add_argument('--network', default = 'VGG13', type = str, help = 'Dataset = [VGG13, Resnet18]')
args = parser.parse_args()

array = [args.ar, args.ac]

network = args.network

if network == 'VGG13' :
  image = [224, 224, 112, 112, 56, 56, 28, 28, 14, 14]
  kernel = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
  channel = [3, 64, 64, 128, 128, 256, 256, 512, 512, 512, 512]

elif network == 'Resnet18' :
  image = [112, 56, 28, 14, 7]
  kernel = [7, 3, 3, 3, 3]
  channel = [3, 64, 128, 256, 512]

network_information(network, image, array, kernel, channel)
result(network, image, array, kernel, channel)