import configparser

config = configparser.ConfigParser()
config['settings'] = {
    'torus':False,
    'gridSizeX':100,
    'gridSizeY':100,
    'canvasSizeX':1000,
    'canvasSizeY':1000,
    'boxSize':10,
    'delay':10,
    'scheduling':"fair",
    'nbTicks':0,
    'grid':True,
    'trace':True,
    'seed':0,
    'refresh':1,
    'nbParticles':100
}
with open("config.ini","w") as configfile:
    config.write(configfile)