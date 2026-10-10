from with_pattern import ControlTower, Airplane

ct=ControlTower()
indigo=Airplane("indigo-101",ct)
spicejet=Airplane("spicejet-101",ct)
airindia=Airplane("airindia-101",ct)

indigo.send_message("landing please")