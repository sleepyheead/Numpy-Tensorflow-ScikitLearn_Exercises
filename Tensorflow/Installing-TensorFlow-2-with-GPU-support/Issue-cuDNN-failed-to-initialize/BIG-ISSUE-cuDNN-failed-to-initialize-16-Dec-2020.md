## THE BIG ISSUE

```
Failed to get convolution algorithm. This is probably because cuDNN failed to initialize, so try looking to see if a warning log message was printed above
```

---

## MY LIFE SAVER

FORTUNATELY I GOT IT WORKING VERY SOON - BUT IT MAY NOT BE LIKE THIS NEXT TIME

https://github.com/tensorflow/tensorflow/issues/24828#issuecomment-689552885

Set the TF_FORCE_GPU_ALLOW_GROWTH environment variable to true.
In your terminal, run this command.

```
export TF_FORCE_GPU_ALLOW_GROWTH=true

```

#### Details on TF_FORCE_GPU_ALLOW_GROWTH

As explained [here](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/guide/gpu.ipynb#scrollTo=ARrRhwqijPzN)

"By default, TensorFlow maps nearly all of the GPU memory of all GPUs (subject to CUDA_VISIBLE_DEVICES) visible to the process. This is done to more efficiently use the relatively precious GPU memory resources on the devices by reducing memory fragmentation. To limit TensorFlow to a specific set of GPUs we use the tf.config.experimental.set_visible_devices method.

In some cases it is desirable for the process to only allocate a subset of the available memory, or to only grow the memory usage as is needed by the process. TensorFlow provides two methods to control this.

The first option is to turn on memory growth by calling tf.config.experimental.set_memory_growth, which attempts to allocate only as much GPU memory as needed for the runtime allocations: it starts out allocating very little memory, and as the program gets run and more GPU memory is needed, we extend the GPU memory region allocated to the TensorFlow process. Note we do not release memory, since it can lead to memory fragmentation.

Another way to enable this option is to set the environmental variable TF_FORCE_GPU_ALLOW_GROWTH to true. This configuration is platform specific."

Some further explanation about **TF_FORCE_GPU_ALLOW_GROWTH** from this [Reddit thread](https://www.reddit.com/r/MachineLearning/comments/ea083i/d_tensorflow_gpu_memory_management_tf_force_gpu/)

"The reason for the TF_FORCE_GPU_ALLOW_GROWTH flag is to allow TF to play nice with other apps (or TF instances?) that also need to use GPU memory. The issue is that GPU memory is fundamentally managed by CUDA API's, but for efficiency TF wants to manage the memory itself, so TF maintains it's own heap (memory allocator) using GPU memory it obtained via CUDA, and TF applications then allocate/release memory to/from the TF heap, not directly to/from CUDA.

The TF heap only ever grows, when needed (i.e. if a TF app requests more memory than TF currently has available), by grabbing more memory from CUDA. TF never shrinks its heap by releasing memory back to CUDA. The TF_FORCE_GPU_ALLOW_GROWTH flag determines whether TF grabs all the CUDA memory it wants at start-up, or - to play nice with other CUDA apps - starts small and grabs more memory only as needed."

And the Tensorflow source code of this flag is [here](https://github.com/tensorflow/tensorflow/blob/3e21fe5faedab3a8258d344c8ad1cec2612a8aa8/tensorflow/core/common_runtime/gpu/gpu_bfc_allocator.cc#L25)

---

### Some more information abut the problem for future reference ( incompatibility in cuda, cudnn and Nvidia drivers or versions)

#### Main Git issue page - https://github.com/tensorflow/tensorflow/issues/24828

It has 270 comments

---

https://medium.com/@JeansPantRushi/fix-for-tensorflow-v2-failed-to-get-convolution-algorithm-b367a088b56e

#### "This could be caused by either an incompatibility in cuda, cudnn and Nvidia drivers or memory growth issue. The solution in the article addresses the memory growth issue as I had hard time finding a solution for it."

---

### Some useful information about the Problem

https://github.com/tensorflow/tensorflow/issues/24828#issuecomment-734529155

The problem doesn't appear on TF2.1 and CUDA 10.1

---

### Following solution mentioned by many in the issue above did not work

```python

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(graph=self.graph, config=config)

# ***

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

# ***

from tensorflow.compat.v1 import ConfigProto
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)

```
