import pygame
from auth import login, register

pygame.init()

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aeroblasters Login")

font = pygame.font.SysFont("Arial", 30)
small_font = pygame.font.SysFont("Arial", 22)

def login_menu():
    global screen

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Aeroblasters Login")

    username = ""
    password = ""

    active_field = "username"
    message = ""

    while True:

        screen.fill((20, 20, 50))

        title = font.render("Aeroblasters Login", True, (255, 255, 0))
        screen.blit(title, (150, 40))

        user_text = small_font.render(
            "Username: " + username,
            True,
            (255, 255, 255)
        )

        pass_text = small_font.render(
            "Password: " + "*" * len(password),
            True,
            (255, 255, 255)
        )

        screen.blit(user_text, (80, 130))
        screen.blit(pass_text, (80, 180))

        info = small_font.render(
            "TAB = Switch Field | ENTER = Login | R = Register",
            True,
            (200, 200, 200)
        )

        screen.blit(info, (30, 260))

        msg = small_font.render(message, True, (0, 255, 0))
        screen.blit(msg, (80, 320))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return None

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_TAB:

                    if active_field == "username":
                        active_field = "password"
                    else:
                        active_field = "username"

                elif event.key == pygame.K_BACKSPACE:

                    if active_field == "username":
                        username = username[:-1]
                    else:
                        password = password[:-1]

                elif event.key == pygame.K_RETURN:

                    if login(username, password):
                        return username
                    else:
                        message = "Invalid Username or Password"

                elif event.key == pygame.K_r:

                    if register(username, password):
                        message = "Registration Successful"
                    else:
                        message = "Username Already Exists"

                else:

                    if active_field == "username":
                        username += event.unicode
                    else:
                        password += event.unicode