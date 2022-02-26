from brownie import accounts,config,SimpleCollectible
from scripts.helpful_scripts import get_account,OPENSEA_URL

sample_token_uri = "https://ipfs.io/ipfs/QmXB8iyKn6L4agHJLfKLfJmMPEwPexTHio98RDKDEMfxUZ?filename=WhatsApp%20Image%202022-02-20%20at%2011.49.06%20AM.jpeg"



def deploy_and_create():
    account=get_account()
    simple_collectible = SimpleCollectible.deploy({"from":account})
    tx = simple_collectible.createCollectible(sample_token_uri,{"from":account})
    tx.wait(1)
    print(f"Awesome, you can view you NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter()-1)}" ) 
    print("Please wait up to 20 minutes, and hit the refreash metadata button.")
    return simple_collectible
def main():
    deploy_and_create()

