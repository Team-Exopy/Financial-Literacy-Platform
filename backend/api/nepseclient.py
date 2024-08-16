import asyncio
import httpx
from nepse import Client


async def main():
    company_Symbol = input('Input Company Symbol (Uppercase): ')

    # Doing this is optional you can directly
    # Initialize using `client = Client()` as well
    async with httpx.AsyncClient() as async_client:
        # Initializes the client
        client = Client(httpx_client=async_client)

        # Gets the data
        data = await client.security_client.get_company(symbol=f"{company_Symbol}")

        # Prints the highest price for that company today
        print(f'High Price of {company_Symbol}: ', data.high_price)
        print(f'Low price of {company_Symbol}: ', data.low_price)
        print(f'Open Price of {company_Symbol}: ', data.open_price)

# Run the function
loop = asyncio.get_event_loop()
loop.run_until_complete(main())