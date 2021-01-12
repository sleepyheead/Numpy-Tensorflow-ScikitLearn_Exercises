### Install cuDNN - This is probably relatively trickier than the other steps in this whole procedures

If before installing cuDNN - you try to run a .py file containing a TensorFlow training code I was getting the following error.

```
Ubuntu 20.04 NVDIA cuda Could not load dynamic library 'libcudnn.so.7'; dlerror: libcudnn.so.7
```

### So to resolve the above you need to install cuDNN (7.6.5)

Followed this very helpful [askubuntu](https://askubuntu.com/questions/1230645/when-is-cuda-gonna-be-released-for-ubuntu-20-04)

First go to **[this official link][3]** then choose _Download cuDNN_. You'll be asked to login/create an account. After logging in and customary acceptance of _the Terms of the cuDNN Software License Agreement_.

A list of downloadable cuDNN will be displayed > Expand the section for **Download cuDNN v7.6.5 (November 5th, 2019), for CUDA 10.1** .

**Important Note - Do NOT choose the files under any other section like "cuDNN Runtime Library for Ubuntu18.04 (Deb)" or "cuDNN Developer Library for Ubuntu18.04 (Deb)"**

![](assets/2020-07-26-07-48-25.png)

After the download is finished, extract the file in your locally downloaded directory

#### Then open the terminal in that downloaded-directory and run:

`sudo cp cuda/include/cudnn.h /usr/lib/cuda/include/`

To copy the `cuda/include/cudnn.h` file to `/usr/lib/cuda/include/` folder. You can of-course manually copy this file as well, i.e. without using the Terminal.

After that: Copy all files under `cuda/lib64/` to `/usr/lib/cuda/lib64/` folder

    `sudo cp cuda/lib64/libcudnn* /usr/lib/cuda/lib64/`

#### Finally: add read permission to both these target directory

    `sudo chmod a+r /usr/lib/cuda/include/cudnn.h /usr/lib/cuda/lib64/libcudnn*`

#### Once you finish, you have to add the CUDA path to your `~/.bashrc` file. Open ~/.bashrc and add following lines

```
    echo 'export LD_LIBRARY_PATH=/usr/lib/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
    echo 'export LD_LIBRARY_PATH=/usr/lib/cuda/include:$LD_LIBRARY_PATH' >> ~/.bashrc

```

Then reload .bashrc by running:

    `source ~/.bashrc`

## Finally to verify the correct installation

Then run `python3` and type the following lines:

```
    import tensorflow as tf
    tf.config.list_physical_devices('GPU')
```

Or in a Terminal you can write

```
python -c 'import tensorflow as tf; print(tf.__version__)'
```

If everything went as planned, you'll get an output telling that Tensorflow has access to your GPU and you will see the following kind of output

```
2020-07-26 08:26:17.262278: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcuda.so.1
2020-07-26 08:26:17.299067: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-07-26 08:26:17.299364: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1561] Found device 0 with properties:
pciBusID: 0000:01:00.0 name: GeForce GT 730 computeCapability: 3.5
coreClock: 0.9015GHz coreCount: 2 deviceMemorySize: 3.95GiB deviceMemoryBandwidth: 11.92GiB/s
2020-07-26 08:26:17.299580: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2020-07-26 08:26:17.300985: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
2020-07-26 08:26:17.301897: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcufft.so.10
2020-07-26 08:26:17.302118: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcurand.so.10
2020-07-26 08:26:17.304091: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusolver.so.10
2020-07-26 08:26:17.304845: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusparse.so.10
2020-07-26 08:26:17.307859: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
2020-07-26 08:26:17.307977: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-07-26 08:26:17.308322: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-07-26 08:26:17.308579: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]

```

## Also alternatively, test Installation of TensorFlow and its access to GPU

Open Terminal > type `python` which will start the shell. then type

`import tensorflow as tf`

Then, ONLY to test CUDA support for your Tensorflow installation, you can run the following command in the shell:

`tf.test.is_built_with_cuda()`

Should return **True**

**Finally, to confirm that the GPU is available to Tensorflow, you can test using a built-in utility function in TensorFlow as shown here:**

```
tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None)
```

It takes a few minutes to return a result from this; when it is finished it returns **`True`** and the full Terminal output will be like below.

```
2020-07-26 08:29:00.239996: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x52e4c10 initialized for platform CUDA (this does not guarantee that XLA will be used). Devices:
2020-07-26 08:29:00.240016: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): GeForce GT 730, Compute Capability 3.5
2020-07-26 08:29:00.240194: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-07-26 08:29:00.240474: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1561] Found device 0 with properties:
pciBusID: 0000:01:00.0 name: GeForce GT 730 computeCapability: 3.5
coreClock: 0.9015GHz coreCount: 2 deviceMemorySize: 3.95GiB deviceMemoryBandwidth: 11.92GiB/s
2020-07-26 08:29:00.240713: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2020-07-26 08:29:00.242165: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
2020-07-26 08:29:00.243010: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcufft.so.10
2020-07-26 08:29:00.243236: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcurand.so.10
2020-07-26 08:29:00.245184: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusolver.so.10
2020-07-26 08:29:00.246093: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusparse.so.10
2020-07-26 08:29:00.249772: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
2020-07-26 08:29:00.249888: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-07-26 08:29:00.250286: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-07-26 08:29:00.250579: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2020-07-26 08:29:00.250623: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2020-07-26 08:29:00.251075: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-07-26 08:29:00.251093: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1108]      0
2020-07-26 08:29:00.251101: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1121] 0:   N
2020-07-26 08:29:00.251213: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-07-26 08:29:00.251559: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-07-26 08:29:00.251871: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/device:GPU:0 with 2996 MB memory) -> physical GPU (device: 0, name: GeForce GT 730, pci bus id: 0000:01:00.0, compute capability: 3.5)
True
```

[1]: https://askubuntu.com/users/263979/meetnick
[2]: https://askubuntu.com/a/1231356/822295
[3]: https://developer.nvidia.com/rdp/form/cudnn-download-survey
