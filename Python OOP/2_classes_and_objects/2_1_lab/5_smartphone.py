class Smartphone:

    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self) -> None:
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: int) -> str:

        if app_memory <= self.memory:

            if self.is_on:

                self.memory -= app_memory
                self.apps.append(app)

                return f"Installing {app}"

            return f"Turn on your phone to install {app}"

        return f"Not enough memory to install {app}"

    def status(self) -> str:

        apps_count = len(self.apps)
        memory_left = self.memory

        return f"Total apps: {apps_count}. Memory left: {memory_left}"

smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())


