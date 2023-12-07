import os
import sys
import asyncio as asyncio
import json

class NoteTopic:
    def __init__(self):
        self.queue = asyncio.Queue()
        # This queue will be used to store the messages (either text or serialized JSON) asynchronously.
    async def put(self, obj):
        """
        The put method is an async method that takes one argument obj. It then checks the type of obj and:
            If obj is a string (str), it puts the string directly onto the asynchronous queue with await self.queue.put(obj).
            If obj is a dictionary (dict), it serializes the dictionary to a JSON string with json.dumps(obj) and puts it onto the queue with await self.queue.put(json.dumps(obj)).
            If obj is neither of these types, it raises a TypeError exception, indicating that the NoteTopic class only accepts objects of type str or dict.
        :param obj:
        :return:
        """
        if isinstance(obj, str):
            await self.queue.put(obj)
        elif isinstance(obj, dict):
            await self.queue.put(json.dumps(obj))
        else:
            raise TypeError("NoteTopic only accepts str or dict objects")

    async def get(self):
        """
        The get method is an async method that retrieves a message from the queue. It simply calls await
            self.queue.get(), which will wait until a message is available if the queue is empty or immediately return
            a message if the queue has items.
        :return:
        """
        return await self.queue.get()