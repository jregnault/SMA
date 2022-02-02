import configparser

config = configparser.ConfigParser()
config['simulation'] = {
    'delay': 0,
    'scheduling': "fair",
    'nb_ticks': 0,
    'trace': False,
    'seed': 0,
    'refresh': 1
}
config['view'] = {
    'box_size': 10,
    'grid': False
}
config['environment'] = {
    'torus': True,
    'grid_size_x': 100,
    'grid_size_y': 100
}
config['particles'] = {
    'nb_particles': 100,
}
config['wator'] = {
    'nb_fishes': 200,
    'nb_sharks': 10,
    'fishes_breed_time': 8,
    'sharks_breed_time': 19,
    'sharks_starve_time': 3
}
with open("config.ini", "w") as configfile:
    config.write(configfile)
