import logging
from algosdk import mnemonic
import algokit_utils
from algopy import String
from algosdk.v2client import algod, indexer
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient

logger = logging.getLogger(__name__)

ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"
INDEXER_ADDRESS = "https://testnet-idx.algonode.cloud"

def deploy(
    algod_client: algod.AlgodClient,
    indexer_client: indexer.IndexerClient,
    app_spec: algokit_utils.ApplicationSpecification,
    deployer: algokit_utils.Account,
) -> None:
    from smart_contracts.artifacts.hello_world.hello_world_client import (
        HelloWorldClient,
    )

    algod_client = algod.AlgodClient(algod_token="", algod_address=ALGOD_ADDRESS)
    indexer_client = indexer.IndexerClient(indexer_token="", indexer_address=INDEXER_ADDRESS)

    private_key = ""
    deployer_address = "B2A6OPKPNFHI6EM27RIFCVCU53VYDL7NOD5HRTHVOMAKOXMZ7Q2PSO2KMI"
    deployer = algokit_utils.Account(private_key=private_key, address=deployer_address)

    app_client = HelloWorldClient(
        algod_client=algod_client,
        creator=deployer,
        indexer_client=indexer_client,
        app_id=0,
    )

    app_client.deploy(
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
        on_update=algokit_utils.OnUpdate.AppendApp,
    )
    name = "Simone"
    response = app_client.hello(name=name, transaction_parameters=algokit_utils.TransactionParameters(
            boxes=[(app_client.app_id, "Greeting")]
        ))
    logger.info(
        f"Called hello on {app_spec.contract.name} ({app_client.app_id}) "
        f"with name={name}, received: {response.return_value}"
    )
