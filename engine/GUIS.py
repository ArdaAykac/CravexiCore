# UI.py
import threading
import os
import unicodedata
import glfw
from OpenGL.GL import *

# -------------------- PRINT SISTEMI --------------------
class UIPrint:
    """
    Scene ve UI ile entegre çalışan print sistemi.
    Normal print gibi kullanılır: UIPrint.print("Hello")
    Ama sahne değişince veya element silince metinler kaybolur.
    """
    def __init__(self):
        self.buffer = []  # yazılar saklanır
        self.active_scene = None

    def set_scene(self, scene):
        self.active_scene = scene
        self.buffer.clear()

    def print(self, *args, **kwargs):
        text = " ".join(str(a) for a in args)
        self.buffer.append(text)
        # sahne varsa hemen çiz
        if self.active_scene:
            self.active_scene.ui_manager.dirty = True

    def get_buffer(self):
        return self.buffer.copy()

    def clear(self):
        self.buffer.clear()
        if self.active_scene:
            self.active_scene.ui_manager.dirty = True

# Singleton instance
ui_print = UIPrint()

# -------------------- BASE UI ELEMENT --------------------
class UIElement:
    def __init__(self):
        self.visible = True
        self.ui = None
        self.focusable = False

    def draw(self, focused=False):
        pass

    def handle_input(self, input_type):
        pass

# -------------------- BUTTON --------------------
class Button(UIElement):
    def __init__(self, text, on_click):
        super().__init__()
        self.text = text
        self.on_click = on_click
        self.focusable = True

    def draw(self, focused=False):
        if self.visible:
            prefix = ">> " if focused else "   "
            print(f"{prefix}[ {self.text} ]")

    def handle_input(self, input_type):
        if input_type == "enter":
            self.on_click()
        elif isinstance(input_type, str):
            norm_input = unicodedata.normalize("NFKD", input_type).encode("ascii","ignore").decode().lower()
            norm_text = unicodedata.normalize("NFKD", self.text).encode("ascii","ignore").decode().lower()
            if norm_input == norm_text:
                self.on_click()

# -------------------- LABEL --------------------
class Label(UIElement):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def draw(self, focused=False):
        if self.visible:
            print(f"   {self.text}")

# -------------------- UI MANAGER --------------------
class UIManager:
    def __init__(self):
        self.elements = []
        self.focus_index = 0
        self.dirty = True
        self.input_buffer = None

    def add(self, element):
        element.ui = self
        self.elements.append(element)
        self.dirty = True

    def update(self, dt):
        if self.input_buffer:
            if self.input_buffer in ["w", "s", "enter"]:
                if self.input_buffer == "w":
                    self.move_focus(-1)
                elif self.input_buffer == "s":
                    self.move_focus(1)
                elif self.input_buffer == "enter":
                    focused = self.get_focused_element()
                    if focused:
                        focused.handle_input("enter")
            else:
                for e in self.elements:
                    e.handle_input(self.input_buffer)
            self.input_buffer = None
            self.dirty = True

        if self.dirty:
            self.draw()
            self.dirty = False

    def move_focus(self, direction):
        focusables = [i for i, e in enumerate(self.elements) if e.focusable]
        if not focusables:
            return
        if self.focus_index not in focusables:
            self.focus_index = focusables[0]
            return
        current = focusables.index(self.focus_index)
        new_index = (current + direction) % len(focusables)
        self.focus_index = focusables[new_index]

    def get_focused_element(self):
        if self.elements and 0 <= self.focus_index < len(self.elements):
            return self.elements[self.focus_index]
        return None

    def draw(self):
        os.system("cls" if os.name == "nt" else "clear")
        
        # Önce UI elemanlarını çiz
        print("\n--- UI ---")
        for i, e in enumerate(self.elements):
            focused = (i == self.focus_index)
            e.draw(focused)
        print("----------")
        
        # Sonra print buffer’ı göster
        if ui_print.get_buffer():
            print("\n".join(ui_print.get_buffer()))
            print("----------")

    def feed_input(self, input_str):
        self.input_buffer = input_str

# -------------------- SCENE --------------------
class Scene:
    def __init__(self, name):
        self.name = name
        self.ui_manager = UIManager()

    def enter(self):
        self.ui_manager.dirty = True
        ui_print.set_scene(self)

    def exit(self):
        self.ui_manager.dirty = False
        ui_print.clear()

    def update(self, dt):
        self.ui_manager.update(dt)

# -------------------- SCENE MANAGER --------------------
class SceneManager:
    def __init__(self):
        self.current_scene = None

    def change_scene(self, scene: Scene):
        if self.current_scene:
            self.current_scene.exit()
        self.current_scene = scene
        self.current_scene.enter()
        self.current_scene.ui_manager.dirty = True
        self.current_scene.ui_manager.draw()

    def update(self, dt):
        if self.current_scene:
            self.current_scene.update(dt)

    def feed_input(self, data):
        if self.current_scene:
            self.current_scene.ui_manager.feed_input(data)

# -------------------- INPUT THREAD --------------------
def start_input_thread(scene_manager: SceneManager):
    def input_loop():
        while True:
            cmd = input("> ").strip()
            scene_manager.feed_input(cmd)
    thread = threading.Thread(target=input_loop, daemon=True)
    thread.start()


class OPD2:
    def __init__(self, width, height, window_name):
        self.width = width
        self.height = height
        self.window_name = window_name
        self.background_color = (0.0, 0.0, 0.0, 1.0)

        if not glfw.init():
            raise Exception("GLFW başlatılamadı!")

        self.window = glfw.create_window(width, height, window_name, None, None)
        if not self.window:
            glfw.terminate()
            raise Exception("Pencere oluşturulamadı!")

        glfw.make_context_current(self.window)

        glViewport(0, 0, width, height)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, 0, height, -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glDisable(GL_DEPTH_TEST)

    def begin_frame(self):
        r, g, b, a = self.background_color
        glClearColor(r, g, b, a)
        glClear(GL_COLOR_BUFFER_BIT)

    def end_frame(self):
        glfw.swap_buffers(self.window)
        glfw.poll_events()

    def should_close(self):
        return glfw.window_should_close(self.window)

    def terminate(self):
        glfw.terminate()