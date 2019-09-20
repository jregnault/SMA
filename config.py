import configparser

config = configparser.ConfigParser()
config['simulation'] = {
    'delay':10,
    'scheduling':"fair",
    'nbTicks':0,
    'trace':True,
    'seed':0,
    'nbParticles':100,
    'refresh':1
}
config['view'] = {
    'canvasSizeX':1000,
    'canvasSizeY':1000,
    'boxSize':10,
    'grid':True
}
config['env'] = {
    'torus':False,
    'gridSizeX':100,
    'gridSizeY':100
}
with open("config.ini","w") as configfile:
    config.write(configfile)