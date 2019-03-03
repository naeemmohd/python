# create a makeCaps function - create a file myCaps.py using - nano myCaps.py or %%writefile myCaps.py in Jupyter
from string import capwords
def makeCaps(word):
    return capwords(word.title())
