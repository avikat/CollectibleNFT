from brownie import accounts,config,SimpleCollectible,network
from scripts.simple_collectible.deploy_and_create import deploy_and_create

from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIROMENT, get_account,LOCAL_BLOCKCHAIN_ENVIROMENT
import pytest


def test_can_create_simple_collectible():
    if(network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENT):
        pytest.skip()

    simple_collectible = deploy_and_create()
    assert simple_collectible.ownerOf(0) == get_account()


    
    