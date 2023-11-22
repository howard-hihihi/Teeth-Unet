import tensorflow as tf

# 檢查是否有可用的 GPU 裝置
gpu_devices = tf.config.list_physical_devices('GPU')
print(gpu_devices)
gpu_devices = tf.test.is_built_with_cuda()
print(gpu_devices)


'''=========='''

# from tensorflow.python.client import device_lib
# print(device_lib.list_local_devices())