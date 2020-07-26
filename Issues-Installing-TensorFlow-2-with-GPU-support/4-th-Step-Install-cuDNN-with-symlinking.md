### First what is cuDNN

[According to NVIDIA](https://developer.nvidia.com/cudnn#:~:text=The%20NVIDIA%20CUDA%C2%AE%20Deep,%2C%20normalization%2C%20and%20activation%20layers.)

"The NVIDIA CUDA® Deep Neural Network library (cuDNN) is a GPU-accelerated library of primitives for deep neural networks. cuDNN provides highly tuned implementations for standard routines such as forward and backward convolution, pooling, normalization, and activation layers.

Deep learning researchers and framework developers worldwide rely on cuDNN for high-performance GPU acceleration. It allows them to focus on training neural networks and developing software applications rather than spending time on low-level GPU performance tuning. cuDNN accelerates widely used deep learning frameworks, including Caffe2, Chainer, Keras, MATLAB, MxNet, PyTorch, and TensorFlow. "

### cuDNN installation is required to resolve this issue - After running a .py file containing a TensorFlow training code I was getting the following error.

```
Ubuntu 20.04 NVDIA cuda Could not load dynamic library 'libcudnn.so.7'; dlerror: libcudnn.so.7
```

Followed this [askubuntu](https://askubuntu.com/questions/1230645/when-is-cuda-gonna-be-released-for-ubuntu-20-04)

**NOTE - For Cuda only, follow my other note as not Ubuntu 20.04's cuda package has been released.**

So I have already followed the above process and now running

`nvcc -V` correctly gives me

```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Sun_Jul_28_19:07:16_PDT_2019
Cuda compilation tools, release 10.1, V10.1.243

```

Then running `dpkg -l | grep cuda-toolkit` correctly gives me

```
ii  cuda-toolkit-11-0                             11.0.2-1                                  amd64        CUDA Toolkit 11.0 meta-package
ii  nvidia-cuda-toolkit                           10.1.243-3                                amd64        NVIDIA CUDA development toolkit

```

AND also `cat /usr/local/cuda/version.txt` correctly gives me

`CUDA Version 11.0.207`

## NOW the most important step - Install cuDNN (7.6.5) - This is what I did on 25-July-2020

First go to **[this official link][3]** then choose _Download cuDNN_. You'll be asked to login/create an account. After logging in and customary acceptance of _the Terms of the cuDNN Software License Agreement_.

A list of downloadable cuDNN will be displayed > Expand the section for **Download cuDNN v7.6.5 (November 5th, 2019), for CUDA 10.1** .

**Important Note - Do NOT choose the files under any other section like "cuDNN Runtime Library for Ubuntu18.04 (Deb)" or "cuDNN Developer Library for Ubuntu18.04 (Deb)"**

![](2020-07-26-07-48-25.png)

After the download is finished, extract the file in your locally downloaded directory

#### Then then open the terminal in that downloaded-directory and run:

`sudo cp cuda/include/cudnn.h /usr/lib/cuda/include/`

To copy the `cuda/include/cudnn.h` file to `/usr/lib/cuda/include/` folder. You can ofcourse manually copy this file as well, i.e. without using the Terminal.

After that: Copy all files under `cuda/lib64/` to `/usr/lib/cuda/lib64/` folder

    `sudo cp cuda/lib64/libcudnn* /usr/lib/cuda/lib64/`

#### Finally: add read permission to both these target directory

    `sudo chmod a+r /usr/lib/cuda/include/cudnn.h /usr/lib/cuda/lib64/libcudnn*`

#### Once you finish, you have to add the CUDA path to your `~/.bashrc` file. You need to run:

```
    echo 'export LD_LIBRARY_PATH=/usr/lib/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
    echo 'export LD_LIBRARY_PATH=/usr/lib/cuda/include:$LD_LIBRARY_PATH' >> ~/.bashrc

```

Then reload .bashrc by running:

    `source ~/.bashrc`

### Finally to verify the correct installation

Then run `python3` and type the following lines:

```
    import tensorflow as tf
    tf.config.list_physical_devices('GPU')

```

If everything went as planned, you'll get an output telling that Tensorflow has access to your GPU.

### Also alternatively, test Installation of TensorFlow and its access to GPU

Open Terminal > type `python` which will start the shell.

Then, ONLY to test CUDA support for your Tensorflow installation, you can run the following command in the shell:

`import tensorflow as tf`

```
tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None)
```

It takes a few minutes to return a result from this; when it is finished it returns True

[1]: https://askubuntu.com/users/263979/meetnick
[2]: https://askubuntu.com/a/1231356/822295
[3]: https://developer.nvidia.com/rdp/form/cudnn-download-survey
