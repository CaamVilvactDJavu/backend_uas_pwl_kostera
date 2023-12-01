from pyramid.view import view_config, view_defaults
from pyramid.response import Response
from client.grpc.kostClient import KostClient


@view_defaults(route_name="kost", renderer="json")
class KostView:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def get(self):
        try:
            kostClient = KostClient()

            kostId = self.request.GET.get("kostId")

            if kostId:
                result = kostClient.get_kost(id=int(kostId))

                if result is None:
                    return Response(
                        json_body={"error": {"message": "Not found"}}, status=404
                    )

            else:
                result = kostClient.get_kosts()

            return result

        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(request_method="POST")
    def post(self):
        if self.request.json_body.get("name") == None:
            return Response(
                json_body={"error": {"message": "Name is required"}}, status=400
            )
        try:
            kostClient = KostClient()
            result = kostClient.create_kost(
                name=self.request.json_body.get("name"),
                price=self.request.json_body.get("price") or 10000,
                rating=self.request.json_body.get("rating") or 1,
                gender=self.request.json_body.get("gender") or "No gender",
                specification=self.request.json_body.get("specification")
                or "No specification",
                rule=self.request.json_body.get("rule") or "No rule",
                address=self.request.json_body.get("address") or "No address",
                facility=self.request.json_body.get("facility") or "No facility",
                image_url=self.request.json_body.get("image_url") or "No image_url",
            )
            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(request_method="PUT")
    def put(self):
        if self.request.json_body.get("id") == None:
            return Response(
                json_body={"error": {"message": "id is required"}}, status=400
            )

        try:
            kostClient = KostClient()

            selected_kost = kostClient.get_kost(id=self.request.json_body.get("id"))

            if selected_kost is None:
                return Response(
                    json_body={"error": {"message": "Not found"}}, status=404
                )

            result = kostClient.update_kost(
                id=self.request.json_body.get("id"),
                name=self.request.json_body.get("name"),
                gender=self.request.json_body.get("gender") or "No gender",
                price=self.request.json_body.get("price") or 10000,
                rating=self.request.json_body.get("rating") or 1,
                specification=self.request.json_body.get("specification")
                or "No specification",
                rule=self.request.json_body.get("rule") or "No rule",
                address=self.request.json_body.get("address") or "No address",
                facility=self.request.json_body.get("facility") or "No facility",
                image_url=self.request.json_body.get("image_url") or "No image_url",
            )
            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(request_method="DELETE")
    def delete(self):
        if self.request.json_body.get("id") == None:
            return Response(
                json_body={"error": {"message": "id is required"}}, status=400
            )

        try:
            kostClient = KostClient()

            selected_kost = kostClient.get_kost(id=self.request.json_body.get("id"))

            if selected_kost is None:
                return Response(
                    json_body={"error": {"message": "Not found"}}, status=404
                )

            result = kostClient.delete_kost(id=self.request.json_body.get("id"))
            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)
