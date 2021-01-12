### Related SO Question - NO ANS

https://stackoverflow.com/q/64606828/1902852

I have a machine with eight GPUs but Tensorflow doesn't seem to use them when training.

## Local Environment

Here's some information about the environment:

- `tensorflow-gpu` 2.3.1 is installed.

- `nvidia-smi` command reports: NVIDIA-SMI 440.82, Driver Version: 440.82, CUDA Version: 10.2

- `nvcc --version` command reports:

```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Wed_Oct_23_19:24:38_PDT_2019
Cuda compilation tools, release 10.2, V10.2.89
```

## Symptoms

When I run `model.fit()` with a large set of data, it doesn't seem to use GPUs at all. `nvidia-smi` shows 0% usage for all GPUs and the CPU usage ranges 400-700% (it's a 16-core machine).

I suspected there is something wrong with my model (perhaps some instructions cannot be compiled into CUDA C or something like that), so I tested it on a Google Colab GPU instance. It takes 10-15ms per step (13s for each epoch) whereas it would take over 100ms for each step on my machine. This leads me to believe that my model is being trained using GPUs on Google Colab.

## Interesting Factors

The following code

```python
import tensorflow as tf

tf.config.list_physical_devices()
```

produces this:

```
[PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU'),
 PhysicalDevice(name='/physical_device:XLA_CPU:0', device_type='XLA_CPU'),
 PhysicalDevice(name='/physical_device:XLA_GPU:0', device_type='XLA_GPU'),
 PhysicalDevice(name='/physical_device:XLA_GPU:1', device_type='XLA_GPU'),
 PhysicalDevice(name='/physical_device:XLA_GPU:2', device_type='XLA_GPU'),
 PhysicalDevice(name='/physical_device:XLA_GPU:3', device_type='XLA_GPU'),
 PhysicalDevice(name='/physical_device:XLA_GPU:4', device_type='XLA_GPU'),
 PhysicalDevice(name='/physical_device:XLA_GPU:5', device_type='XLA_GPU'),
 PhysicalDevice(name='/physical_device:XLA_GPU:6', device_type='XLA_GPU'),
 PhysicalDevice(name='/physical_device:XLA_GPU:7', device_type='XLA_GPU')]
```

### But this

```python
tf.test.gpu_device_name()
```

returns an empty string.

However, on Google Colab,

```
>>> tf.config.list_physical_devices()
[PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU'),
 PhysicalDevice(name='/physical_device:XLA_CPU:0', device_type='XLA_CPU'),
 PhysicalDevice(name='/physical_device:XLA_GPU:0', device_type='XLA_GPU'),
 PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

```
>>> tf.test.gpu_device_name()
'/device:GPU:0'
```

The only meaningful difference I found between my machine and Google Colab at this point is that my machine has `XLA_GPU` devices whereas Google Colab has `GPU`. I'm not entirely sure if this has anything to do with the issue I'm having. Is anyone experiencing similar issues?
