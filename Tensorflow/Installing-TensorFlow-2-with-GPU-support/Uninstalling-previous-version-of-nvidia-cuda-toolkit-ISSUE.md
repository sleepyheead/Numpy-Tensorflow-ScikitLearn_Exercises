I wanted to install CUDA on ubuntu 20.04 and was following the instructions here https://linuxconfig.org/how-to-install-cuda-on-ubuntu-20-04-focal-fossa-linux

But I already had the nvidia-cuda-toolkit packages installed from the ubuntu repo, but then discovered I needed version 10.2.

So I did a `apt-get remove nvidia-cuda-toolkit` and then went through the instructions for installing from the cuda repo but that failed dues to broken packages (uninstalling nvidia-cuda-toolkit was not clean).

Now I'm stuck. I try this:

```
# apt-get remove cuda
Reading package lists... Done
Building dependency tree
Reading state information... Done
Package 'cuda' is not installed, so not removed
You might want to run 'apt --fix-broken install' to correct these.
The following packages have unmet dependencies.
 cuda-libraries-10-2 : Depends: libcublas10 (>= 10.2.2.89) but 10.1.243-3 is to be installed
 libcublas-dev : Depends: libcublas10 (>= 10.2.2.89) but 10.1.243-3 is to be installed
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).
```

So I try this:

```
# apt --fix-broken install
Reading package lists... Done
Building dependency tree
Reading state information... Done
Correcting dependencies... Done
The following packages were automatically installed and are no longer required:
  ca-certificates-java cuda-10-2 cuda-command-line-tools-10-2 cuda-compiler-10-2 cuda-cudart-10-2 cuda-cudart-dev-10-2 cuda-cufft-10-2
  cuda-cufft-dev-10-2 cuda-cuobjdump-10-2 cuda-cupti-10-2 cuda-cupti-dev-10-2 cuda-curand-10-2 cuda-curand-dev-10-2 cuda-cusolver-10-2
  cuda-cusolver-dev-10-2 cuda-cusparse-10-2 cuda-cusparse-dev-10-2 cuda-demo-suite-10-2 cuda-documentation-10-2 cuda-driver-dev-10-2
  cuda-drivers cuda-gdb-10-2 cuda-libraries-10-2 cuda-libraries-dev-10-2 cuda-license-10-2 cuda-memcheck-10-2 cuda-misc-headers-10-2
  cuda-npp-10-2 cuda-npp-dev-10-2 cuda-nsight-10-2 cuda-nsight-compute-10-2 cuda-nsight-systems-10-2 cuda-nvcc-10-2 cuda-nvdisasm-10-2
  cuda-nvgraph-10-2 cuda-nvgraph-dev-10-2 cuda-nvjpeg-10-2 cuda-nvjpeg-dev-10-2 cuda-nvml-dev-10-2 cuda-nvprof-10-2 cuda-nvprune-10-2
  cuda-nvrtc-10-2 cuda-nvrtc-dev-10-2 cuda-nvtx-10-2 cuda-nvvp-10-2 cuda-runtime-10-2 cuda-samples-10-2 cuda-sanitizer-api-10-2
  cuda-toolkit-10-2 cuda-tools-10-2 cuda-visual-tools-10-2 default-jre default-jre-headless fonts-dejavu-extra freeglut3 freeglut3-dev g++-8
  java-common javascript-common libaccinj64-10.1 libatk-wrapper-java libatk-wrapper-java-jni libcublas-dev libcublas10 libcublaslt10 libcufft10
  libcufftw10 libcuinj64-10.1 libcupti-dev libcupti-doc libcupti10.1 libcurand10 libcusolver10 libcusolvermg10 libcusparse10 libegl-dev
  libgl-dev libgl1-mesa-dev libgles-dev libgles1 libglu1-mesa-dev libglvnd-dev libglx-dev libice-dev libjs-jquery libjs-underscore libncurses5
  libnppc10 libnppial10 libnppicc10 libnppicom10 libnppidei10 libnppif10 libnppig10 libnppim10 libnppist10 libnppisu10 libnppitc10 libnpps10
  libnvblas10 libnvgraph10 libnvidia-ml-dev libnvjpeg10 libnvrtc10.1 libnvtoolsext1 libnvvm3 libopengl-dev libopengl0 libpthread-stubs0-dev
  libsm-dev libstdc++-8-dev libthrust-dev libtinfo5 libvdpau-dev libx11-dev libxau-dev libxcb1-dev libxdmcp-dev libxext-dev libxfixes-dev
  libxi-dev libxmu-dev libxmu-headers libxt-dev node-html5shiv nsight-compute nsight-systems nvidia-modprobe nvidia-opencl-dev nvidia-profiler
  nvidia-visual-profiler ocl-icd-opencl-dev opencl-c-headers openjdk-11-jre openjdk-11-jre-headless openjdk-8-jre openjdk-8-jre-headless
  x11proto-core-dev x11proto-dev x11proto-input-dev x11proto-xext-dev xorg-sgml-doctools xtrans-dev
Use 'apt autoremove' to remove them.
The following additional packages will be installed:
  libcublas10
The following packages will be upgraded:
  libcublas10
1 to upgrade, 0 to newly install, 0 to remove and 5 not to upgrade.
11 not fully installed or removed.
Need to get 0 B/42.2 MB of archives.
After this operation, 35.8 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
(Reading database ... 190757 files and directories currently installed.)
Preparing to unpack .../libcublas10_10.2.2.89-1_amd64.deb ...
Unpacking libcublas10 (10.2.2.89-1) over (10.1.243-3) ...
dpkg: error processing archive /var/cache/apt/archives/libcublas10_10.2.2.89-1_amd64.deb (--unpack):
 trying to overwrite '/usr/lib/x86_64-linux-gnu/libnvblas.so.10', which is also in package libnvblas10:amd64 10.1.243-3
Errors were encountered while processing:
 /var/cache/apt/archives/libcublas10_10.2.2.89-1_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

I can't remove the offending packages and I can't fix the broken packages.
Any ideas how to get out of this impasse?

## Solution

Run the command:

`sudo apt --fix-broken install -o Dpkg::Options::="--force-overwrite"`

**[Source](https://askubuntu.com/questions/1238715/unable-to-fix-broken-packages-when-installing-cuda)**
