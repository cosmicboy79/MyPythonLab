"""
Source: https://www.geeksforgeeks.org/python/await-in-python/
"""
import asyncio
from asynchronous.runner.task.myasynctask import custom_async_task
from asynchronous.runner.operation.myoperations import first_operation, second_operation

# runs two runner sequentially, waiting for one to finish before starting the next
async def running_sequentially():
    await custom_async_task(first_operation, 3)
    await custom_async_task(second_operation, 2)

# executes both runner, totaling around 5 seconds of runtime
def main():
    asyncio.run(running_sequentially())
