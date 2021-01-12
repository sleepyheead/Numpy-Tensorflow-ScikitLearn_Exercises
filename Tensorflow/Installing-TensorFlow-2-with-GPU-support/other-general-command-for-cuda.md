### To locate all the file paths of CUDA

```
$ locate cuda | grep /cuda$
```

It gave me following on - 26-Jul-2020

```
/home/paul/.local/lib/python3.8/site-packages/tensorflow/include/external/local_config_cuda/cuda
/home/paul/.local/lib/python3.8/site-packages/tensorflow/include/external/local_config_cuda/cuda/cuda
/home/paul/.local/lib/python3.8/site-packages/tensorflow/include/tensorflow/stream_executor/cuda
/home/paul/Downloads/NVIDIA-Drivers/cuDnn-library/25-Jul-2020/10.1/2-only-linux/cudnn-10.1-linux-x64-v7.6.5.32/cuda
/home/paul/Downloads/Video-Editing/Blender/4-July-2020/blender-2.83.1-linux64/2.83/scripts/addons/cycles/source/kernel/kernels/cuda
/usr/include/thrust/system/cuda
/usr/lib/cuda
/usr/local/cuda
/usr/local/cuda-11.0/targets/x86_64-linux/include/cuda
/usr/local/cuda-11.0/targets/x86_64-linux/include/thrust/system/cuda
/usr/share/doc/cuda
/usr/share/doc/libthrust-dev/examples/cuda

```

### How to get number of GPU cards I have from a command-line

This command gets the number of GPUs directly, assuming you have nvidia-smi.

`nvidia-smi --query-gpu=name --format=csv,noheader | wc -l`

It prints the names of the GPUs, one per line, and then counts the number of lines.
