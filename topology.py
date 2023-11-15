from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def simpleTopology():
    # Initialize the Mininet network simulator
    net = Mininet(controller=Controller, switch=OVSKernelSwitch)

    info('*** Adding controller\n')
    # Add a default OpenFlow controller
    c0 = net.addController('c0')

    info('*** Adding hosts\n')
    # Add two hosts, each with a default IP address
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')

    info('*** Adding switch\n')
    # Add a single Open vSwitch
    s1 = net.addSwitch('s1')

    info('*** Creating links\n')
    # Create a link between each host and the switch
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    info('*** Starting network\n')
    # Start the network
    net.build()
    c0.start()
    s1.start([c0])

    info('*** Running CLI\n')
    # Run the Mininet CLI
    CLI(net)

    info('*** Stopping network\n')
    # Stop the network
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    simpleTopology()
