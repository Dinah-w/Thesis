"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
class MyTopo( Topo ): 
    def build( self ):
        "Create custom topo."
        
        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )
        h7 = self.addHost( 'h7' )
        h8 = self.addHost( 'h8' )
        h9 = self.addHost( 'h9' )
        h10 = self.addHost( 'h10' )
        h11 = self.addHost( 'h11' )
        h12 = self.addHost( 'h12' )
       
        leftSwitch  = self.addSwitch( 's1' )
        rightSwitch = self.addSwitch( 's2' )
        lowerSwitch = self.addSwitch( 's3' )
        upperSwitch = self.addSwitch( 's4' )

        # Add links
        # Slice A
        self.addLink( h1, leftSwitch, bw=20)
        self.addLink( leftSwitch, rightSwitch, bw=20)
        self.addLink( rightSwitch, h2, bw=20)
        self.addLink( h3 , leftSwitch, bw=20)
        self.addLink( h4 , rightSwitch, bw=20)
        self.addLink( h5 , leftSwitch, bw=20)
        self.addLink( h6 , rightSwitch, bw=20)
        
        #Slice B
        self.addLink( h7, lowerSwitch,bw=10)
        self.addLink( lowerSwitch, upperSwitch, bw=10)
        self.addLink( upperSwitch, h8,bw=10)
        self.addLink (h9 , lowerSwitch, bw =10)
        self.addLink (h10 , upperSwitch,bw =10)
        self.addLink (h11 , lowerSwitch, bw =10)
        self.addLink (h12 , upperSwitch,bw =10)

topos = { 'mytopo': ( lambda: MyTopo() ) }

if __name__ == "__main__":
    topo = mytopo()
    net = Mininet(
     topo=topo,
     switch=OVSKernelSwitch,
     build=False,
     autoSetMacs=True,
     autoStaticArp=True,
     link=TCLink,
    )
    controller = RemoteController("c1", ip="127.0.0.1", port=6633)
    net.addController(controller)
    net.build()
    net.start()
    CLI(net)
    net.stop()