### ISSUE

The recommended command to check CUDA Version - Running `nvcc --version` would give me below `10.2` version (But I have cuda 11 installed)

```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Wed_Oct_23_19:24:38_PDT_2019
Cuda compilation tools, release 10.2, V10.2.89

```

#### However running `/usr/local/cuda/bin/nvcc --version`

Would give me the more upgraded correct version

```

nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2020 NVIDIA Corporation
Built on Thu_Jun_11_22:26:38_PDT_2020
Cuda compilation tools, release 11.0, V11.0.194

```

#### The above discrepancy was because my PATH in .bashrc was not upgraded

running `which nvcc` gives me `/usr/bin/nvcc` but my upgraded `nvcc` resides in

`/usr/local/cuda/bin/nvcc --version`

---

## Solution

### The guide I followed on 11-Nov-2020

https://linuxconfig.org/how-to-install-cuda-on-ubuntu-20-04-focal-fossa-linux

```
sudo apt update

sudo apt install nvidia-cuda-toolkit

sudo apt install cuda

```

### NOW FINALLY, set your path to point to CUDA binaries:

```
echo 'export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}' >> ~/.bashrc

```

The above command will create a new line in my `.bashrc` as below

`export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}`

Now reload `source ~/.bashrc`

---

And now running `which nvcc` gives me `/usr/local/cuda/bin/nvcc` and running `nvcc --version` gives me

```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2020 NVIDIA Corporation
Built on Thu_Jun_11_22:26:38_PDT_2020
Cuda compilation tools, release 11.0, V11.0.194
Build cuda_11.0_bu.TC445_37.28540450_0
```

### General References on this issue

https://stackoverflow.com/questions/40517083/multiple-cuda-versions-on-machine-nvcc-v-confusion
