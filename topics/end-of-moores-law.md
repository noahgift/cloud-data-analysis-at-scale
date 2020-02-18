## End of Moore’s Law

Perhaps the best source to describe what is happening with chips is [Dr. David Patterson a professor at UC Berkeley](https://content.riscv.org/wp-content/uploads/2018/12/A-New-Golden-Age-for-Computer-Architecture-History-Challenges-and-Opportunities-David-Patterson-.pdf) and an architect for the TPU (Tensorflow Processing Unit).

![Screen Shot 2020-02-18 at 11 49 01 AM](https://user-images.githubusercontent.com/58792/74757959-b4098d00-5244-11ea-8eea-da0929cec796.png)

The high-level version is that CPU clock speed is effectively dead.  This opens up an opportunity for new solutions.  These solutions involve both cloud computing and also specialized chips called [ASICs](https://en.wikipedia.org/wiki/Application-specific_integrated_circuit).


## ASICS:  GPUs, TPUs, FPGA

### ASIC vs CPU vs GPU

**TPU in Production**
![TPU Production](https://user-images.githubusercontent.com/58792/45001200-fd4a1c00-af7f-11e8-8fef-530cf2d70ada.png)

**CPU**
![How CPUs work](https://user-images.githubusercontent.com/58792/45001241-5d40c280-af80-11e8-9a82-81f900995721.png)

**GPU**
![GPUs work](https://user-images.githubusercontent.com/58792/45001287-b90b4b80-af80-11e8-9cc7-cc6d2fb2b19c.png)

**TPU**
![TPUs work](https://user-images.githubusercontent.com/58792/45001315-ef48cb00-af80-11e8-8880-aa59a272e095.png)

Sources: https://storage.googleapis.com/nexttpu/index.html

### Using GPUs and JIT

*Screencast* [![Do GPU Programming with CUDA, Numba and Colab!](https://img.youtube.com/vi/ny7a_OQdyvc/0.jpg)](https://youtu.be/ny7a_OQdyvc)

One of the easiest ways to use a Just in Time compiler (JIT) or a GPU is to use a library like [numba](https://numba.pydata.org/numba-doc/latest/cuda/overview.html) and a hosted runtime like [Google Colab](https://github.com/noahgift/cloud-data-analysis-at-scale/blob/master/GPU_Programming.ipynb).  

There is a step by step example of how to use these operations in the following notebook (https://github.com/noahgift/cloud-data-analysis-at-scale/blob/master/GPU_Programming.ipynb)[https://github.com/noahgift/cloud-data-analysis-at-scale/blob/master/GPU_Programming.ipynb].  The main high level takeaway is that the GPU runtime in colab must be enabled.

![Screen Shot 2020-02-18 at 12 44 56 PM](https://user-images.githubusercontent.com/58792/74762754-7f013880-524c-11ea-9e5d-3cf2af8f64ef.png)

Next up install `numba` and double check the CUDA `.so` libraries are available.

```
!pip install numba
!find / -iname 'libdevice'
!find / -iname 'libnvvm.so'
```

You should see something like this.

```bash
/usr/local/cuda-10.0/nvvm/libdevice
/usr/local/cuda-10.1/nvvm/libdevice
/usr/local/cuda-10.0/nvvm/lib64/libnvvm.so
/usr/local/cuda-10.1/nvvm/lib64/libnvvm.so
```

Next up try one of the methods for speeding up your code.

#### GPU Workflow
[TO DO:  Create GPU vectorize workflow diagram]

### Exercise

* Topic:  Go through [colab example here](https://github.com/noahgift/cloud-data-analysis-at-scale/blob/master/GPU_Programming.ipynb)
* Estimated time:  20-30 minutes
* People:  Individual or Final Project Team
* Slack Channel:  #noisy-exercise-chatter
* Directions:
  * Part A:  Get code working in colab
  * Part B:  Make your own GPU or JIT code to speed up a project you are working on.  Share in slack and/or create a technical blog post about it.