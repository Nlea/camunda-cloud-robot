from dotenv import load_dotenv
import os
import asyncio

from pyzeebe import (
    ZeebeClient,
    create_camunda_cloud_channel
)

async def main():
    load_dotenv()
    my_client_id = os.environ.get('ZEEBE_CLIENT_ID')
    my_client_secret = os.environ.get('ZEEBE_CLIENT_SECRET')
    my_cluster_id = os.environ.get('ZEEBE_ADDRESS')
    
    grpc_channel = create_camunda_cloud_channel(
        client_id= my_client_id,
        client_secret=my_client_secret,
        cluster_id= my_cluster_id,
        region="bru-2",  # Default is bru-2
        )
        
    zeebe_client = ZeebeClient(grpc_channel)
    
    await zeebe_client.deploy_process('robot-process.bpmn')
    print('Process deployed')

asyncio.run(main())
