#### While Installing CUDA 11 in Ubuntu 20.04

After running `sudo apt-get install cuda` and I get an error about not being able to install `libnvidia-compute-450`.

So I run `sudo apt-get --fix-broken` install and I get error of the following form

```
libdvd-pkg: `apt-get check` failed, you may have broken packages. Aborting...
E: Sub-process /usr/bin/dpkg returned an error code (1)error code (1)
```

I managed to solve it by forcing its installation with

`sudo apt-get -o Dpkg::Options::="--force-overwrite" install libnvidia-compute-450`

**[Source of the Solution](https://askubuntu.com/questions/1251000/installing-cuda-11-in-ubuntu-20-04-with-nvida-gtx-1060)**

And also [this github-issue](https://github.com/tensorflow/tensorflow/issues/40278)
