from brownie import (
    accounts,
    network,
    config
)

FORKED_LOCAL_ENVIRONEMNETS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local", "ganache", "hardhat", "local-ganache", "mainnet-fork"]

def get_account(index=None, id=None):
    # accounts[0]
    # accounts.add("env")
    # accounts.load("id")
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONEMNETS
    ):
        return accounts[0]

    return accounts.add(
        config["wallets"]["from_key"]
    )  # will now be our default making it more liberal