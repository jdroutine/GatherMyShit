import pygame

# zainicjowanie biblioteki
pygame.init()

# koordynaty
x = 70
y = 50

# gracz

# tworzy prostokąt w miejscu x,y o wymiarach 100x100px
player = pygame.rect.Rect(x, y, 100, 100)

# stworzenie okna gry
window = pygame.display.set_mode((800, 600))

# stworzenie nieskończonej pętli
run = True
while run:

    # szybkośc wykonywania pętli w fps
    pygame.time.Clock().tick(60)

    # odczytywanie zdarzeń wywołanych przez gracza
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # jeśli gracz zamknie okno gry
            run = False

    keys = pygame.key.get_pressed()  # przechwycenie informacji z klawiatury

    speed = 5  # prędkość poruszania się

    # sprawdzamy czy klawisz (strzałka w prawo)  jest naciśnięty
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:  # strzałka w lewo
        x -= speed
    if keys[pygame.K_UP]:  # strzałka w górę
        y -= speed
    if keys[pygame.K_DOWN]:  # strzałka w dół
        y += speed

    player = pygame.rect.Rect(x, y, 100, 100)  # odświerzenie położenia postaci

    window.fill((102, 0, 102))  # zmiana tła, kolor podany w rgb
    # narysowanie gracza (okno,kolor,gracz)
    pygame.draw.rect(window, (255, 255, 255), player)
    pygame.display.update()  # zapisuje każdą narysowaną zmianę
