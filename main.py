from visual.stage import Stage

def main():
    stage = Stage()
    stage.set_window(640, 360)
    stage.set_framerate(60)
    stage.start()

if __name__ == '__main__':
    main()
