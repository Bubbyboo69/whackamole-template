#writing a program for whackamole
import pygame
import random


def main():
    try:
        pygame.init()

        mole_image = pygame.image.load("mole.png")

        screen = pygame.display.set_mode((640, 512))
        pygame.display.set_caption("Whack-a-Mole")

        grid_width = 20
        grid_height = 16
        cell_size = 32

        # Initializes moles potition at (0,0)
        mole_x = 0
        mole_y = 0

        #Controls frame rate
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Checks if mole's clicked
                    mouse_x, mouse_y = event.pos
                    if mole_x <= mouse_x < mole_x + cell_size and mole_y <= mouse_y < mole_y + cell_size:
                        # Moves mole randomly on grid
                        mole_x = random.randrange(0, grid_width) * cell_size
                        mole_y = random.randrange(0, grid_height) * cell_size

            screen.fill("lightgreen")

            x = 0
            while x < screen.get_width():
                pygame.draw.line(screen, "black", (x, 0), (x, screen.get_height()))
                x += cell_size

            y = 0
            while y < screen.get_height():
                pygame.draw.line(screen, "black", (0, y), (screen.get_width(), y))
                y += cell_size

            screen.blit(mole_image, (mole_x, mole_y))

            pygame.display.flip()

            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
