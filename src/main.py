from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "World")
    text = "Hello, " + name
    return web.Response(text=text)

async def main():
    app = web.Application()
    app.add_routes([web.get('/', handle),
                      web.get('/{name}', handle)])
    return app

if __name__ == '__main__':
    app = web.run_app(main())