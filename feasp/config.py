METHOD: dict[str, str] = {
    "GET": "GET",
    "POST": "POST",
    "DELETE": "DELETE",
    "PUT": "PUT",
    "HEAD": "HEAD",
    "CONNECT": "CONNECT",
    "OPTIONS": "OPTIONS",
    "TRACE": "TRACE",
}


FEASP_ERROR: dict[str, tuple[str, str, int]] = {
    "HTTP_100": ("<h1>CONTINUE</h1>", "text/html", 101),
    "HTTP_101": ("<h1>SWITCHING PROTOCOLS</h1>", "text/html", 101),
    "HTTP_200": ("<h1>OK</h1>", "text/html", 200),
    "HTTP_201": ("<h1>CREATED</h1>", "text/html", 201),
    "HTTP_202": ("<h1>ACCEPTED</h1>", "text/html", 202),
    "HTTP_203": ("<h1>NON-AUTHORITATIVE INFORMATION</h1>", "text/html", 203),
    "HTTP_204": ("<h1>NO CONTENT</h1>", "text/html", 204),
    "HTTP_205": ("<h1>RESET CONTENT</h1>", "text/html", 205),
    "HTTP_206": ("<h1>PARTIAL CONTENT</h1>", "text/html", 206),
    "HTTP_300": ("<h1>MULTIPLE CHOICES</h1>", "text/html", 300),
    "HTTP_301": ("<h1>MOVED PERMANENTLY</h1>", "text/html", 301),
    "HTTP_302": ("<h1>FOUND</h1>", "text/html", 302),
    "HTTP_303": ("<h1>SEE OTHER</h1>", "text/html", 303),
    "HTTP_304": ("<h1>NOT MODIFIED</h1>", "text/html", 304),
    "HTTP_305": ("<h1>USE PROXY</h1>", "text/html", 305),
    "HTTP_306": ("<h1>RESERVED</h1>", "text/html", 306),
    "HTTP_307": ("<h1>TEMPORARY REDIRECT</h1>", "text/html", 307),
    "HTTP_400": ("<h1>BAD REQUEST</h1>", "text/html", 400),
    "HTTP_401": ("<h1>UNAUTHORIZED</h1>", "text/html", 401),
    "HTTP_402": ("<h1>PAYMENT REQUIRED</h1>", "text/html", 402),
    "HTTP_403": ("<h1>FORBIDDEN</h1>", "text/html", 403),
    "HTTP_404": ("<h1>NOT FOUND</h1>", "text/html", 404),
    "HTTP_405": ("<h1>METHOD NOT ALLOWED</h1>", "text/html", 405),
    "HTTP_406": ("<h1>NOT ACCEPTABLE</h1>", "text/html", 406),
    "HTTP_407": ("<h1>PROXY AUTHENTICATION REQUIRED</h1>", "text/html", 407),
    "HTTP_408": ("<h1>REQUEST TIMEOUT</h1>", "text/html", 408),
    "HTTP_409": ("<h1>CONFLICT</h1>", "text/html", 409),
    "HTTP_410": ("<h1>GONE</h1>", "text/html", 410),
    "HTTP_411": ("<h1>LENGTH REQUIRED</h1>", "text/html", 411),
    "HTTP_412": ("<h1>PRECONDITION FAILED</h1>", "text/html", 412),
    "HTTP_413": ("<h1>REQUEST ENTITY TOO LARGE</h1>", "text/html", 413),
    "HTTP_414": ("<h1>REQUEST-URI TOO LONG</h1>", "text/html", 414),
    "HTTP_415": ("<h1>UNSUPPORTED MEDIA TYPE</h1>", "text/html", 415),
    "HTTP_416": ("<h1>REQUESTED RANGE NOT SATISFIABLE</h1>", "text/html", 416),
    "HTTP_417": ("<h1>EXPECTATION FAILED</h1>", "text/html", 417),
    "HTTP_500": ("<h1>INTERNAL SERVER ERROR</h1>", "text/html", 500),
    "HTTP_501": ("<h1>NOT IMPLEMENTED</h1>", "text/html", 501),
    "HTTP_502": ("<h1>BAD GATEWAY</h1>", "text/html", 502),
    "HTTP_503": ("<h1>SERVICE UNAVAILABLE</h1>", "text/html", 503),
    "HTTP_504": ("<h1>GATEWAY TIMEOUT</h1>", "text/html", 504),
    "HTTP_505": ("<h1>HTTP VERSION NOT SUPPORTED</h1>", "text/html", 505),
}


class FeaspNotFound(Exception):
    pass
