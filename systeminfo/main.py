'''
Created on Feb 22, 2018

@author: Brynja
'''
import platform

def get_platfrom_info():
    print(platform.platform())
    return (platform.platform())


if __name__ == '__main__':
    get_platfrom_info()