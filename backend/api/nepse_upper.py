import asyncio
import httpx
from nepse import Client

async def main():

    # Initializes the client
    client = Client()

    # Gets the data
    data = await client.security_client.get_company(symbol="UPPER")

    # Prints the highest price for that company today
    print(data.high_price)

    # Closes the session
    await client.close()

# Run the function
loop = asyncio.get_event_loop()
loop.run_until_complete(main())