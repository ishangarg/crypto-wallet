class BaseAsset():
    '''
    BaseAsset class is the skeleton for L1 asset such as Bitcoin, Ethereum, Tron, Solana etc. Each BaseAsset has their own Dedicated node 
    and has common methods avialable for all balace
    '''
    NAME = None
    TICKER = None

    def __init__(self, name, ticker):
        self.NAME = name
        self.TICKER = ticker

    def create_wallet(self) -> None:
        '''
        Creates a new wallet & private key.
        '''
        pass
        
    def get_balance(self, address:str) -> float:
        '''
        Gets the balance of the address corresponding to the asset class
        
        returns -> float
        '''
        pass

    def transfer(self, address:str, amount:float) -> bool:
        '''
        Lower level method to transfer the asset to a particular adderss. Checks should be done 
        before calling this method. 
        
        returns -> bool
        '''
        pass

    def listen_forever(self, address:str) -> None:
        '''
        Opens the socket, and starts listening for state changes. Notifies the supplied socket with Blockchain state changes
        '''
        pass

