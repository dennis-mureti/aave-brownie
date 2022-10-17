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
    account = get_account
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])