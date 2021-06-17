import tensorflow as tf

if {{cookiecutter.datapath}} == "mnist":
    tf.keras.datasets.mnist.load_data(path="data/"+{{cookiecutter.datapath}}+".npz")
else:
    tf.keras.datasets.fashion_mnist.load_data(path="data/"+{{cookiecutter.datapath}}+".npz")