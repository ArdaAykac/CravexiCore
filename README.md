# Cravexi Core Game Engine

OPD2, Python ile terminal ve OpenGL tabanlı oyunlar geliştirmek için hazırlanmış bir kütüphanedir.
Kütüphane 2D oyun, animasyon, envanter, UI, RAM yönetimi ve network desteği sunar.

İçindekiler  
    [Kurulum](#Kurulum)  
    [Yeni Oyun Başlatma (NewGame)](#NewGame)  
    [Inventory ve SaveSystem](#Inventory&SaveSystem)  
    [debug_system](#debug_system)   
    [RAMManager](#RAMManager)    
    [GameLoop](#GameLoop)  
    [OPD2](#GUISLibrary)  
    [UI](#UI)      
    [MultiPlayer](#Network)   
    [Registry&İtems](#Registry&items) 



#Kurulum
Python 3.10 veya üstü Gerekli kütüphaneler:     

    pip install glfw PyOpenGL Pillow

Engine Klasöründeki tüm dosyaları kendi mevcut projenize eklemelisiniz

Önerilen klasör yapısı:

    engine/
    ├─ __init__.py
    ├─ GLANIM.py
    ├─ GLElements.py
    ├─ UI.py
    ├─ registry.py
    ├─ inventory.py
    ├─ network_driver.py

#NewGame  
Oyun oluşturmak ve türlerini yönetmek için kullanılır.

| Özellik / Fonksiyon                     | Açıklama                               | Parametreler / Dönüş                                 |
| --------------------------------------- | -------------------------------------- | ---------------------------------------------------- |
| `base_folder`                           | Oyun dosyalarının kaydedileceği klasör | string, default `"database"`                         |
| `current_game`                          | Şu anki oyun bilgisi                   | `[game_name, networking]`                            |
| `game_types`                            | Oyun türleri ve indeksleri             | dict, ör: `{"game name":0,"networking":1,"Games":2}` |
| `new_game(game_name, networking=False)` | Yeni oyun oluşturur ve klasörü açar    | `game_name: str`, `networking: bool (default False)` |

Örnek:

    from engine import New_Game

    New_Game.new_game("MyFirstGame", networking=True)
    print(New_Game.current_game)  # ['MyFirstGame', True]

#Inventory&SaveSystem

Sınıf: Inventory  
Oyun içi itemleri yönetir.
| Fonksiyon                     | Açıklama                                    | Parametreler / Dönüş                                   |
| ----------------------------- | ------------------------------------------- | ------------------------------------------------------ |
| `add_item(item_key, count=1)` | Envantere item ekler                        | `item_key: str`, `count: int (default 1)`, dönüş: bool |
| `set_item(item_key, count)`   | Item sayısını ayarlar veya sıfırsa kaldırır | `item_key: str`, `count: int`, dönüş: bool             |

Örnek:

    from engine.inventory import Inventory
    inv = Inventory()
    inv.add_item("game:stone", 5)  # 5 taş ekle
    inv.set_item("game:wood", 3)   # 3 odun

Sınıf: SaveSystem  
Envanteri kaydetmek ve yüklemek için kullanılır.

| Fonksiyon                                                         | Açıklama             | Parametreler / Dönüş                                      |
| ----------------------------------------------------------------- | -------------------- | --------------------------------------------------------- |
| `save_inventory(game_name, inventory, filename="inventory.json")` | JSON olarak kaydeder | `game_name: str`, `inventory: Inventory`, `filename: str` |
| `load_inventory(game_name, inventory, filename="inventory.json")` | JSON’dan yükler      | `game_name: str`, `inventory: Inventory`, `filename: str` |
| `list_games(list_games=False, folders_path="database")`           | Klasörleri listeler  | `list_games: bool`, `folders_path: str`                   |

Örnek:

    from engine import SaveSystem
    SaveSystem.save_inventory("MyFirstGame", inv)
    SaveSystem.load_inventory("MyFirstGame", inv)

#debug_system  
Debug modunu aktif eder ve oyun durumunu gösterir.
| Fonksiyon                              | Açıklama                   | Parametreler                                      |
| -------------------------------------- | -------------------------- | ------------------------------------------------- |
| `debug(arg, *game_types, debug=False)` | Debug mesajlarını yazdırır | `arg: str`, `game_types: str list`, `debug: bool` |

Örnek:

    from engine import debug_system
    debug_system.debug("Status", "networking", debug=True)


#RAMManager  
Bellek tabanlı geçici veri saklama sistemi.
| Fonksiyon / Özellik | Açıklama            | Parametreler / Dönüş            |
| ------------------- | ------------------- | ------------------------------- |
| `__init__(size_kb)` | RAM alanı ayarlar   | `size_kb: int`                  |
| `store(key, data)`  | Veriyi RAM’e yazar  | `key: str`, `data: bytes`       |
| `load(key)`         | Veriyi RAM’den okur | `key: str`, dönüş: `memoryview` |

Örnek:

    ram = RAMManager(1024)
    ram.store("player_data", b"Player info")
    data = ram.load("player_data")
    print(bytes(data))


#GameLoop  
FPS tabanlı oyun döngüsü.

| Fonksiyon / Özellik                    | Açıklama               | Parametreler / Dönüş             |
| -------------------------------------- | ---------------------- | -------------------------------- |
| `__init__(target_fps=60, debug=False)` | Oyun döngüsü oluşturur | `target_fps: int`, `debug: bool` |
| `add(obj)`                             | GameLoop’a obje ekler  | obj: `Behaviour` veya benzeri    |
| `run()`                                | Döngüyü başlatır       | -                                |
| `stop()`                               | Döngüyü durdurur       | -                                |
| `log(*args)`                           | Debug log              | args: list                       |

Örnek:

    from engine import GameLoop, Behaviour

    class MyObj(Behaviour):
        def update(self, dt):
            print(f"Update dt={dt}")

    loop = GameLoop(debug=True)
    loop.add(MyObj())
    loop.run()


#GUISLibrary  

Pencere Oluşturma – OPD2  
OPD2 sınıfı OpenGL tabanlı bir pencere açmak ve render döngüsünü yönetmek için kullanılır.

    from engine import OPD2

    window = OPD2(width=800, height=600, window_name="My Game")

| Parametre     | Açıklama           | Zorunlu | Tip |
| ------------- | ------------------ | ------- | --- |
| `width`       | Pencere genişliği  | Evet    | int |
| `height`      | Pencere yüksekliği | Evet    | int |
| `window_name` | Pencere başlığı    | Evet    | str |

| Fonksiyon        | Açıklama                                                              |
| ---------------- | --------------------------------------------------------------------- |
| `begin_frame()`  | Yeni frame için hazırlık. Temizler ve ortografik projeksiyon ayarlar. |
| `end_frame()`    | Frame’i ekrana gönderir ve inputları poll eder.                       |
| `should_close()` | Pencerenin kapanıp kapanmadığını kontrol eder.                        |
| `close()`        | Pencereyi kapatır.                                                    |
| `terminate()`    | GLFW kütüphanesini kapatır.                                           |



Buton Oluşturma – GLButton

    from engine import GLButton, ButtonAnimProfile

    def on_click():
        print("Button clicked!")

    button = GLButton(
        x=100, y=100, w=150, h=50,
        color=(0.2, 0.7, 0.3),
        on_click=on_click,
        text="Click Me",
        text_color=(1,1,1),
        text_scale=6,
        anim_profile=ButtonAnimProfile(hover_brightness=1.1, press_scale=0.9),
        texture_path=None
    )

Zorunlu Parametreler
| Parametre  | Açıklama                                   |
| ---------- | ------------------------------------------ |
| `x`        | Buton sol üst köşe X koordinatı            |
| `y`        | Buton sol üst köşe Y koordinatı            |
| `w`        | Buton genişliği                            |
| `h`        | Buton yüksekliği                           |
| `color`    | RGB tuple `(r,g,b)` (0.0-1.0)              |
| `on_click` | Fonksiyon referansı, tıklandığında çalışır |

Opsiyonel Parametreler
| Parametre      | Açıklama                  | Default               |
| -------------- | ------------------------- | --------------------- |
| `text`         | Buton üzerindeki yazı     | `""`                  |
| `text_color`   | Yazı rengi `(r,g,b)`      | `(1,1,1)`             |
| `text_scale`   | Yazı boyutu               | `6`                   |
| `anim_profile` | Hover ve press animasyonu | `ButtonAnimProfile()` |
| `texture_path` | PNG/JPG yolu              | `None`                |



Animasyon Profili – ButtonAnimProfile  
Butonlar hover ve tıklama animasyonları alabilir.

    profile = ButtonAnimProfile(hover_brightness=1.2, press_scale=0.92, press_time=0.15)


| Parametre          | Açıklama                              | Default |
| ------------------ | ------------------------------------- | ------- |
| `hover_brightness` | Hover durumunda renk çarpanı          | `1.2`   |
| `press_scale`      | Tıklandığında butonun küçülme oranı   | `0.92`  |
| `press_time`       | Tıklama animasyonunun süresi (saniye) | `0.12`  |


Animasyon Yönetimi – GLButtonAnimator

    from engine import GLButtonAnimator

    animator = GLButtonAnimator()
    state = animator.update(button, window)

update(button, window) → ButtonAnimState döner  
ButtonAnimState içerir: hover, pressed, scale, color_mul


Label Oluşturma – GLLabel  
yazı göstermek için.

    from engine import GLLabel

    label = GLLabel(x=50, y=400, text="Hello World", color=(1,1,0), scale=8, max_width=500)

Nesneler  
GLELEMENTS
Transform

GLObject (Base class)

GLQuad

GLCircle

GLCylinder

🔹 Transform

Tüm sahne objelerinin konum, dönüş ve ölçek bilgilerini tutar.

Oluşturma

    t = Transform(x=0, y=0, z=0, rotation=0, sx=1, sy=1, sz=1)

| Özellik    | Tip            | Açıklama               |
| ---------- | -------------- | ---------------------- |
| `position` | `[x, y, z]`    | Dünya konumu           |
| `rotation` | `float`        | Derece cinsinden dönüş |
| `scale`    | `[sx, sy, sz]` | Ölçek                  |

Metotlar

    translate(dx, dy, dz=0)
Objeyi mevcut konumundan kaydırır.

    rotate(angle)
Objeyi Z ekseni etrafında döndürür.

    set_position(x, y, z=0)
Objenin konumunu doğrudan ayarlar.

    set_rotation(angle)
Objenin dönüşünü doğrudan ayarlar.

GLObject (Base Class)

Tüm OpenGL objelerinin temel sınıfıdır.
Tek başına çizilmez.

| Özellik     | Açıklama              |
| ----------- | --------------------- |
| `transform` | Transform instance    |
| `color`     | RGB tuple             |
| `visible`   | Çizilip çizilmeyeceği |


🔹 GLQuad (Dikdörtgen / Kare)

2D düzlemde merkezden çizilen bir dörtgendir.

Oluşturma

    quad = GLQuad(width=100, height=50, color=(1, 0, 0))
Çizim Özellikleri   
Merkezden çizilir   
Transform tamamen etkilidir   
Z rotasyonu destekler   

Örnek Kullanım

    from engine.GLELEMENTS import GLQuad
    quad = GLQuad(100, 100, color=(1, 0, 0))
    quad.transform.set_position(400, 300)
    quad.transform.set_rotation(45)
    quad.draw()

GLCircle (2D Daire)

Segment bazlı OpenGL dairesi.

    circle = GLCircle(radius=50, segments=32, color=(0, 1, 0))

| Parametre  | Açıklama         |
| ---------- | ---------------- |
| `radius`   | Yarıçap          |
| `segments` | Daire düzgünlüğü |
| `color`    | RGB renk         |

Örnek

    circle = GLCircle(40, color=(0, 0, 1))
    circle.transform.set_position(200, 200)
    circle.draw()

GLCylinder (3D Silindir)  
Z ekseninde yükselen 3D silindir.

Oluşturma:   

    cyl = GLCylinder(radius=20, height=100, segments=32, color=(1, 1, 0))

Notlar   
Y ekseni etrafında döner   
Derinlik testi (GL_DEPTH_TEST) gerektirir   
OPD2 classında varsayılan olarak kapalıdır   
Sadece 3D pencerelerde kullanılır şuanllık OPD2 yani 2D pencere desteği vardır

    glEnable(GL_DEPTH_TEST)
    cyl = GLCylinder(30, 120)
    cyl.transform.set_position(400, 300, 0)
    cyl.transform.set_rotation(45)
    cyl.draw()


örnek oyun:

    from engine.GUIS import OPD2
    from engine.GLELEMENTS import GLQuad, GLCircle

    window = OPD2(800, 600, "Demo")

    quad = GLQuad(100, 100, color=(1, 0, 0))
    quad.transform.set_position(400, 300)

    circle = GLCircle(40, color=(0, 1, 0))
    circle.transform.set_position(200, 200)

    while not window.should_close():
        window.begin_frame()
        quad.draw()
        circle.draw()
        window.end_frame()

    window.terminate()



| Parametre   | Açıklama                              | Zorunlu / Opsiyonel | Default   |
| ----------- | ------------------------------------- | ------------------- | --------- |
| `x`         | Sol üst X koordinatı                  | Zorunlu             | -         |
| `y`         | Sol üst Y koordinatı                  | Zorunlu             | -         |
| `text`      | Gösterilecek yazı                     | Zorunlu             | -         |
| `color`     | RGB tuple `(r,g,b)`                   | Opsiyonel           | `(1,1,1)` |
| `scale`     | Yazı boyutu                           | Opsiyonel           | `10`      |
| `max_width` | Satır kaydırma için maksimum genişlik | Opsiyonel           | `None`    |


#UI
Terminal UI – Button, Label, UIManager, Scene, SceneManager  
Python terminali için kullanılır. OpenGL(OPD2) gerekmez.

Buton – Button

    from engine import Button

    def say_hello():
        print("Hello Terminal!")

    btn = Button("Click Me", say_hello)

Zorunlu: text, on_click  
Opsiyonel: focusable (default True)


Label – Label

    from engine import Label
    lbl = Label("This is a label")

Zorunlu: text  
Opsiyonel: visible (default True)

UI Manager – UIManager 

    manager = UIManager()
    manager.add(btn)
    manager.add(lbl)
    manager.update(0.016)  # 60 FPS benzeri update
    manager.feed_input("enter")  # input simülasyonu

elements: UI elemanlarını tutar  
focus_index: odaklanılan element  
dirty: çizim gerekip gerekmediği  
input_buffer: input tutar


Scene – Scene

    scene = Scene("Main")
    scene.ui_manager.add(btn)
    scene.ui_manager.add(lbl)
    scene.enter()
    scene.update(0.016)
    scene.exit()


Scene Manager – SceneManager

    sm = SceneManager()
    sm.change_scene(scene)
    sm.feed_input("enter")
    sm.update(0.016)


Input Thread

    from engine import start_input_thread
    start_input_thread(sm)

Kullanıcı terminalden girdi yapabilir  
Thread sürekli input bekler

Kullanım Örnekleri

OPD2

    from engine import OPD2, GLButton, GLLabel, GLButtonAnimator

    window = OPD2(800, 600, "Test Game")
    button = GLButton(100,100,150,50,(0.5,0.5,1.0), lambda: print("Clicked!"),     text="Press")   
    label = GLLabel(50, 400, "Hello World")

    animator = GLButtonAnimator()

    while not window.should_close():
        window.begin_frame()
        state = animator.update(button, window)
        button.handle_click(window, state)
        button.draw(state)
        label.draw()
        window.end_frame()

    window.terminate()


Terminal UI


    from engine import Button, Label, Scene, SceneManager, start_input_thread

    def greet():
        print("Hello Terminal!")

    scene = Scene("Main")
    scene.ui_manager.add(Label("Welcome"))
    scene.ui_manager.add(Button("Say Hello", greet))

    sm = SceneManager()
    sm.change_scene(scene)
    start_input_thread(sm)

    while True:
        sm.update(0.016)



#Network  
TCP server oluşturma:

    from engine import network

    network.create_server("127.0.0.1", 5555, max_player=4, debug=True)


| Parametre    | Açıklama        | Default / Tür      |
| ------------ | --------------- | ------------------ |
| `server_ip`  | Sunucu IP       | str                |
| `port`       | Port numarası   | int                |
| `max_player` | Maksimum oyuncu | int, default 4     |
| `debug`      | Debug mesajları | bool, default True |


#Registry&items  
Registry, oyun içi itemleri saklar.

Fonksiyonlar:  
register_item(key, data) → Yeni item ekler  
get_item(key) → Item bilgisini döndürür  
has_item(key) → Item var mı kontrol eder

    from engine.registry import Registry
    from engine.items import load_vanilla_item
    
    load_vanilla_item()
    print(Registry.get_item("game:stone"))
