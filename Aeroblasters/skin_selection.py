import pygame
from auth import update_skin


def skin_selection_screen(win, current_user):
    """
    Displays the skin selection screen.
    Returns the selected skin name.
    """

    # List of available skins
    skins = ["default", "inferno", "arctic", "golden"]
    aircraft_names = {
        "default": "Falcon Mk-I",
        "inferno": "Inferno X",
        "arctic": "Arctic Hawk",
        "golden": "Golden Eagle"
        }

    # Current selected skin
    selected_index = 0
    equipped_skin = current_user and "default"

    # Screen size
    WIDTH, HEIGHT = win.get_size()

    # Fonts
    title_font = pygame.font.SysFont("Arial", 36, bold=True)
    text_font = pygame.font.SysFont("Arial", 24)
    # Preview images
    preview_images = {}

    for skin in skins:
        img = pygame.image.load(f"Assets/Skins/{skin}_1.png")
        img = pygame.transform.scale(img, (180, 155))
        preview_images[skin] = img

    running = True

    while running:

        # Background
        win.fill((20, 20, 35))

        # Title
        welcome_font = pygame.font.SysFont("Arial", 22)
        welcome_text = welcome_font.render(
            f"Welcome, {current_user}",
            True,
            (0, 255, 255)
        )
        title = title_font.render("AIRCRAFT HANGAR", True, (255, 255, 255))
        win.blit(
            welcome_text,
            (WIDTH//2 - welcome_text.get_width()//2, 8)
        )
        win.blit(title, (WIDTH//2 - title.get_width()//2, 45))
        # Current skin
        current_skin = skins[selected_index]

        # Aircraft preview
        preview = preview_images[current_skin]

        preview_rect = preview.get_rect(center=(WIDTH//2, HEIGHT//2 - 30))
        win.blit(preview, preview_rect)

        # Skin name
        skin_text = text_font.render(
            aircraft_names[current_skin],
            True,
            (255, 255, 0)
        )
        win.blit(
            skin_text,
            (WIDTH//2 - skin_text.get_width()//2,
            preview_rect.bottom + 30)
        )
        status_font = pygame.font.SysFont("Arial", 20, bold=True)

        if current_skin == equipped_skin:
            status_text = status_font.render(
                "✔ EQUIPPED",
                True,
                (0, 255, 0)
            )
        else:
            status_text = status_font.render(
                "Press SPACE to Equip",
                True,
                (255, 255, 255)
            )

        win.blit(
            status_text,
            (
                WIDTH//2 - status_text.get_width()//2,
                preview_rect.bottom + 75
            )
        )
       # Navigation Instructions
        instruction = text_font.render(
            "◄ Previous Skin      Next Skin ►",
            True,
            (200, 200, 200)
        )

        win.blit(
            instruction,
            (
                WIDTH//2 - instruction.get_width()//2,
                preview_rect.bottom + 125
            )
        )

       # Bottom instruction
        bottom_text = text_font.render(
            "ENTER = Start Mission",
            True,
            (0, 255, 0)
        )

        win.blit(
            bottom_text,
            (
                WIDTH//2 - bottom_text.get_width()//2,
                preview_rect.bottom + 170
            )
        )
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                # Previous skin
                if event.key == pygame.K_LEFT:
                    selected_index = (selected_index - 1) % len(skins)

                # Next skin
                elif event.key == pygame.K_RIGHT:
                    selected_index = (selected_index + 1) % len(skins)
                    
                # Equip aircraft
                elif event.key == pygame.K_SPACE:
                    selected_skin = skins[selected_index]
                    update_skin(current_user, selected_skin)
                    equipped_skin = selected_skin

                # Start Mission
                elif event.key == pygame.K_RETURN:
                    return equipped_skin

               