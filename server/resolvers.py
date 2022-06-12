import asyncio
import json

from tartiflette import Resolver, Subscription

feed = []

queue = asyncio.Queue()


@Resolver("Query.feed")
async def feed_resolver(parent, args, ctx, info):
    return feed


@Resolver("Mutation.postLink")
async def post_link_resolver(parent, args, ctx, info):
    iid = len(feed)
    url = args["url"]
    description = args["description"]
    link = {"id": iid, "url": url, "description": description}
    feed.append(link)

    await queue.put(link)

    return link


@Subscription("Subscription.newLink")
async def new_link_subscription(parent, args, ctx, info):
    while True:
        print("Waiting for new link...")
        yield await queue.get()
        print("New link received: ")
