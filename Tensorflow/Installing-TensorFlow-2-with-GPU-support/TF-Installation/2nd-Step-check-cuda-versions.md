### 1. The first method is to check the version of the Nvidia CUDA Compiler nvcc. To do so execute:

`nvcc --version`

```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Wed_Oct_23_19:24:38_PDT_2019
Cuda compilation tools, release 10.2, V10.2.89

```

(or `/usr/local/cuda/bin/nvcc --version`) gives the CUDA compiler version (which matches the toolkit version).

From application code, you can query the runtime API version with

    cudaRuntimeGetVersion()

or the driver API version with

    cudaDriverGetVersion()

As Daniel points out, deviceQuery is an SDK sample app that queries the above, along with device capabilities.

As others note, you can also check the contents of the `version.txt` using (e.g., on Mac or Linux)

    cat /usr/local/cuda/version.txt

However, if there is another version of the CUDA toolkit installed other than the one symlinked from `/usr/local/cuda`, this may report an inaccurate version if another version is earlier in your `PATH` than the above, so use with caution.

---

### 2. Given that you have the Nvidia driver installed on your Ubuntu 20.04 system, the following command will also reveal the CUDA version:

`nvidia-smi`

I got below

![](assets/2020-07-26-03-52-33.png)

### 3. If you did not changed the default CUDA installation path, you can also check the CUDA version simply by viewing the content of the /usr/local/cuda/version.txt file:

```
$ cat /usr/local/cuda/version.txt
CUDA Version 11.0.207
```

### 4. Check for installed CUDA toolkit package:

```
$ dpkg -l | grep cuda-toolkit
ii  cuda-toolkit-11-0                             11.0.2-1                                  amd64        CUDA Toolkit 11.0 meta-package
ii  nvidia-cuda-toolkit                           10.1.243-3                                amd64        NVIDIA CUDA development toolkit

```

[https://linuxconfig.org/how-to-check-cuda-version-on-ubuntu-20-04-focal-fossa-linux](https://linuxconfig.org/how-to-check-cuda-version-on-ubuntu-20-04-focal-fossa-linux)
