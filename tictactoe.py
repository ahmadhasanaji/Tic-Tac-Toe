import tkinter as tk

class GameState:
    PLAYING = 0
    DRAW = 1
    CROSS_WON = 2
    NOUGHT_WON = 3

class Seed:
    EMPTY = 0
    CROSS = 1
    NOUGHT = 2

class Cell:
    def __init__(self, row, col):
        self.content = Seed.EMPTY
        self.row = row
        self.col = col

    def clear(self):
        self.content = Seed.EMPTY

    def paint(self, canvas):
        cell_x = self.col * 100
        cell_y = self.row * 100
        canvas.create_rectangle(cell_x, cell_y, cell_x + 100, cell_y + 100, outline="black")
        if self.content == Seed.CROSS:
            canvas.create_line(cell_x + 20, cell_y + 20, cell_x + 80, cell_y + 80, fill="red", width=4)
            canvas.create_line(cell_x + 80, cell_y + 20, cell_x + 20, cell_y + 80, fill="red", width=4)
        elif self.content == Seed.NOUGHT:
            canvas.create_oval(cell_x + 20, cell_y + 20, cell_x + 80, cell_y + 80, outline="blue", width=4)

class Board:
    def __init__(self):
        self.cells = [[Cell(row, col) for col in range(3)] for row in range(3)]

    def init(self):
        for row in range(3):
            for col in range(3):
                self.cells[row][col].clear()

    def is_draw(self):
        for row in range(3):
            for col in range(3):
                if self.cells[row][col].content == Seed.EMPTY:
                    return False
        return True

    def has_won(self, seed, seed_row, seed_col):
        return (self.cells[seed_row][0].content == seed
                and self.cells[seed_row][1].content == seed
                and self.cells[seed_row][2].content == seed
                or self.cells[0][seed_col].content == seed
                and self.cells[1][seed_col].content == seed
                and self.cells[2][seed_col].content == seed
                or seed_row == seed_col
                and self.cells[0][0].content == seed
                and self.cells[1][1].content == seed
                and self.cells[2][2].content == seed
                or seed_row + seed_col == 2
                and self.cells[0][2].content == seed
                and self.cells[1][1].content == seed
                and self.cells[2][0].content == seed)

    def paint(self, canvas):
        for row in range(3):
            for col in range(3):
                self.cells[row][col].paint(canvas)

class GameMain(tk.Frame):
    ROWS = 3
    COLS = 3
    CELL_SIZE = 100
    CANVAS_WIDTH = CELL_SIZE * COLS
    CANVAS_HEIGHT = CELL_SIZE * ROWS
    GRID_WIDTH = 8
    GRID_WIDTH_HALF = GRID_WIDTH // 2
    CELL_PADDING = CELL_SIZE // 6
    SYMBOL_SIZE = CELL_SIZE - CELL_PADDING * 2
    SYMBOL_STROKE_WIDTH = 8

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.canvas = tk.Canvas(self, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT)
        self.canvas.pack()
        self.board = Board()
        self.init_game()

    def init_game(self):
        for row in range(3):
            for col in range(3):
                self.board.cells[row][col].clear()
        self.current_state = GameState.PLAYING
        self.current_player = Seed.CROSS

    def update_game(self, the_seed, row, col):
        if self.board.has_won(the_seed, row, col):
            self.current_state = (GameState.CROSS_WON if the_seed == Seed.CROSS else GameState.NOUGHT_WON)
        elif self.board.is_draw():
            self.current_state = GameState.DRAW

    def paint(self):
        self.canvas.delete("all")
        self.board.paint(self.canvas)

    def handle_click(self, event):
        row = event.y // 100
        col = event.x // 100
        if self.current_state == GameState.PLAYING and self.board.cells[row][col].content == Seed.EMPTY:
            self.board.cells[row][col].content = self.current_player
            self.update_game(self.current_player, row, col)
            self.current_player = Seed.NOUGHT if self.current_player == Seed.CROSS else Seed.CROSS
            self.paint()

root = tk.Tk()
app = GameMain(master=root)

app.canvas.bind("<Button-1>", app.handle_click)
app.paint()
app.mainloop()
