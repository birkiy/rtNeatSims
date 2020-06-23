from visual.stage import Stage

def main():
    stage = Stage()
    stage.set_window(960, 540)
    stage.set_font('fonts/Courier Prime Code.ttf', 24)
    stage.set_framerate(30)
    stage.add_sim()
    stage.start()

if __name__ == '__main__':
    main()
