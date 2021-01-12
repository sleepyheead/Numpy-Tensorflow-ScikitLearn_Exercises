## Alt-1

```python
import tensorflow as tf

from tensorflow.python.client import device_lib

device_lib.list_local_devices()
```

### Output

```
[name: "/device:CPU:0"
 device_type: "CPU"
 memory_limit: 268435456
 locality {
 }
 incarnation: 11248873635033752949,
 name: "/device:XLA_CPU:0"
 device_type: "XLA_CPU"
 memory_limit: 17179869184
 locality {
 }
 incarnation: 17922956980258821587
 physical_device_desc: "device: XLA_CPU device",
 name: "/device:XLA_GPU:0"
 device_type: "XLA_GPU"
 memory_limit: 17179869184
 locality {
 }
 incarnation: 8360513798352767371
 physical_device_desc: "device: XLA_GPU device"]
```

---

## Alt-2

```python

import tensorflow as tf

print(tf.config.list_physical_devices())
```

#### OUTPUT

```
[PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU'), PhysicalDevice(name='/physical_device:XLA_CPU:0', device_type='XLA_CPU'), PhysicalDevice(name='/physical_device:XLA_GPU:0', device_type='XLA_GPU')]
```
