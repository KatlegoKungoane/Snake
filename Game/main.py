# Example file showing a circle moving on screen
import pygame as pg
import Helpers.constants as const

def main():
    pg.init()
    screen = pg.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
    running = True

    while running:
        running = controlPolling()
        controlKeyEvents()

        screen.fill(const.GREY)
        controlRender(screen=screen)
        pg.display.flip()

        # deltaTime = clock.tick(const.FPS) / 1000

    pg.quit()


def controlPolling():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
    return True


def controlKeyEvents():
    t = 1
    # clock = pg.time.Clock()
    # deltaTime = 0
    # keys = pg.key.get_pressed()
    # if keys[pg.K_w]:
    #     player_pos.y -= 300 * deltaTime
    # if keys[pg.K_s]:
    #     player_pos.y += 300 * deltaTime
    # if keys[pg.K_a]:
    #     player_pos.x -= 300 * deltaTime
    # if keys[pg.K_d]:
    #     player_pos.x += 300 * deltaTime


def controlRender(screen: pg.Surface):
    blockWidth = const.SCREEN_WIDTH / 10
    blockHeight = const.SCREEN_HEIGHT / 10

    for i in range(10):
        pg.draw.rect(screen, const.BLACK, (-0.5, i * blockHeight - 0.5, const.SCREEN_WIDTH, 1))
        pg.draw.rect(screen, const.BLACK, (i * blockWidth - 0.5, -0.5, 1, const.SCREEN_HEIGHT))


if __name__ == "__main__":
    main()