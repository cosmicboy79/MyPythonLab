"""
Source: https://www.geeksforgeeks.org/python/await-in-python/
"""
import asyncio
from asynchronous.runner.task.myasynctask import custom_async_task
from asynchronous.runner.operation.myoperations import first_operation, second_operation


# this coroutine runs both runner concurrently with asyncio.gather()
async def running_concurrently():
    await asyncio.gather(custom_async_task(first_operation, 3),
                         custom_async_task(second_operation, 2))


# starts the event loop, running and waiting for both runner to complete
def main():
    asyncio.run(running_concurrently())
