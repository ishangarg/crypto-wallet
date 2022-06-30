from .base import BaseAsset
from web3 import Web3


class Ethereum(BaseAsset):

    '''Base class for Ethereum'''

    w3 = None

    def __init__(self, rpc_url):
        super().__init__('Ethereum', 'ETH')
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))

    def create_wallet(self) -> None:
        
        pass