import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)
W = tf.get_variable('big_matrix', shape=(20, 10), initializer=tf.zeros_initializer())
H = tf.Variable(tf.constant(10))

print(a)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    x, W = sess.run([x, W])
    print(W, H.eval())