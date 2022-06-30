from web3 import Web3
import time


# print(str(w3.eth.get_block('latest')))

# new_transaction_filter = w3.eth.filter('pending')
# print(new_transaction_filter.get_new_entries())

def handle_event(event, w3):
    print(event)
    block_hash = Web3.toJSON(event)
    print(block_hash)
    # print(w3.eth.get_block('latest'))
    # print(w3.eth.get_block(block_hash))

def log_loop(event_filter, poll_interval, w3):
    while True:
        # for event in event_filter.get_new_entries():
        #     handle_event(event, w3)
        latest_blocks = w3.eth.getFilterChanges(event_filter.filter_id)
        print(latest_blocks)
        time.sleep(poll_interval)

def main(w3):
    block_filter = w3.eth.filter('latest')
    log_loop(block_filter, 2, w3)

if __name__ == '__main__':

    w3 = Web3(Web3.HTTPProvider('https://nd-105-344-848.p2pify.com/ce28add8fa5b092ffa58be757febd7d6'))

    USDT_CONTRACT = '0xdAC17F958D2ee523a2206206994597C13D831ec7'

    new_acct = w3.eth.account.create()

    print(str(w3.isConnected()))

    print(str(new_acct.address))
    main(w3)
