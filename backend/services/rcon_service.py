from mcrcon import MCRcon

class RconService:
    def __init__(self, host: str, port: int, password: str):
        self.host = host
        self.port = port
        self.password = password

    def execute(self, command: str) -> str:
        with MCRcon(self.host,self.password,port=self.port) as mcr:
            return mcr.command(command)
