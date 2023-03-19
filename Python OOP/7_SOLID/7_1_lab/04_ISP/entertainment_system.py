class ElectricPower:
    def plug_in_power(self):
        pass


class RCAconnect:
    def connect_to_device_via_rca_cable(self, device):
        pass


class HDMIConnect:
    def connect_to_device_via_hdmi_cable(self, device):
        pass


class EthernetConnect:
    def connect_to_device_via_ethernet_cable(self, device):
        pass


class Television(HDMIConnect, ElectricPower, EthernetConnect):
    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)


class DVDPlayer(ElectricPower, RCAconnect):
    def connect_to_tv(self, tv):
        self.connect_to_device_via_rca_cable(tv)


class GameConsole(ElectricPower, EthernetConnect, HDMIConnect):

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def connect_to_tv(self, tv):
        self.connect_to_device_via_hdmi_cable(tv)


class Router(ElectricPower, EthernetConnect):

    def connect_to_tv(self, tv):
        self.connect_to_device_via_ethernet_cable(tv)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)




