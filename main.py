# Student ID: [001352245] - WGUPS Routing Program
""""
Entry point for the WGUPS Routing Program.
Creates the delivery routing service and launches the user interface.
The service handles all routing logic; the UI handles all user interaction.
"""

from DeliveryRoutingService import DeliveryRoutingService
from WGUPSUserInterface import WGUPSUserInterface

service = DeliveryRoutingService()
ui = WGUPSUserInterface(service)

ui.user_interface()
