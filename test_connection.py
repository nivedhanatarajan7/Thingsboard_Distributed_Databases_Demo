from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo
from pyignite import Client
from keras.datasets import mnist
import numpy as np
import time

# Load MNIST data
mnist_file = './mnist.npz'
with np.load(mnist_file) as data:
    x_train = data['x_train']
    y_train = data['y_train']

client = Client()
client.connect('127.0.0.1', 10800)

#Create cache
my_cache = client.get_or_create_cache("testCache")

# Prepare data for insertion
documents = []
for i in range(len(x_train)):
    value = {
        'image': x_train[i].tolist(),  # Convert numpy array to list
        'label': int(y_train[i])
    }
    my_cache.put(i, value)
    documents.append(value)


# Insert data into Apache Ignite
print("Data uploaded successfully to MNISTtrain!")
print(f"Total number of documents uploaded: {len(documents)}")

start_time = time.time()

# Fetch all documents
images = []
labels = []

for i in range(len(x_train)):
    value = my_cache.get(i)
    images.append(value['image'])
    labels.append(value['label'])

# Convert lists to NumPy arrays
x_train = np.array(images, dtype=np.float32)
y_train = np.array(labels, dtype=np.int64)

end_time = time.time()

# Calculate the time taken
time_taken = end_time - start_time

print(f"\n--------Time taken to fetch train dataset: {time_taken:.4f} seconds\n------------")