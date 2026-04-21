from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel

def topology():

    net = Mininet(controller=RemoteController)

    c0 = net.addController('c0', ip='127.0.0.1', port=6633)

    #  Server
    h1 = net.addHost('h1')

    #  Clients
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    h5 = net.addHost('h5')
    h6 = net.addHost('h6')

    # Switch
    s1 = net.addSwitch('s1')

    # Links (ALL traffic goes through same switch → congestion)
    net.addLink(h1, s1)

    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s1)
    net.addLink(h5, s1)
    net.addLink(h6, s1)

    net.start()

    print("SDN Topology Running")

    CLI(net)

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
