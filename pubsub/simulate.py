from pubsub import Broker, Publisher, Subscriber
br = Broker('./store/')
p1 = Publisher('p1', br)
p1.addTopic('t1')
p2 = Publisher('p2', br)
p2.addTopic('t2')
c1 = Subscriber('c1', br)
c1.addTopic('t1')
c2 = Subscriber('c2', br)
c2.addTopic('t2')
p2.publish('t2', 'hello t2')
p1.publish('t1', 'hello t1')
