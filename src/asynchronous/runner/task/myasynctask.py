import asyncio


async def custom_async_task(func, sleep_time):
    """
    Custom asynchronous task (coroutine)
    :param func: operation to execute
    :param sleep_time: sleep time
    """
    print(f"Execution of {func.__name__} started")
    func()
    await asyncio.sleep(sleep_time)
    print(f"Execution of {func.__name__} completed")
