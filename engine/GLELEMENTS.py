from OpenGL.GL import *
import glfw


class GLButton:
    def __init__(self, x, y, w, h, color, on_click):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.on_click = on_click
        self.pressed = False

    def update(self, window):
        mx, my = glfw.get_cursor_pos(window)
        my = glfw.get_window_size(window)[1] - my  # Y ekseni düzeltme

        hovered = (
            self.x <= mx <= self.x + self.w and
            self.y <= my <= self.y + self.h
        )

        if hovered and glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_LEFT) == glfw.PRESS:
            if not self.pressed:
                self.pressed = True
                self.on_click()
        else:
            self.pressed = False

    def draw(self):
        glColor3f(*self.color)

        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + self.w, self.y)
        glVertex2f(self.x + self.w, self.y + self.h)
        glVertex2f(self.x, self.y + self.h)
        glEnd()
