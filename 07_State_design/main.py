from without_design import TransportMode, TransportService
from with_design import TransportServive, Bike, Train

# ts=TransportService(TransportMode.WALKING)
# ts.eta()
# ts.directions()

bike=Bike()
train=Train()

td=TransportServive(bike)
td.eta()
td.directions()

td.setMode(train)
td.eta()
td.directions()