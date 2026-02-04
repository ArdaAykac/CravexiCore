class network:
    @classmethod
    def create_server(
        cls,
        server_ip: str,
        port: int,
        max_player: int | None = ...,
        debug: bool = True
    ) -> None: ...
