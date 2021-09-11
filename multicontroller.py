
from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI 
from mininet.log import setLogLevel

    def multiContrller():
    #Create a network with multiple controllers 
    
    net = Mininet( controller=Controller,Switch=OVSSwitch, build=False )
    
    print "&&&&&& Creating (reference) Controllers &&&&&&"
    c0 = net.addController('c0', port=6633)
    c1 = net.addController('c1', port=6644)
    c2 = net.addController('c2', port=6655)
    c3 = net.addController('c3', port=6666)
   

    
    print "&&&&& Creating Switches &&&&&&"
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    
    s5 = net.addSwitch('s5')
    s6 = net.addSwitch('s6')
   
    print "&&&&& Creating Hosts &&&&&&"
    h1 = [net.addHost(h1)]
    h2 = [net.addHost(h2)]
    h3 = [net.addHost(h3)]
    h4 = [net.addHost(h4)]
    
    h5 = [net.addHost(h5)]
    h6 = [net.addHost(h6)]
    h7 = [net.addHost(h7)]
    h8 = [net.addHost(h8)]
    
    h9 = [net.addHost(h9)]
    h10 = [net.addHost(h10)]
    h11 = [net.addHost(h11)]
    h12 = [net.addHost(h12)]
    
    print "&&&& Creating Links &&&&"
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    
    net.addLink(h5, s3)
    net.addLink(h6, s3)
    
    net.addLink(h7, s4)
    net.addLink(h8, s4)
    
    net.addLink(h9, s5)
    net.addLink(h10, s5)
    
    net.addLink(h11, s6)
    net.addLink(h12, s6)
    
    print "&&&&& Start Network &&&&&"
    net.build()
    c0.start()
    c1.start( [ c0 ] )
    c2.start( [ c0 ] )
    c3.start( [ c0 ] )
   
    
    s1.start( [ c1 ] )
    s2.start( [ c1 ] )
    
    s3.start( [ c2 ] )
    s4.start( [ c2 ] )
    
    s5.start( [ c3 ] )
    s6.start( [ c3 ] )
 

    print "&&&&Testing Network&&&"
    net.pingAll()
    
    print "&&&& Running CLI &&&&&"
    CLI( net )
    
    print "&&&& Stopping Network &&&&&"
    net.stop()
    
    if __name__ == '__main__':
    setLogLevel( 'info' )  # for CLI output
    multiControllerNet()
    
    
    
    
    
