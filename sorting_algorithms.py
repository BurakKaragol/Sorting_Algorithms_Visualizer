import math

import pygame
import random

pygame.init()

class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BLUE = 0, 0, 255
    GREY = 128, 128, 128
    LIGHT_GREY = 150, 150, 150
    DARK_GREY = 190, 190, 190
    DRAW_COLOR_RED = 1.25
    DRAW_COLOR_GREEN = 1.25
    DRAW_COLOR_BLUE = 1.25
    INCRIMINATION = 0.15
    BACKGROUND_COLOR = WHITE

    SORTING_INDEX = 0
    SORTING_ALGO_NAMES = ["Insertion Sort", "Bubble Sort", "Selection Sort", "Shell Sort"]

    FONT = pygame.font.SysFont('comicsans', 30)
    LARGE_FONT = pygame.font.SysFont('comicsans', 40)
    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithms")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

def draw(draw_info, algo_name, ascending, speed = 60, amount = 50):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}",
                                  1, draw_info.BLUE)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | Z - Reset Colors", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 45))

    order = draw_info.FONT.render("A - Ascending | D - Descending", 1, draw_info.BLACK)
    draw_info.window.blit(order, (draw_info.width / 2 - order.get_width() / 2, 75))

    sorting = draw_info.FONT.render("W - Previous Algorithm | S - Next Algorithm", 1, draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 105))

    speed_txt = draw_info.FONT.render(f"Speed: {speed}", 1, draw_info.BLACK)
    draw_info.window.blit(speed_txt, (10, 5))
    speed_txt2 = draw_info.FONT.render(f"up-down arrow keys", 1, draw_info.BLACK)
    draw_info.window.blit(speed_txt2, (10, 35))

    amount = draw_info.FONT.render(f"Count: {amount}", 1, draw_info.BLACK)
    draw_info.window.blit(amount, (10, 65))
    amount2 = draw_info.FONT.render(f"right-left arrow keys", 1, draw_info.BLACK)
    draw_info.window.blit(amount2, (10, 95))

    color_txt = draw_info.FONT.render(f"Color Values:", 1, draw_info.BLACK)
    draw_info.window.blit(color_txt, (draw_info.width - color_txt.get_width() - 10, 5))

    red_val = round(draw_info.DRAW_COLOR_RED * 100)
    red_txt = draw_info.FONT.render(f"f - {red_val} - g", 1, draw_info.RED)
    draw_info.window.blit(red_txt, (draw_info.width - red_txt.get_width() - 10, 35))

    green_val = round(draw_info.DRAW_COLOR_GREEN * 100)
    green_txt = draw_info.FONT.render(f"h - {green_val} - j", 1, draw_info.GREEN)
    draw_info.window.blit(green_txt, (draw_info.width - green_txt.get_width() - 10, 65))

    blue_val = round(draw_info.DRAW_COLOR_BLUE * 100)
    blue_txt = draw_info.FONT.render(f"k - {blue_val} - l", 1, draw_info.BLUE)
    draw_info.window.blit(blue_txt, (draw_info.width - blue_txt.get_width() - 10, 95))

    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info, color_positions = {}, clear_bg = False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD,
                      draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color_val_red = round(val * draw_info.DRAW_COLOR_RED)
        color_val_green = round(val * draw_info.DRAW_COLOR_GREEN)
        color_val_blue = round(val * draw_info.DRAW_COLOR_BLUE)
        color = (color_val_red, color_val_green, color_val_blue)

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()

def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst

def bubble_sort(draw_info, ascending = True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True

    return lst

def insertion_sort(draw_info, ascending = True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
            yield True

    return lst

def selection_sort(draw_info, ascending = True):
    lst = draw_info.lst

    for idx in range(len(lst)):
        min_idx = idx
        for j in range(idx + 1, len(lst)):
            if lst[min_idx] > lst[j] and ascending:
                min_idx = j
            if lst[min_idx] < lst[j] and not ascending:
                min_idx = j
        lst[idx], lst[min_idx] = lst[min_idx], lst[idx]
        draw_list(draw_info, {idx: draw_info.GREEN, min_idx: draw_info.RED}, True)
        yield True

    return lst

def shell_sort(draw_info, ascending = True):
    lst = draw_info.lst

    gap = len(lst) // 2
    while gap > 0:
        for i in range(gap, len(lst)):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp and ascending:
                lst[j] = lst[j - gap]
                j = j-gap
                lst[j] = temp
            while j >= gap and lst[j - gap] < temp and not ascending:
                lst[j] = lst[j - gap]
                j = j-gap
                lst[j] = temp
            draw_list(draw_info, {j: draw_info.GREEN, j - gap: draw_info.RED}, True)
            yield True
        gap = gap//2

    return lst

def set_algorithm(draw_info, sorting_algorithm, sorting_algo_name, next = True):
    if next:
        draw_info.SORTING_INDEX += 1
    else:
        draw_info.SORTING_INDEX -= 1

    if draw_info.SORTING_INDEX >= len(draw_info.SORTING_ALGO_NAMES):
        draw_info.SORTING_INDEX = 0

    if draw_info.SORTING_INDEX < 0:
        draw_info.SORTING_INDEX = len(draw_info.SORTING_ALGO_NAMES) - 1

    sorting_algo_name = draw_info.SORTING_ALGO_NAMES[draw_info.SORTING_INDEX]
    if draw_info.SORTING_INDEX == 0:
        sorting_algorithm = insertion_sort
    elif draw_info.SORTING_INDEX == 1:
        sorting_algorithm = bubble_sort
    elif draw_info.SORTING_INDEX == 2:
        sorting_algorithm = selection_sort
    elif draw_info.SORTING_INDEX == 3:
        sorting_algorithm = shell_sort

    return sorting_algorithm, sorting_algo_name

def set_color(color, incrimination, add = True):
    if add:
        color += incrimination
        if color > 2.25:
            color = 2.25
    else:
        color -= incrimination
        if color < 0.3:
            color = 0.3
    return color

def main():
    run = True
    clock = pygame.time.Clock()

    speed = 60
    increase_amount = 15

    n = 50
    min_val = 0
    max_val = 100
    lst =generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(1100, 700, lst)
    sorting = False
    ascending = True

    sorting_algorithm = insertion_sort
    sorting_algo_name = "Insertion Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(speed)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending, speed, n)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_w and not sorting:
                sorting_algorithm, sorting_algo_name = set_algorithm(draw_info,sorting_algorithm,
                                                                     sorting_algo_name, True)
            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm, sorting_algo_name = set_algorithm(draw_info, sorting_algorithm,
                                                                     sorting_algo_name, False)
            elif event.key == pygame.K_DOWN and not sorting:
                speed -= increase_amount
                if speed < 15:
                    speed = 15
            elif event.key == pygame.K_UP and not sorting:
                speed += increase_amount
                if speed > 150:
                    speed = 150
            elif event.key == pygame.K_LEFT and not sorting:
                n -= 10
                if n < 20:
                    n = 20
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_RIGHT and not sorting:
                n += 10
                if n > 120:
                    n = 120
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_f:
                draw_info.DRAW_COLOR_RED = set_color(draw_info.DRAW_COLOR_RED, draw_info.INCRIMINATION, False)
            elif event.key == pygame.K_g:
                draw_info.DRAW_COLOR_RED = set_color(draw_info.DRAW_COLOR_RED, draw_info.INCRIMINATION, True)
            elif event.key == pygame.K_h:
                draw_info.DRAW_COLOR_GREEN = set_color(draw_info.DRAW_COLOR_GREEN, draw_info.INCRIMINATION, False)
            elif event.key == pygame.K_j:
                draw_info.DRAW_COLOR_GREEN = set_color(draw_info.DRAW_COLOR_GREEN, draw_info.INCRIMINATION, True)
            elif event.key == pygame.K_k:
                draw_info.DRAW_COLOR_BLUE = set_color(draw_info.DRAW_COLOR_BLUE, draw_info.INCRIMINATION, False)
            elif event.key == pygame.K_l:
                draw_info.DRAW_COLOR_BLUE = set_color(draw_info.DRAW_COLOR_BLUE, draw_info.INCRIMINATION, True)
            elif event.key == pygame.K_z:
                draw_info.DRAW_COLOR_RED = 1.25
                draw_info.DRAW_COLOR_GREEN = 1.25
                draw_info.DRAW_COLOR_BLUE = 1.25

    pygame.quit()

if __name__ == "__main__":
    main()