### What is CUDA in relation to NVIDIA in Ubuntu

[CUDA®](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) is a parallel computing platform and programming model invented by NVIDIA®. It enables dramatic increases in computing performance by harnessing the power of the graphics processing unit (GPU).

CUDA-capable GPUs have hundreds of cores that can collectively run thousands of computing threads. These cores have shared resources including a register file and a shared memory. The on-chip shared memory allows parallel tasks running on these cores to share data without sending it over the system memory bus.

**System Requirements**

- To use CUDA on your system, you will need the following installed:
- CUDA-capable GPU
- A supported version of Linux with a gcc compiler and toolchain
- NVIDIA CUDA Toolkit (available at http://developer.nvidia.com/cuda-downloads)

### My first trial to install Cuda

And the below steps seems to have worked.

Following [askubuntu.com/when-is-cuda-gonna-be-released-for-ubuntu-20-04](https://askubuntu.com/questions/1230645/when-is-cuda-gonna-be-released-for-ubuntu-20-04)

As per now, there is no deb file or run file for Ubuntu 20.04, so the only solution is to run:

```
    sudo apt install nvidia-cuda-toolkit

```

It will take a while to be installed.
After that, to make sure that CUDA is installed, run:

    `nvcc -V`

You would get an output similar to the following:

```
    nvcc: NVIDIA (R) Cuda compiler driver
    Copyright (c) 2005-2019 NVIDIA Corporation
    Built on Sun_Jul_28_19:07:16_PDT_2019
    Cuda compilation tools, release 10.1, V10.1.243

```

This means that CUDA is successfully installed on your Ubuntu 20.04.

#### The slight difference is that cuda is not installed in the usual path (`/usr/local/cuda`, `/usr/local/cuda-10.1`). Instead, it is installed in `/usr/lib/` (`/usr/lib/cuda/`).

You can get where CUDA is installed by running the following command:

`whereis cuda`

#### Note that the above problem of NOT installing cuda at the right directory in Ubuntu was indeed there when following the above steps ( i.e. directly running `sudo apt install nvidia-cuda-toolkit` ) - BUT after NVIDIA Cuda 11 Toolkit for Ubuntu 20.04 was finally released and I followed the below official guidance - the above issue of misplacing the `cuda` file WAS NO MORE THERE.

Now running `whereis cuda` will give me correctly

`cuda: /usr/lib/cuda /usr/include/cuda.h /usr/local/cuda`

### Now installing the latest Cuda release for Ubuntu 20.04

1. [https://illya13.github.io/RL/tutorial/2020/04/26/installing-tensorflow-on-ubuntu-20.html](https://illya13.github.io/RL/tutorial/2020/04/26/installing-tensorflow-on-ubuntu-20.html)

[NVIDIA Cuda 11 Toolkit for Ubuntu 20.04](https://developer.nvidia.com/cuda-downloads) is finally released.

```none
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin

sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600

wget http://developer.download.nvidia.com/compute/cuda/11.0.2/local_installers/cuda-repo-ubuntu2004-11-0-local_11.0.2-450.51.05-1_amd64.deb

sudo dpkg -i cuda-repo-ubuntu2004-11-0-local_11.0.2-450.51.05-1_amd64.deb

sudo apt-key add /var/cuda-repo-ubuntu2004-11-0-local/7fa2af80.pub

sudo apt-get update

sudo apt-get -y install cuda
```

The above commands are after selecting Ubuntu and other relevant system architecture. And the last command from above will install 3.8 GB of packages.

Now running `nvcc -V` will give me

```
nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Sun_Jul_28_19:07:16_PDT_2019
Cuda compilation tools, release 10.1, V10.1.243
```

And also now running `whereis cuda` will give me correctly

`cuda: /usr/lib/cuda /usr/include/cuda.h /usr/local/cuda`

And I tried to install cuda again by running `sudo apt-get install cuda` after above and it says

`cuda is already the newest version (11.0.2-1)`

### Pre-installation Actions

Some actions must be taken before the CUDA Toolkit and Driver can be installed on Linux:
Verify the system has a CUDA-capable GPU.
Verify the system is running a supported version of Linux.
Verify the system has gcc installed.
Verify the system has the correct kernel headers and development packages installed.
Download the NVIDIA CUDA Toolkit.
Handle conflicting installation methods.

#### And all the commands and details for all the above checks are explanied more tin this very important [official Link - cuda-installation-guide-linux/index.html](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
