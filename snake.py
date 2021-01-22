import pygame,math,random,sys,time,quicksort
try:
    import Score
except ModuleNotFoundError:
    file = open('Score.py', 'w')
    file.write("S = []")
    file.close()
    import Score

#start pygame
pygame.init()
pygame.display.init()
clock = pygame.time.Clock()
size = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
run=True

#variables
user_text = ''
speed = 20
select = 1
select2 = 1
select3 = 1
page = 0
frames = 0
snakeSize = 40
snakeLength = (800/40)*(600/40)-2
direction = 'W'
command = 'W'
grid = []
font = pygame.font.SysFont("Verdana", 20)
font1 = pygame.font.SysFont("Verdana", 50)

#objects
select_box = pygame.Rect(size[0]/2-200,50,size[0]/2,75)

#functions and procedures

def create_score_screen():
    screen.fill("black")
    for i in range(0,len(Score.S)):
        if i <= 17:
            img = font.render(str(Score.S[i][0]),False,"white")
            screen.blit(img, (size[0]/2-350, i*30+30))
            img = font.render(str(Score.S[i][1]),False,"white")
            screen.blit(img, (size[0]/2-200, i*30+30))
            img = font.render(str(Score.S[i][2]),False,"white")
            screen.blit(img, (size[0]/2+100, i*30+30))
            img = font.render(str(Score.S[i][3]),False,"white")
            screen.blit(img, (size[0]/2+200, i*30+30))

def create_name_selection_screen():
    screen.fill("black")
    img = font1.render("Save name", False, "white")
    screen.blit(img, (size[0]/2-150, 150))
    img1 = font.render(user_text, False, "white")
    screen.blit(img1, (size[0]/2-150, 250))
    #pygame.draw.line(screen,"white",(size[0]/2,0),(size[0]/2,size[1]))

def create_save_screen():
    screen.fill("black")
    img = font1.render("Save?", False, "white")
    screen.blit(img, (size[0]/2-75, 150))
    if select3 == 1:
        pygame.draw.rect(screen,"#141414",(size[0]/2-150-10, 300-10,55,50))
    else:
        pygame.draw.rect(screen,"#141414",(size[0]/2+100-10, 300-10,55,50))
    img1 = font.render("Yes", False, "white")
    screen.blit(img1, (size[0]/2-150, 300))
    img2 = font.render("No", False, "white")
    screen.blit(img2, (size[0]/2+100, 300))
    #pygame.draw.line(screen,"white",(size[0]/2,0),(size[0]/2,size[1]))

def create_score(P,name):
    global page
    if snakeSize == 40:
        SaveSize = "Big"
    elif snakeSize == 20:
        SaveSize = "Normal"
    elif snakeSize == 10:
        SaveSize = "Small"
    if speed == 20:
        SaveSpeed = "Slow"
    elif speed == 10:
        SaveSpeed = "Normal"
    elif speed == 5:
        SaveSpeed = "Fast"

    Score.S.append([P,name,SaveSpeed,SaveSize])
    new = quicksort.quickSort(Score.S,0,len(Score.S)-1)
    file = open('Score.py', 'w')
    file.write("S = ")
    file.close()
    file = open('Score.py', 'a')
    file.write(str(new))
    file.close()
    page = 0

def create_point():
    global grid
    global pointPos
    if not snakeLength == (size[0]/snakeSize)*(size[1]/snakeSize):
        pointPos = [random.randint(0,(size[1]/snakeSize)-1),random.randint(0,(size[0]/snakeSize)-1)]
        while grid[pointPos[0]][pointPos[1]] != 0:
            pointPos = [random.randint(0,(size[1]/snakeSize)-1),random.randint(0,(size[0]/snakeSize)-1)]
        grid[pointPos[0]][pointPos[1]] = 1

def create_settings():
    screen.fill("black")
    pygame.draw.rect(screen,"#141414",select_box)
    img = font1.render("- Size +", False, "white")
    screen.blit(img, (size[0]/2-100, 50))
    img4 = font.render("  Big", False, "white")
    if snakeSize == 40:
        img4 = font.render("  Big", False, "white")
    elif snakeSize == 20:
        img4 = font.render("Normal", False, "white")
    elif snakeSize == 10:
        img4 = font.render(" Small", False, "white")
    screen.blit(img4, (size[0]/2-30, 110))
    img2 = font1.render("- Speed +", False, "white")
    screen.blit(img2, (size[0]/2-120, 250))
    img5 = font.render(" Slow", False, "white")
    if speed == 5:
        img5 = font.render(" Fast", False, "white")
    elif speed == 10:
        img5 = font.render("Normal", False, "white")
    elif speed == 20:
        img5 = font.render(" Slow", False, "white")
    screen.blit(img5, (size[0]/2-30, 310))
    img3 = font1.render("Done", False, "white")
    screen.blit(img3, (size[0]/2-60, 450))

def create_main_menu():
    screen.fill("black")
    pygame.draw.rect(screen,"#141414",select_box)
    img = font1.render("Play game", False, "white")
    screen.blit(img, (size[0]/2-130, 50))
    img2 = font1.render("Settings", False, "white")
    screen.blit(img2, (size[0]/2-105, 250))
    img3 = font1.render("Score", False, "white")
    screen.blit(img3, (size[0]/2-70, 450))

def game_over():
    global page, select_box
    time.sleep(.750)
    page = 3
    select_box = pygame.Rect(size[0]/2-200,50,size[0]/2,75)
    screen.fill("black")
    #page = 0

def draw(x,y):
    if grid[x][y] >= 2:
        pygame.draw.rect(screen,"white",(y*snakeSize,x*snakeSize,snakeSize,snakeSize))
    elif grid[x][y] == 1:
        pygame.draw.rect(screen,"green",(y*snakeSize,x*snakeSize,snakeSize,snakeSize))
    
def get_head_pos():
    pos = []
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if grid [i][j] == 2:
                pos = [i,j]
    return pos

def create_tail():
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if grid[i][j] >= 2:
                grid[i][j] = int(math.fmod(grid[i][j]+1,snakeLength+2))

def move_grid():
    global direction
    global grid
    global snakeLength
    pos = get_head_pos()
    if command == 'W' and pos[1]>0 and (grid[pos[0]][pos[1]-1] == 0 or grid[pos[0]][pos[1]-1] == snakeLength+1 or grid[pos[0]][pos[1]-1] == 1):
        create_tail()
        if grid[pos[0]][pos[1]-1] == 1:
            snakeLength +=1
            create_point()
        grid[pos[0]][pos[1]-1] = 2
        direction = command
    elif command == 'E' and pos[1] < (size[0]/snakeSize)-1 and (grid[pos[0]][pos[1]+1] == 0 or grid[pos[0]][pos[1]+1] == snakeLength+1 or grid[pos[0]][pos[1]+1] == 1):
        create_tail()
        if grid[pos[0]][pos[1]+1] == 1:
            snakeLength +=1
            create_point()
        grid[pos[0]][pos[1]+1] = 2
        direction = command
    elif command == 'N' and pos[0]>0 and (grid[pos[0]-1][pos[1]] == 0 or grid[pos[0]-1][pos[1]] == snakeLength+1 or grid[pos[0]-1][pos[1]] == 1):
        create_tail()
        if grid[pos[0]-1][pos[1]] == 1:
            snakeLength +=1
            create_point()
        grid[pos[0]-1][pos[1]] = 2
        direction = command
    elif command == 'S' and pos[0] < (size[1]/snakeSize)-1 and (grid[pos[0]+1][pos[1]] == 0 or grid[pos[0]+1][pos[1]] == snakeLength+1 or grid[pos[0]+1][pos[1]] == 1):
        create_tail()
        if grid[pos[0]+1][pos[1]] == 1:
            snakeLength +=1
            create_point()
        grid[pos[0]+1][pos[1]] = 2
        direction = command
    else:
        game_over()

def start_game():
    global snakeSize, grid, snakeLength, direction, command, frames 
    grid = []
    if snakeSize == 40:
        for i in range(0,int(size[1]/snakeSize)):
            grid.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif snakeSize == 10:
        for i in range(0,int(size[1]/snakeSize)):
            grid.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif snakeSize == 20:
        for i in range(0,int(size[1]/snakeSize)):
            grid.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    grid[int(size[1]/snakeSize/2)][int(size[0]/snakeSize/2)] = 2
    snakeLength = 2
    direction = 'W'
    command = 'W'
    create_point()
    frames = 0

#game loop
while run:
    if snakeLength == (size[0]/snakeSize)*(size[1]/snakeSize):
        game_over()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

        #player movement
        if page == 2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if not direction == 'S':
                        command = 'N'
                elif event.key == pygame.K_a:
                    if not direction == 'E':
                        command = 'W'
                elif event.key == pygame.K_s:
                    if not direction == 'N':
                        command = 'S'
                elif event.key == pygame.K_d:
                    if not direction == 'W':
                        command = 'E'

        elif page == 0:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and select != 1:
                    select -= 1
                    select_box.y -= 200
                elif event.key == pygame.K_s and select != 3:
                    select += 1
                    select_box.y += 200
                elif event.key == pygame.K_SPACE :
                    if select == 1:
                        start_game()
                        page = 2
                    elif select == 2:
                        select_box = pygame.Rect(size[0]/2-200,50,size[0]/2,75)
                        page = 1
                        select2 = 1
                    elif select == 3:
                        page = 5
        elif page == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and select2 != 1:
                    select2 -= 1
                    select_box.y -= 200
                elif event.key == pygame.K_s and select2 != 3:
                    select2 += 1
                    select_box.y += 200
                elif event.key == pygame.K_SPACE and select2 == 3:
                    select_box = pygame.Rect(size[0]/2-200,50,size[0]/2,75)
                    page = 0
                    select = 1
                elif event.key == pygame.K_a:
                    if select2 == 1 and snakeSize != 10:
                        snakeSize = snakeSize/2
                    elif select2 == 2 and speed != 20:
                        speed = speed*2
                elif event.key == pygame.K_d:
                    if select2 == 1 and snakeSize != 40:
                        snakeSize = snakeSize*2
                    elif select2 == 2 and speed != 5:
                        speed = speed/2

        elif page == 3:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if select3 == 1:
                        page = 4
                    elif select3 == 2:
                        page = 0
                        select3 = 1
                elif event.key == pygame.K_a and select3 == 2:
                    select3 = 1
                elif event.key == pygame.K_d and select3 == 1:
                    select3 = 2
        elif page == 4:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    create_score(snakeLength-2,user_text)
                    user_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
        elif page == 5:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    page = 0

    if page == 2:
        if math.fmod(frames,speed) == 0.0:
            screen.fill("black")

            #move grid
            move_grid()

            #draw objects
            for i in range(0,len(grid)):
                for j in range(0,len(grid[i])):
                    draw(i,j)
            
            #score
            img1 = font.render(f"{snakeLength-2}", False, "grey")
            screen.blit(img1, (size[0]/2-6, 8))

        frames += 1

    #main menu
    elif page == 0:
        #write text
        create_main_menu()
    elif page == 1:
        create_settings()
    elif page == 3:
        create_save_screen()
    elif page == 4:
        create_name_selection_screen()
    elif page == 5:
        create_score_screen()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()