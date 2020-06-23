from visual.stage import Stage
from neuralnetwork.network import Network
from random import randint

def main():
    '''stage = Stage()
    stage.set_window(960, 540)
    stage.set_font('fonts/Courier Prime Code.ttf', 24)
    stage.set_framerate(30)
    stage.add_sim()
    stage.start()'''
    networks = [Network(4, 3) for _ in range(200)]
    for network in networks:
        for _ in range(100):
            a = randint(0, 2)
            if a == 0:
                network.add_edge()
            elif a == 1:
                network.add_node()
            elif a == 2:
                network.change_edge()
    print(networks[0])


if __name__ == '__main__':
    main()
