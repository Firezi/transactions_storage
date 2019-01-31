from __future__ import absolute_import, unicode_literals
from tr_storage.celery import app

from web3 import Web3, HTTPProvider
from tr_storage import settings

from api.models import Transaction, AppInfo

web3 = Web3(HTTPProvider(settings.INFURA_ENDPOINT))

account_address = settings.ACCOUNT_ADDRESS.lower()
confirmation_block_count = settings.CONFIRMATION_BLOCK_COUNT


@app.task()
def poll_blocks():
    last_block_number = web3.eth.blockNumber

    app_info = AppInfo.objects.get()
    last_polled_block_number = app_info.last_polled_block_number

    app_info.last_polled_block_number = last_block_number - confirmation_block_count
    app_info.save()

    for block_number in range(last_polled_block_number + 1, last_block_number - confirmation_block_count + 1):
        print("Block %s polling..." % block_number)
        trs_count = web3.eth.getBlockTransactionCount(block_number)

        for i in range(0, trs_count):
            poll_transaction.delay(block_number, i)


@app.task()
def poll_transaction(block_number, index):
    tr = web3.eth.getTransactionByBlock(block_number, index)

    if tr['from'] and tr['to']:
        if tr['from'].lower() == account_address or tr['to'].lower() == account_address:
            print("Transaction found in %d - %d" % (block_number, index))

            timestamp = web3.eth.getBlock(block_number)['timestamp']

            new_transaction = Transaction.objects.create(hash=tr['hash'].hex(), block_number=tr['blockNumber'], from_address=tr['from'],
                                                         to_address=tr['to'], quantity=str(tr['value']), timestamp=timestamp,
                                                         input_data=tr['input'])
            new_transaction.save()
