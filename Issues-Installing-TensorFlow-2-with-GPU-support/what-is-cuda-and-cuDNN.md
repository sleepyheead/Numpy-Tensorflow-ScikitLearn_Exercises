## What is CUDA? If we can perform TensorFlow's computation directly from a GPU, then why do we actually need it?

CUDA(Compute Unified Device Architecture) is a set of Programming APIs which is released by Nvidia to use and program the Nvidia GPU cores(CUDA cores).

Previously this cores only served the purpose of rendering the Graphics but since High computing requirement has arisen, Nvidia made a way to use this cores in a way GPGPU(General Purpose GPU) Computing.

These CUDA cores are indeed very slow compared to the cores of CPUs but they are available in abundance(normal CPU cores: 4–16 vs Normal GPU cores: 128–384) in GPU. So one can use these cores concurrently in parallel computing to enhance the performance of the application or program.

Addition to that GPUs are very good at SIMD which adds the boost in performance.

Now coming to your second question”Why do we actually need it?”. We need it because it’s an interface of communication between your application/program and GPUs. Nvidia has already implemented library called cuDNN which is only for these kind of applications. So using CUDA will give better performance.

## What is cuDNN

[According to NVIDIA](https://developer.nvidia.com/cudnn#:~:text=The%20NVIDIA%20CUDA%C2%AE%20Deep,%2C%20normalization%2C%20and%20activation%20layers.)

"The NVIDIA CUDA® Deep Neural Network library (cuDNN) is a GPU-accelerated library of primitives for deep neural networks. cuDNN provides highly tuned implementations for standard routines such as forward and backward convolution, pooling, normalization, and activation layers.

Deep learning researchers and framework developers worldwide rely on cuDNN for high-performance GPU acceleration. It allows them to focus on training neural networks and developing software applications rather than spending time on low-level GPU performance tuning. cuDNN accelerates widely used deep learning frameworks, including Caffe2, Chainer, Keras, MATLAB, MxNet, PyTorch, and TensorFlow. "
