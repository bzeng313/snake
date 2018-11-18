import curses
import random

screen = curses.initscr()
curses.curs_set(False)
screen_h, screen_w = screen.getmaxyx()
window = curses.newwin(screen_h, screen_w, 0, 0)
window.keypad(True)
window.timeout(100)

snake = [
			(screen_h/2, screen_w/2)
		]

while True:
	food = (random.randint(0, screen_h - 2), random.randint(0, screen_w - 1))
	if food != snake[0]:
		break

window.addch(food[0], food[1], '*')	
window.addch(snake[0][0], snake[0][1], 'O')

#snake_head = snake[0]
#snake_tail = snake[0]
prev_key = random.choice([
							curses.KEY_LEFT,
							curses.KEY_RIGHT,
							curses.KEY_UP,
							curses.KEY_DOWN
						])
score = 0
window.addstr(screen_h - 1, 0, 'Score: %d'%score)
while True:
	new_key = window.getch()
	
	if (
		(new_key == curses.KEY_LEFT and prev_key != curses.KEY_RIGHT) or 
		(new_key == curses.KEY_RIGHT and prev_key != curses.KEY_LEFT) or 
		(new_key == curses.KEY_UP and prev_key != curses.KEY_DOWN) or 
		(new_key == curses.KEY_DOWN and prev_key != curses.KEY_UP)
		):
		prev_key = new_key

	if prev_key == curses.KEY_LEFT:
		snake.insert(0, (snake[0][0], snake[0][1] - 1))
	elif prev_key == curses.KEY_RIGHT:
		snake.insert(0, (snake[0][0], snake[0][1] + 1))
	elif prev_key == curses.KEY_UP:
		snake.insert(0, (snake[0][0] - 1, snake[0][1]))
	elif prev_key == curses.KEY_DOWN:
		snake.insert(0, (snake[0][0] + 1, snake[0][1]))
	
	snake_tail = snake.pop()
	window.addch(snake_tail[0], snake_tail[1], ' ')
	
	if snake[0] == food:
		snake.append(snake_tail)
 		score += 100
		while food in snake:
			food = (random.randint(0, screen_h - 2), random.randint(0, screen_w - 1))
		window.addch(food[0], food[1], '*')	
		window.addstr(screen_h - 1, 0, 'Score: %d'%score)

	if (
		snake[0] in snake[1:] or 
		snake[0][0] >= screen_h - 1 or 
		snake[0][0] < 0 or 
		snake[0][1] >= screen_w or 
		snake[0][1] < 0
		):
		break

	for y, x in snake:
		window.addch(y, x, 'O')
				
curses.endwin()
