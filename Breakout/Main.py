# Import all the necessary libraries and initialize pygame engine
import ObjectProperties
from Button import button
from Ball import Ball
from Pedal import pedal
from Brick import Brick
import UnitTest
import random
import pygame
pygame.init()

# This will be a list that will contain all the sprites we intend to use in our game
all_sprites_list = pygame.sprite.Group()
all_sprites_list_intro = pygame.sprite.Group()

# This is a database unit test
SQLtest = UnitTest.UnitTest()
SQLtest.db_test()

# create and position our paddle
player1Pedal = pedal(ObjectProperties.GREEN, 100, 10)
player1Pedal.rect.x = 350
player1Pedal.rect.y = 550

# create and position our Ball
ball1 = Ball(ObjectProperties.WHITE, 10, 10)
ball1.rect.x = 345
ball1.rect.y = 195


# Create a group for all the bricks
all_bricks = pygame.sprite.Group()

# Create the bricks
for i in range(7):
    brick = Brick(ObjectProperties.RED, 80, 30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(ObjectProperties.ORANGE, 80, 30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(ObjectProperties.YELLOW, 80, 30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

# Add the paddle to the list of sprites
all_sprites_list.add(player1Pedal)

# Add the ball to the list of sprites
all_sprites_list.add(ball1)

# Create three buttons
button_del_user = button(ObjectProperties.GRAY, 70, 20)
button_del_user.rect.x = 200
button_del_user.rect.y = 10
button_quit = button(ObjectProperties.GRAY, 70, 20)
button_quit.rect.x = 500
button_quit.rect.y = 10
button_scoreboard = button(ObjectProperties.GRAY, 70, 20)
button_scoreboard.rect.x = 350
button_scoreboard.rect.y = 10
all_sprites_list.add([button_scoreboard, button_quit, button_del_user])

# Create intro name box
username_box = button(ObjectProperties.WHITE, 320, 80)
username_box.rect.x = 250
username_box.rect.y = 300
all_sprites_list_intro.add(username_box)


# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

# The loop will carry on until the user exit the game
carryOn = True

# Has the user clicked the box?
click_box = False

# The clock is used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Intro screen -----------
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False

    # Clear the screen to dark blue.
    screen.fill(ObjectProperties.DARKBLUE)

    font = pygame.font.Font(None, 40)
    text = font.render("Enter your name:", 1, ObjectProperties.BLACK)
    screen.blit(text, (290, 240))

    # Detects if the mouse is clicking the box
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 250 + 320 > mouse[0] > 250 and 300 + 80 > mouse[1] > 300 and click[0] != 0:
        pygame.draw.line(screen, ObjectProperties.WHITE, [0, 38], [800, 38], 2)

        ObjectProperties.score += 1
        print(ObjectProperties.score)

    all_sprites_list_intro.draw(screen)

    # Update the screen
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)


carryOn = True
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            while True:  # Infinite loop that will be broken when the user press the space bar again
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    break  # Exit infinite loop

        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False

    # Clear the screen to dark blue.
    screen.fill(ObjectProperties.DARKBLUE)

    # Detects if the mouse is clicking the buttons
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 200 + 70 > mouse[0] > 200 and 10 + 20 > mouse[1] > 10 and click[0] != 0:
        ObjectProperties.score += 1
    if 350 + 70 > mouse[0] > 350 and 10 + 20 > mouse[1] > 10 and click[0] != 0:
        ObjectProperties.score += 1
    if 500 + 70 > mouse[0] > 500 and 10 + 20 > mouse[1] > 10 and click[0] != 0:
        ObjectProperties.score += 1




    # Display the score and number of lives at the top of the screen
    pygame.draw.line(screen, ObjectProperties.WHITE, [0, 38], [800, 38], 2)
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(ObjectProperties.score), 1, ObjectProperties.WHITE)
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(ObjectProperties.lives), 1, ObjectProperties.WHITE)
    screen.blit(text, (650, 10))


    # Moving the paddle when the user presses the arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1Pedal.moveleft(5)
    if keys[pygame.K_RIGHT]:
        player1Pedal.moveright(5)

    # Updates the balls position
    all_sprites_list.update()

    # Check if the ball is bouncing against any of the 4 walls:
    if ball1.rect.x >= 790:
        ball1.velocity[0] = -ball1.velocity[0]
    if ball1.rect.x <= 0:
        ball1.velocity[0] = -ball1.velocity[0]
    if ball1.rect.y > 590:
        ball1.velocity[1] = -ball1.velocity[1]
        # Make the player loose lives if the ball hits the bottom of the screen
        ObjectProperties.lives -= 1
        # The player looses the game if lives = 0
        if ObjectProperties.lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, ObjectProperties.WHITE)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)
            carryOn = False
    if ball1.rect.y < 40:
        ball1.velocity[1] = -ball1.velocity[1]

    # Check if the ball only moves horizontally
    if ball1.velocity[1] == 0:
        ball1.velocity[1] = random.randint(1,5)

    # Detect collisions between the ball and the paddle
    if pygame.sprite.collide_mask(ball1, player1Pedal):
        ball1.rect.x -= ball1.velocity[0]
        ball1.rect.y -= ball1.velocity[1]
        ball1.bounce()

    # Check if there is a collision between ball and brick
    brick_collision_list = pygame.sprite.spritecollide(ball1,all_bricks,False)
    for brick in brick_collision_list:
        ball1.bounce()
        ObjectProperties.score += 1
        brick.kill()
        # Display Level Complete Message for 3 seconds
        if len(all_bricks) == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, ObjectProperties.WHITE)
            screen.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)

            # Stop the Game
            carryOn = False

    # Draw all the sprites in one go
    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 20)
    text = font.render("Delete me", 1, ObjectProperties.BLACK)
    screen.blit(text, (205, 14))
    text = font.render("Score", 1, ObjectProperties.BLACK)
    screen.blit(text, (355, 14))
    text = font.render("User", 1, ObjectProperties.BLACK)
    screen.blit(text, (505, 14))

    # Update the screen
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine
pygame.quit()