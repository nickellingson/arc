import fastapi

# @app.get("/users/{id}")
# def get_user(id: int) -> User: ...
# vs 
# def get_user(id: int) -> User: ...
# app.add_api_route("/users/{id}", get_user, methods=["GET"])


# class FastAPI(Starlette):
#     def get(self, path: str, **opts):
#         def decorator(func):
#             self.add_api_route(path, func, methods=["GET"], **opts)
#             return func  # your function is returned unmodified
#         return decorator