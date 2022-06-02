from brownie import OurToken, network, config, accounts
from web3 import Web3


def deploy_token():

    account = accounts.add(config["wallets"]["from_key"])
    initial_supply = Web3.toWei(1000000, "ether")

    token = OurToken.deploy(
        initial_supply,
        {"from": account},
    )

    print(f"Contract has been deployed! {token.name()}")


def main():
    deploy_token()
