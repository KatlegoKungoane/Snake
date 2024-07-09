# Example file showing a circle moving on screen
import pygame as pg
import numpy as np
from Helpers import constants as const
from snake import Snake

def main():
    pg.init()
    screen: pg.display = pg.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
    running: bool = True

    snakes: list[Snake] = [
        Snake(bodyPoints=np.array([
            [0, 0],
            [4, 0],
        ])),
        Snake(bodyPoints=np.array([
            [3, 5],
            [3, 4],
            [2, 4],
            [2, 2],
        ])),
        Snake(bodyPoints=np.array([
            [9, 6],
            [9, 7],
            [8, 7],
            [8, 6],
            [7, 6],
        ])),
        Snake(bodyPoints=np.array([
            [8, 8],
            [8, 9],
            [5, 9]
        ]))
    ]

    while running:
        running = controlPolling()
        controlKeyEvents()

        screen.fill(const.GREY)
        controlRender(screen=screen)
        drawSnakesOnBoard(screen=screen, snakes=snakes);
        pg.display.flip()

        # deltaTime = clock.tick(const.FPS) / 1000

    pg.quit()


def controlPolling() -> bool: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
    return True


def controlKeyEvents() -> None:
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


def controlRender(screen: pg.Surface) -> None:
    for i in range(const.NO_TILES):
        pg.draw.rect(screen, const.BLACK, (-0.5, i * const.BLOCK_HEIGHT - 0.5, const.SCREEN_WIDTH, 1))
        pg.draw.rect(screen, const.BLACK, (i * const.BLOCK_WIDTH - 0.5, -0.5, 1, const.SCREEN_HEIGHT))


def drawSnakesOnBoard(
    screen: pg.surface, 
    snakes: list[Snake]
) -> None:
    for snake in snakes:
        for (index, point) in enumerate(snake.bodyPoints):
            if index != 0:
                drawLine(
                    screen=screen, 
                    start=point,
                    end=snake.bodyPoints[index - 1],
                    color=snake.color
                )
        
        drawEye(
            screen=screen, 
            point=snake.bodyPoints[0]
        )

        drawTail(
            screen=screen, 
            point=snake.bodyPoints[-1]
        )

def drawLine(
    screen: pg.surface, 
    start: np.ndarray, 
    end: np.ndarray, 
    color: pg.Color = const.BLACK
) -> None:
    width = (abs(end[1] - start[1]) + 1) * const.BLOCK_WIDTH
    length = (abs(end[0] - start[0]) + 1) * const.BLOCK_HEIGHT
    pg.draw.rect(
        screen, 
        color, 
        (
            min(start[1], end[1]) * const.BLOCK_WIDTH, 
            min(start[0], end[0]) * const.BLOCK_HEIGHT, 
            width, 
            length
        )
    )

def drawEye(
    screen: pg.surface, 
    point: np.ndarray, 
    color: pg.Color = const.WHITE
):
    pg.draw.circle(
        screen, 
        color, 
        ((point[1] + 0.5) * const.BLOCK_WIDTH, (point[0] + 0.25) * const.BLOCK_HEIGHT),
        min(const.BLOCK_HEIGHT, const.BLOCK_WIDTH) / 5
)   
    
def drawTail(
    screen: pg.surface, 
    point: np.ndarray, 
    color: pg.Color = const.WHITE
) -> None:
    pg.draw.rect(
        screen, 
        color, 
        (
            (point[1] + 0.40) * const.BLOCK_WIDTH, 
            (point[0] + 0.40) * const.BLOCK_HEIGHT, 
            const.BLOCK_WIDTH * 0.2, 
            const.BLOCK_HEIGHT * 0.2
        )
    )


if __name__ == "__main__":
    main()