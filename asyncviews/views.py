import asyncio
import time
import httpx
from django.http import HttpResponse

async def http_call_async():
    start = time.time()
    for num in range(1, 6):
        await asyncio.sleep(1)
        elapsed = time.time() - start
        print(f"[{elapsed:.1f}s] Contador: {num}")
    
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/get")
        print(f"Status da requisição: {r.status_code}")

async def async_view(request):
    asyncio.create_task(http_call_async())  # Executa em paralelo
    return HttpResponse("View assíncrona iniciada. Contador em segundo plano.")



# import asyncio
# from time import sleep
# import httpx
# from django.http import HttpResponse

# async def http_call_async():
#     for num in range(1, 6):
#         await asyncio.sleep(1)
#         print(num)
#     async with httpx.AsyncClient() as client:
#         r = await client.get("https://httpbin.org")
#         print(r)

# async def async_view(request):
#     loop = asyncio.get_event_loop()
#     loop.create_task(http_call_async())
#     return HttpResponse("Non-blocking HTTP request")
