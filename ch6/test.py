import tensorflow as tf

g1 = tf.Graph()
with g1.as_default():
    v1 = tf.Variable(1, name= "v1")
print(v1._variable)
print("---------------------------------------------------")
print(v1.op)
print("---------------------------------------------------")
print(g1.as_graph_def())
print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")

with tf.Session(graph=g1) as sess:
    init = tf.global_variables_initializer()
    print(init)
print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")

with g1.as_default():
    v = tf.Variable(1, name= "v1")
    v = v+1
    v = tf.assign(v, v + 1)
print("---------------------------------------------------")

with tf.Session(graph=g1) as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(v))

