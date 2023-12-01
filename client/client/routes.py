def includeme(config):
    config.add_route("home", "/")
    config.add_route("kost", "/api/v1/kost/")
    config.add_route("auth", "/api/v1/auth/")
    config.add_route("register", "/api/v1/auth/register")
    config.add_route("login", "/api/v1/auth/login")
    config.add_route("verify", "/api/v1/auth/verify")
