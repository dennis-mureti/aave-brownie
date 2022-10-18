from scripts.helpful_scripts import get_account
from brownie import interface, network, config

def main():
    get_weth()

def get_weth():
    """
    Mints WETH by depositing ETH.
    """
    # ABI
    # address
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    # now we call the deposit function
    tx = weth.deposit({"from": account, "value": 0.1 * 10 ** 18})
    tx.wait(1)
    print("Received 0.1 WETH")
    return tx