### Fresh installation of Tensorflow in local machine

When installing TensorFlow, we want to make sure we are installing and upgrading to the newest version available in PyPi.

Therefore, we’ll be using the following command syntax with pip:

`pip3 install --upgrade tensorflow`

It will install around 516MB of packages and then check the version like below in a .py file

```py
import tensorflow as tf
print(tf.__version__)
```

Will output `2.2.0`

**To verify the installation, you can also run the following command within the terminal directly, which will print the TensorFlow version:**

`python -c 'import tensorflow as tf; print(tf.__version__)'`