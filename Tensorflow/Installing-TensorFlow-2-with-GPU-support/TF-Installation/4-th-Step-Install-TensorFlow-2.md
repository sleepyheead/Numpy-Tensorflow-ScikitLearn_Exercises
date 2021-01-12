#### Followed the below steps while being in the (base) environment in the Terminal - 4-Dec-2020

https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html - This official link suggest activating a new conda environment and installing TF with the **pip** command below

`pip install --ignore-installed --upgrade tensorflow==2.2.0` - But I did not have to

**Before you can install and run TensorFlow, you'll need to install the CUDA drivers for your machine and the cuDNN updates for it.**

### Fresh installation of Tensorflow in local machine

When installing TensorFlow, we want to make sure we are installing and upgrading to the newest version available in PyPi.

Therefore, we’ll be using the following command syntax with pip:

```
pip3 install --upgrade tensorflow

```

It will install around 516MB of packages and then check the version like below in a .py file

```py
import tensorflow as tf
print(tf.__version__)
```

Will output `2.2.0`

**To verify the installation, you can also run the following command within the terminal directly, which will print the TensorFlow version:**

```
python -c 'import tensorflow as tf; print(tf.__version__)'

```

### Extra notes on Installation

1. https://www.tensorflow.org/install/pip#2.-create-a-virtual-environment-recommended - This official guide clearly says - While the TensorFlow provided pip package is recommended, a community-supported Anaconda package is available. To install, read the [Anaconda TensorFlow guide](https://docs.anaconda.com/anaconda/user-guide/tasks/tensorflow/).

But the above **Anaconda TensorFlow guide** recommends to create a new conda environment and install TF there.

To install the current release of GPU TensorFlow on Linux or Windows:

```
conda create -n tf-gpu tensorflow-gpu
conda activate tf-gpu
```
