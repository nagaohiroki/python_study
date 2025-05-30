import werkzeug
import jsonrpc


@jsonrpc.dispatcher.add_method
def foobar(**kwargs: int | str) -> None:
    v = kwargs["foo"]
    k = kwargs["bar"]
    print(v, k)


@werkzeug.wrappers.Request.application
def application(request: werkzeug.wrappers.Request) -> werkzeug.wrappers.Response:
    response = jsonrpc.manager.JSONRPCResponseManager.handle(
        request.get_data(cache=False, as_text=True), jsonrpc.dispatcher
    )
    if response:
        return werkzeug.wrappers.Response(response.json, mimetype="application/json")
    return werkzeug.wrappers.Response(status=204, mimetype="application/json")


if __name__ == "__main__":
    werkzeug.serving.run_simple("localhost", 4000, application)
