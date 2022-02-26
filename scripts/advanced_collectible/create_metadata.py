from brownie import AdvancedCollectible,network
from scripts.helpful_scripts import get_account,get_breed
from metadata.sample_metdata import metadata_template
from pathlib import Path
import json
import requests

def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"You have created {number_of_advanced_collectibles} collectibles!")

    for token_id in range(number_of_advanced_collectibles) : 
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadat_file_name = f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        collectible_metadata = metadata_template
        if Path(metadat_file_name).exists():
            print(f"{metadat_file_name} already exists! Delete it to overwrite")

        else:
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = f"An adorable {breed} pup!"
            image_file_path ="./img/" +  breed.lower().replace("_","-") + ".png"
            image_uri= upload_to_ipfs(image_file_path)
            collectible_metadata["image"] = image_uri
            with open (metadat_file_name,"w") as file:
                json.dump(collectible_metadata,file)
            upload_to_ipfs(metadat_file_name)
            



def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file":image_binary})

        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
        


    