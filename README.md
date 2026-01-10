## Technical Documentation

#TR

#### ECOSYSTEM Documentation

Bu dökümantasyon, Python tabanlı bir oyun ve veri yönetimi framework'ünü açıklamaktadır. Framework; oyun yaratma, kaydetme/yükleme, RAM yönetimi, oyun döngüsü ve davranış sınıflarını içerir.

⚡ Modules & Classes Overview
Class / Module	Açıklama

New_Game	Yeni oyun başlatmak ve oyun tiplerini yönetmek için kullanılır.

SaveSystem	Oyun verilerini (inventory vb.) kaydetmek ve yüklemek için kullanılır.

debug_system	Oyun sırasında debug mesajlarını yönetmek ve konsola yazdırmak için kullanılır.

RAMManager	RAM üzerinde veri depolamak ve hızlı erişim sağlamak için kullanılır.

Behaviour	Tüm oyun nesneleri için temel davranış şablonu. awake, start, update, draw fonksiyonlarını içerir.

GameLoop	Oyun döngüsünü yönetir. Nesneleri ekler, günceller ve hedef FPS ile çalıştırır.

#🕹️ New_Game Class

    ´´´
    class New_Game:
    base_folder = "database"  # Oyun verilerinin kaydedileceği klasör
    current_game = None
    game_types = {"game name": 0, "networking": 1, "Games": 2}

    @classmethod
    def new_game(cls, game_name: str, networking: bool=False):
        """
        Yeni bir oyun başlatır.

        Parameters:
        - game_name (str): Oyunun adı
        - networking (bool): Ağ desteği var mı?

        Side Effects:
        - `current_game` güncellenir
        - Oyun için klasör oluşturulur
        """
    ´´´

#Kullanım:

´´´

    New_Game.new_game("TerminalGame", networking=False)
    print(New_Game.current_game)
    # Output: ['TerminalGame', False]
´´´

💾 SaveSystem Class

Oyun verilerini JSON formatında kaydeder ve yükler.

Fonksiyonlar:

save_inventory(game_name, inventory, filename="inventory.json")              
Oyuncu envanterini kaydeder.

Parametreler:

game_name (str): Oyun adı

inventory (Inventory nesnesi):        Kaydedilecek envanter

filename (str, default=inventory.json):      Dosya adı

load_inventory(game_name, inventory, filename="inventory.json")
Daha önce kaydedilmiş envanteri yükler.
Eğer dosya yoksa, envanter boş atanır.

list_games(list_games=False, folders_path="database")
Klasördeki oyunları listeler.

Parametreler:

list_games (bool): True ise oyunları listeler

folders_path (str): Oyun klasörlerinin bulunduğu dizin

#Örnek Kullanım

    
    from engine import SaveSystem
    inventory = Inventory()
    SaveSystem.save_inventory("TerminalGame", inventory)
    SaveSystem.load_inventory("TerminalGame", inventory)
    SaveSystem.list_games(True)


#🐞debug_system Class

Debug mesajlarını yönetmek için statik bir sınıftır.

    debug_system.debug(arg, *game_types, debug=False)


arg: Herhangi bir bilgi mesajı (opsiyonel)

game_types: New_Game.game_types içinde kontrol edilecek tipler

debug (bool): Debug modunu aktif eder

#Örnek Kullanım:

    debug_system.debug("Game Info", "game name", "networking", debug=True)



Output:


    # Debug is active
    # <game name>: TerminalGame
    # <networking>: False


#🧠 RAMManager Class

RAM üzerinde hızlı veri depolamak ve erişmek için kullanılır.

    ram = RAMManager(size_kb=1024)  # 1 MB RAM allocate
    ram.store("player_data", b"example bytes")
    data = ram.load("player_data")


size_kb: RAM boyutu kilobayt cinsinden

store(key, data): RAM'e veri ekler

load(key): RAM'den veri okur

#🏗️ Behaviour Class

Tüm oyun nesneleri için temel davranış şablonu.

    class Behaviour:
    def awake(self): pass      # Nesne oluşturulduğunda çağrılır
    def start(self): pass      # Oyun başlatıldığında çağrılır
    def update(self, dt): pass # Her frame güncelleme
    def draw(self): pass       # Çizim yapılacaksa burada


#⏱️ GameLoop Class
    Oyun döngüsünü yönetir ve hedef FPS ile nesneleri çalıştırır.

#Önemli Fonksiyonlar:

add(obj)

Oyun nesnesi ekler ve awake fonksiyonunu çağırır.

run()

Oyun döngüsünü başlatır, nesneleri günceller ve çizim yapar.

stop()

Döngüyü durdurur.

#Parametreler:

target_fps (int): Hedef FPS, default 60

debug (bool): Debug mesajlarını aktif eder

#Örnek Kullanım:

    game_loop = GameLoop(target_fps=60, debug=True)

    class Player(Behaviour):
        def awake(self):
            print("Player Awake")
        def update(self, dt):
            print(f"Updating player, dt={dt}")

    player = Player()
    game_loop.add(player)
    game_loop.run()  # Ctrl+C ile durdurabilirsiniz veya game_loop.stop() ile


🔹 Özet

Bu framework ile:  
Yeni oyunlar başlatabilir (New_Game)  
Oyuncu envanterlerini kaydedip yükleyebilir (SaveSystem)  
RAM üzerinde geçici veri depolayabilirsiniz (RAMManager)  
Oyun nesnelerinin davranışlarını yönetebilirsiniz (Behaviour)  
Sabit FPS ile oyun döngüsü oluşturabilirsiniz (GameLoop)   
Debug mesajlarını kolayca takip edebilirsiniz (debug_system)

## Registry Documentation

🗂️ Registry Documentation  
Bu modül, oyun içindeki tüm item tanımlarını merkezi olarak saklamak için kullanılır.
Inventory, vanilla_items ve diğer sistemler bu sınıf üzerinden item doğrulaması yapar.  

🎯 Amaç  
Item’ları tek bir merkezde toplamak  
Inventory’ye yalnızca kayıtlı item’ların eklenmesini sağlamak  
Modüler ve genişletilebilir bir item altyapısı sunmak

🧱 Registry Class
    class Registry:
        items = {}

Açıklama:
Tüm item tanımları items sözlüğü içinde saklanır.

    Registry.items = {
        "game:stone": {
            "name": "Stone",
            "item_id": 1,
            "type": "block"
        }
    }


📌 Sınıf Özellikleri
| Özellik | Tip               | Açıklama                 |
| ------- | ----------------- | ------------------------ |
| `items` | `dict[str, dict]` | Item key → item metadata |

Registry stateful ve globaldir.  
Oyun çalıştığı sürece tüm item’lar bellekte tutulur.


➕ register_item

    @classmethod
    def register_item(cls, item_key: str, item_data: dict):


Açıklama  
Yeni bir item’ı Registry’ye kaydeder.  

Parametreler
| Parametre   | Tip    | Açıklama                                      |
| ----------- | ------ | --------------------------------------------- |
| `item_key`  | `str`  | Item’ın benzersiz anahtarı (`namespace:item`) |
| `item_data` | `dict` | Item metadata bilgileri                       |

Davranış  
Aynı item_key tekrar eklenirse üzerine yazar  
Hata fırlatmaz (bilinçli basit tasarım)

    Registry.register_item(
        "game:stone",
        {
            "name": "Stone",
            "item_id": 1,
            "type": "block"
        }
    )

🔍 get_item

    @classmethod
    def get_item(cls, item_key: str):

Açıklama  
Belirtilen item’ın metadata bilgisini döndürür.

Parametreler
| Parametre  | Tip   | Açıklama      |
| ---------- | ----- | ------------- |
| `item_key` | `str` | Item anahtarı |

Dönüş Değeri
| Durum      | Dönüş  |
| ---------- | ------ |
| Item varsa | `dict` |
| Item yoksa | `None` |

Örnek

    item = Registry.get_item("game:stone")

    print(item["name"])
OUTPUT:

    # Stone


✔️ has_item

    @classmethod
    def has_item(cls, item_key: str) -> bool:

Açıklama  
Bir item’ın Registry’de kayıtlı olup olmadığını kontrol eder. 

Parametreler
| Parametre  | Tip   | Açıklama                       |
| ---------- | ----- | ------------------------------ |
| `item_key` | `str` | Kontrol edilecek item anahtarı |

Dönüş Değeri
| Değer   | Açıklama           |
| ------- | ------------------ |
| `True`  | Item kayıtlı       |
| `False` | Item kayıtlı değil |


Örnek:

    Registry.has_item("game:stone")  # True
    Registry.has_item("game:diamond")  # False


🔗 Sistem Entegrasyonu  
Inventory

    if not Registry.has_item(item_key):
    print("[Inventory] Unknown item")


Vanilla Item Loader

    Registry.register_item("game:wood", {...})

## İTEMS Documentation


🧱 vanilla_items Documentation

Bu modül, oyunda varsayılan (vanilla) item’ların Registry sistemine kaydedilmesini sağlar. Oyun başlatılırken bir kez çağrılması gerekir.

🔗 Bağımlılıklar

    from engine.registry import Registry
Bu modül, item kayıt işlemleri için Registry sistemine bağımlıdır.


📦 load_vanilla_item Function
Tanım

    def load_vanilla_item():

Açıklama  
Oyunun temel (vanilla) item’larını Registry sistemine kaydeder.

Bu fonksiyon çağrılmadan önce:  
Inventory.add_item  
Inventory.set_item  
çalışmaz, çünkü item’lar Registry’de kayıtlı değildir.


🧾 Kayıt Edilen Item’lar
🪨 Stone

    Registry.register_item(
        "game:stone",
        {
            "name": "Stone",
            "item_id": 1,
            "type": "block"
        }
    )

| Alan      | Tip   | Açıklama            |
| --------- | ----- | ------------------- |
| `key`     | `str` | `"game:stone"`      |
| `name`    | `str` | Oyunda görünen ad   |
| `item_id` | `int` | Dahili benzersiz ID |
| `type`    | `str` | Item türü (`block`) |



▶️ Ne Zaman Çağrılmalı?  
Bu fonksiyon oyun başlatılırken, en erken aşamada çağrılmalıdır.  

Önerilen Akış

    from engine.ecosystem import New_Game
    from engine.items import load_vanilla_item
    from engine.inventory import Inventory

    New_Game.new_game("MyGame")
    load_vanilla_item()

    inv = Inventory()
    inv.add_item("game:stone", 5)

⚠️ Önemli Notlar  
Bu fonksiyon birden fazla kez çağrılmamalıdır  
Aynı item key’i tekrar register edilirse  
Registry ya hata fırlatmalı  
ya da overwrite etmemelidir (Registry implementasyonuna bağlı)




🔹 Özet  
✔ Oyunun temel item’larını yükler  
✔ Inventory ve SaveSystem ile tam uyumludur  
✔ Modüler item sistemine uygundur  
✔ Registry tabanlı güvenli tasarım
## İnventory Documentation

#📦 Inventory Documentation  
Bu modül, oyun içi item (eşya) yönetimini sağlar. Registry sistemi ile entegre çalışır ve yalnızca kayıtlı (registered) item’ların envantere eklenmesine izin verir.

#🔗 Bağımlılıklar
    from engine.registry import Registry

Inventory, item doğrulaması için Registry sistemine bağımlıdır.  
Registry.has_item(item_key) → item sistemde kayıtlı mı kontrol eder

🧱 Inventory Class  

Açıklama:  
Oyuncunun veya sistemin sahip olduğu item’ları tutar.
Item’lar dict yapısında saklanır.

    self.items = {
    "stone": 12,
    "wood": 5
    }


📌 Özellikler
| Özellik | Tip              | Açıklama             |
| ------- | ---------------- | -------------------- |
| `items` | `dict[str, int]` | Item anahtarı → adet |


➕ add_item

    def add_item(self, item_key: str, count=1) -> bool

Açıklama  
Belirtilen item’ı envantere ekler veya mevcutsa miktarını artırır.

#Parametreler

| Parametre  | Tip   | Açıklama                          |
| ---------- | ----- | --------------------------------- |
| `item_key` | `str` | Registry’de kayıtlı item anahtarı |
| `count`    | `int` | Eklenecek miktar (default: `1`)   |

Davranış  
Item Registry’de yoksa → eklenmez  
Item varsa → mevcut sayıya eklenir

| Değer   | Açıklama               |
| ------- | ---------------------- |
| `True`  | Item başarıyla eklendi |
| `False` | Item Registry’de yok   |

ÖRNEK:

    inv = Inventory()

    inv.add_item("stone", 3)
    inv.add_item("wood")

    print(inv.items)

OUTPUT:

    # {'stone': 3, 'wood': 1}

✏️ set_item

    def set_item(self, item_key: str, count: int) -> bool

Açıklama  
Bir item’ın miktarını doğrudan ayarlar.

Parametreler
| Parametre  | Tip   | Açıklama                 |
| ---------- | ----- | ------------------------ |
| `item_key` | `str` | Registry’de kayıtlı item |
| `count`    | `int` | Yeni miktar              |


Kurallar  
count > 0 → miktar ayarlanır  
count <= 0 → item envanterden silinir  
Item Registry’de yoksa işlem yapılmaz  
Dönüş Değeri
| Değer   | Açıklama             |
| ------- | -------------------- |
| `True`  | İşlem başarılı       |
| `False` | Item Registry’de yok |

Örnek

    inv.set_item("stone", 10)
    inv.set_item("wood", 0)

    print(inv.items)
OUTPUT:

    # {'stone': 10}



⚠️ Hata ve Uyarılar  
Registry’de olmayan bir item kullanılırsa:  

    [Inventory] Unknown item: diamond_sword



🧩 Registry ile Entegrasyon  
Bu sınıf Registry zorunlu olacak şekilde tasarlanmıştır.  
Beklenen Registry arayüzü:

    class Registry:
    @staticmethod
    def has_item(item_key: str) -> bool:
        ...


🧠 Tasarım Notları  
Inventory bilinçli olarak pasif tutulmuştur
(render, UI veya save işlemleri içermez)  
JSON ile kaydetmeye uygundur (SaveSystem ile tam uyumlu)  
Multiplayer veya server-side inventory için güvenlidir


🧪 Tipik Kullanım Akışı

    from engine.inventory import Inventory
    from engine.ecosystem import SaveSystem
    
    inv = Inventory()
    
    inv.add_item("stone", 5)
    inv.set_item("wood", 2)
    
    SaveSystem.save_inventory("MyGame", inv)

## UI Documentation

#🖨️ UIPrint Class  
UI ile entegre çalışan özel bir print sistemidir. Normal print gibi çalışır ancak sahne değiştiğinde veya element silindiğinde yazılar kaybolur.

    class UIPrint:
    def __init__(self):
        self.buffer = []  # Yazılar saklanır
        self.active_scene = None

    def set_scene(self, scene):
        """Aktif sahneyi belirler ve buffer’ı temizler."""
    
    def print(self, *args, **kwargs):
        """Yeni yazı ekler, sahne varsa UI'yi günceller."""
    
    def get_buffer(self):
        """Buffer'daki tüm yazıları listeler."""
    
    def clear(self):
        """Buffer'ı temizler ve UI'yi günceller."""
Örnek Kullanım:

    ui_print.print("Hello World")
    print(ui_print.get_buffer())  # ['Hello World']
    ui_print.clear()


⚡ UIElement Class

Tüm UI elementleri için temel sınıf.

    class UIElement:
    def __init__(self):
        self.visible = True
        self.ui = None
        self.focusable = False

    def draw(self, focused=False):
        pass

    def handle_input(self, input_type):
        pass

draw(focused=False): Elementi çizer.  

handle_input(input_type): Kullanıcı girdilerini işler.       



🔘 Button Class  
UIElement sınıfından türetilmiştir. Tıklanabilir buton sağlar.

    class Button(UIElement):
    def __init__(self, text, on_click):
        self.text = text
        self.on_click = on_click
        self.focusable = True

    def draw(self, focused=False):
        """Console üzerinde butonu çizer."""
    
    def handle_input(self, input_type):
        """Enter veya metin eşleşmesi ile on_click tetikler."""

#Örnek Kullanım:

    def click_action():
    print("Button clicked!")

    btn = Button("Play", click_action)
    btn.handle_input("enter")  # Çıktı: Button clicked!



🏷️ Label Class  
Sadece yazı göstermek için kullanılır.

    class Label(UIElement):
    def __init__(self, text):
        self.text = text

    def draw(self, focused=False):
        """Console üzerinde yazıyı çizer."""

🧩 UIManager Class  
UI elementlerini yönetir, odak ve input yönetimi sağlar.

    class UIManager:
    def __init__(self):
        self.elements = []
        self.focus_index = 0
        self.dirty = True
        self.input_buffer = None

    def add(self, element):
        """UI element ekler."""

    def update(self, dt):
        """Inputları kontrol eder ve UI'yi çizer."""

    def move_focus(self, direction):
        """Odaklanmış elementi değiştirir."""

    def get_focused_element(self):
        """Odaklanmış element döndürür."""

    def draw(self):
        """UI ve buffer yazılarını konsola çizer."""

    def feed_input(self, input_str):
        """Input'u UI sistemine besler."""


elements: UI elementlerinin listesi.  
dirty: Ekran güncellenmeli mi kontrolü.  
input_buffer: Kullanıcı girdisi bekler.  

Örnek Kullanım:

    ui_manager = UIManager()
    ui_manager.add(Button("Play", lambda: print("Clicked")))
    ui_manager.update(0.016)  # frame update



#🎬 Scene Class  
UIManager ile entegre sahne yönetimi sağlar.

    class Scene:
    def __init__(self, name):
        self.name = name
        self.ui_manager = UIManager()

    def enter(self):
        """Sahne aktif olur, UI buffer temizlenir."""

    def exit(self):
        """Sahneden çıkılır, buffer temizlenir."""

    def update(self, dt):
        """UIManager güncellemesi çağrılır."""


#🔄 SceneManager Class  
Sahne değişimlerini ve güncellemelerini yönetir.

    class SceneManager:
    def __init__(self):
        self.current_scene = None

    def change_scene(self, scene: Scene):
        """Mevcut sahneden çıkar ve yeni sahneye geçer."""

    def update(self, dt):
        """Aktif sahneyi günceller."""

    def feed_input(self, data):
        """Input'u sahneye gönderir."""

Örnek Kullanım:

    sm = SceneManager()
    scene1 = Scene("MainMenu")
    sm.change_scene(scene1)
    sm.feed_input("enter")
    sm.update(0.016)


#⌨️ Input Thread  
Konsoldan sürekli kullanıcı girişi almak için thread başlatır.

    def start_input_thread(scene_manager: SceneManager):
    """Sonsuz loop ile input alır ve sahneye besler."""


Thread daemon olarak çalışır, ana program kapanınca otomatik biter.


#🖥️ OPD2 Class  
OpenGL + GLFW ile pencere oluşturur ve frame yönetimi sağlar.

    class OPD2:
    def __init__(self, width, height, window_name):
        """
        Pencere oluşturur ve OpenGL context başlatır.
        Parameters:
        - width: Pencere genişliği
        - height: Pencere yüksekliği
        - window_name: Pencere başlığı
        """
    
    def begin_frame(self):
        """Yeni frame başlatır, arka plan rengini temizler."""
    
    def end_frame(self):
        """Frame sonlandırır, buffer swap ve event polling yapar."""
    
    def should_close(self):
        """Pencerenin kapanma durumu kontrol edilir."""
    
    def terminate(self):
        """GLFW ve pencereyi sonlandırır."""


Örnek Kullanım:

    window = OPD2(800, 600, "Demo")
    while not window.should_close():
        window.begin_frame()
        # OpenGL çizimleri
        window.end_frame()
    window.terminate()


🔹 Özet

Terminal tabanlı UI ve sahne yönetimi: UIPrint, UIElement, Button, Label, UIManager, Scene, SceneManager

Input yönetimi için thread desteği: start_input_thread

OpenGL ile pencere ve render yönetimi: OPD2

## GLELEMENTS Documentation

OpenGL + GLFW kullanılarak oluşturulmuş basit bir buton sınıfıdır. Pencere üzerinde tıklanabilir butonlar oluşturur ve renkli gösterim sağlar.


🖱️ GLButton Class

Tanım:

    class GLButton:
    def __init__(self, x, y, w, h, color, on_click):
        
Açıklama:
Bu sınıf, OpenGL üzerinde bir dikdörtgen buton oluşturur ve kullanıcı tıklamalarını algılar. update fonksiyonu ile mouse hareketlerini ve tıklamaları takip eder, draw fonksiyonu ile butonu ekrana çizer.

#Parametreler

| Parametre  | Tip      | Açıklama                                 |
| ---------- | -------- | ---------------------------------------- |
| `x`        | float    | Butonun sol üst X koordinatı             |
| `y`        | float    | Butonun sol üst Y koordinatı             |
| `w`        | float    | Butonun genişliği                        |
| `h`        | float    | Butonun yüksekliği                       |
| `color`    | tuple    | RGB renk, örn: `(1.0, 0.0, 0.0)` kırmızı |
| `on_click` | function | Butona tıklanınca çalışacak fonksiyon    |



#Fonksiyonlar  
1️⃣ update(window)

    def update(self, window):
    ...

Açıklama:
Mouse pozisyonunu ve tıklamayı kontrol eder. Eğer kullanıcı butona tıklarsa, on_click fonksiyonunu çağırır.

Parametreler:

| Parametre | Tip                | Açıklama                     |
| --------- | ------------------ | ---------------------------- |
| `window`  | GLFW window object | Butonun bağlı olduğu pencere |

İşleyiş:

glfw.get_cursor_pos(window)  ile mouse pozisyonunu alır.  
Mouse Y eksenini düzeltir (GLFW'de üst sol orijin, OpenGL’de alt sol orijin).  
Butonun üzerine gelinip gelinmediğini kontrol eder.  
Sol fare tuşuna basıldığında on_click çağrılır ve pressed durumu güncellenir.

2️⃣ draw()

    def draw(self):
    ...

Açıklama:
Butonu OpenGL üzerinde dikdörtgen olarak çizer. Renk, sınıfın color parametresinden alınır.  
İşleyiş:  
glColor3f(*self.color) ile renk ayarlanır.  
glBegin(GL_QUADS) ve glVertex2f ile dört köşe çizilir.  
glEnd() ile çizim tamamlanır.

#Örnek Kullanım

    import glfw
    from OpenGL.GL import *
    from glbutton import GLButton  # GLButton sınıfınızın bulunduğu dosya

    def on_button_click():
        print("Button clicked!")

    # GLFW başlatma
    if not glfw.init():
        exit()

    window = glfw.create_window(800, 600, "GLButton Demo", None, None)
    glfw.make_context_current(window)

    # Buton oluştur
    button = GLButton(100, 100, 200, 50, (0.0, 1.0, 0.0), on_button_click)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        button.update(window)
        button.draw()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

Önemli Notlar  
GLButton sadece 2D dikdörtgen butonlar için uygundur.  
Y ekseni OpenGL’de alt sol orijin olduğu için update() fonksiyonu mouse Y pozisyonunu düzeltir.   
on_click fonksiyonu bloklayıcı olmamalıdır, çünkü her frame çağrılır.

## 🌐 network Documentation

Bu modül, oyunun ağ (network) tarafı için temel bir TCP server oluşturmayı sağlar.  
Basit ve öğrenme odaklı bir yapı sunar, küçük ölçekli multiplayer denemeleri için uygundur.

🔗 Bağımlılıklar

    import socket
    import requests

⚠️ requests şu an kullanılmıyor, ileride:  
public IP alma  
master server’a kayıt  
HTTP tabanlı handshake  
gibi işlemler için düşünüldü


🧱 network Class  
Bu sınıf state tutmaz, tüm işlemler @classmethod ile yapılır.

🛠️ create_server

    @classmethod
    def create_server(
        cls,
        server_ip,
        port,
        max_player=None,
        debug=True
    )


Açıklama  
Belirtilen IP ve port üzerinde TCP server oluşturur ve ilk client bağlantısını kabul eder.

📥 Parametreler
| Parametre    | Tip           | Açıklama                           |
| ------------ | ------------- | ---------------------------------- |
| `server_ip`  | `str`         | Server’ın bind edileceği IP adresi |
| `port`       | `int`         | Dinlenecek port                    |
| `max_player` | `int \| None` | Maksimum oyuncu sayısı (1–4)       |
| `debug`      | `bool`        | Debug çıktıları aktif mi           |


⚙️ Varsayılan Davranışlar  
max_player = None → otomatik 4  
max_player aralığı: 1–4  
Aksi halde ValueError fırlatılır

    if not 1 <= max_player < 5:
    raise ValueError("max_player 1 ile 4 arasında olmalı")

🐞 Debug Modu
Debug = True

    Debug: Debug is True
    Server Ip: 127.0.0.1
    Max Player: 4
    Waiting Players


Debug = False

    Debug: Debug is False


🔌 Server Akışı  
TCP socket oluşturulur  
IP ve port’a bind edilir  
Dinlemeye geçilir  
İlk client bağlantısı kabul edilir


    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, port))
    server.listen()

    client, addr = server.accept()
    print("Connection request from", addr)


⚠️ Şu an:  
sadece 1 client kabul edilir  
max_player henüz gerçek anlamda kullanılmıyor

▶️ Örnek Kullanım

    from engine.network import network

    network.create_server(
        server_ip="127.0.0.1",
        port=5555,
        max_player=2,
        debug=True
    )














## ReadMe And Some Technical information


# ENGLISH

# 🛠️ CRAVEXI CORE — Game Engine

CravexiCore is a Python-based **high-performance Terminal (CLI)** game and **modern OpenGL (GUI)** application hybrid engine.

---

## 📖 What is CravexiCore?

CravexiCore is a core designed to minimize repetitive boilerplate code in game development. It focuses on **low RAM usage**, **flexible save system**, and **rapid prototyping**.

### Use Cases

* **Retro-Style Games:** Terminal-based RPG or strategy games
* **Modern 2D/3D Apps:** OpenGL-based graphical interfaces
* **Data-Driven Simulations:** Large datasets with optimized RAM management
* **Multiplayer Testing:** Built-in TCP infrastructure for multiplayer trials

---

## ✨ Features

### 🛠️ 1. Architecture Features

* **Hybrid Engine Core:** Run CLI or OpenGL GUI with the same codebase
* **Unity-Style Behaviour System:** `awake`, `start`, `update`, `draw` lifecycle
* **Automatic Project Scaffolding:** Auto folder structure with `New_Game`

### 🚀 2. Performance and Memory

* **RAMManager:** RAM buffering instead of disk I/O
* **Delta Time (dt):** FPS-independent game flow
* **Target FPS Control:** CPU usage optimization

### 🎨 3. UI / UX

* **GLELEMENTS:** Easy UI components on OpenGL
* **Event-Based UI:** Events like `on_click`
* **Responsive Coordinates:** Normalized position system

### 💾 4. Data and Networking

* **Registry:** Centralized entity registry
* **JSON SaveSystem:** One-line save/load
* **TCP Network Driver:** Asynchronous server-client architecture

---

## 📘 Lessons Learned

### 🏗️ 1. Starting a Project — `New_Game`

```python
from ecosystem import New_Game

# Creates a networkless project named "DragonHunt"
New_Game.new_game("DragonHunt", networking=False)
```

---

### 🔄 2. Object System — `Behaviour`

```python
from ecosystem import Behaviour

class Enemy(Behaviour):
    def start(self):
        self.health = 100

    def update(self, dt):
        self.health -= 5 * dt
```

---

### 🧠 3. Memory Management — `RAMManager`

```python
from ecosystem import RAMManager

memory = RAMManager(size_kb=2048)
memory.store("high_score", 5000)
score = memory.load("high_score")
```

---

### 🎨 4. OpenGL UI — `GUIS` & `GLELEMENTS`

```python
from GUIS import OPD2
from GLELEMENTS import GLButton

window = OPD2(800, 600, "Cravexi Window")

def say_hello():
    print("Hello Player!")

btn = GLButton(
    x=0,
    y=0,
    w=0.2,
    h=0.1,
    color=(1, 0, 0),
    on_click=say_hello
)
```

---

### 📦 5. Registry & SaveSystem

```python
from registry import Registry
from ecosystem import SaveSystem

Registry.register_item("Flame_Sword", {"damage": 45, "price": 100})

inventory = ["Flame_Sword", "Shield"]
SaveSystem.save_inventory("DragonHunt", inventory)
```

---

### 🌐 6. Networking

```python
from network_driver import create_server

create_server("127.0.0.1", 5555, 10)
```

---

## 🕹️ Demo Games

### 🖥️ Terminal-Based Game

```python
from engine.ecosystem import GameLoop, Behaviour, New_Game, SaveSystem
from engine.inventory import Inventory
from engine.items import load_vanilla_item
from engine.GUIS import Scene, Button, SceneManager, start_input_thread, Label

New_Game.new_game("TerminalGame", networking=False)
load_vanilla_item()

inventory = Inventory()
SaveSystem.load_inventory("TerminalGame", inventory)

scene_manager = SceneManager()
menu = Scene("Menu")

info_label = Label("No stones collected yet")

def collect_stone():
    inventory.add_item("game:stone", 1)
    count = inventory.items.get("game:stone", 0)
    info_label.text = f"[+] Collected stones x{count}"

def save_and_exit():
    SaveSystem.save_inventory("TerminalGame", inventory)
    info_label.text = "[✓] Game saved. Exiting..."
    exit()

menu.ui_manager.add(info_label)
menu.ui_manager.add(Button("Collect Stone", collect_stone))
menu.ui_manager.add(Button("Save & Exit", save_and_exit))

class TerminalGame(Behaviour):
    def update(self, dt):
        scene_manager.update(dt)

start_input_thread(scene_manager)
scene_manager.change_scene(menu)

loop = GameLoop()
loop.add(TerminalGame())

try:
    loop.run()
finally:
    SaveSystem.save_inventory("TerminalGame", inventory)
```

> In this game, selecting **Collect Stone** or **Save & Exit** saves the stone count to `database/TerminalGame/*.json`.

![Cravexi Core Preview](assets/terminal1.png)

![Cravexi Core Preview](assets/terminal2.png)

![Cravexi Core Preview](assets/terminal3.png)

---

### 🪟 OpenGL-Based Game

```python
from engine.GUIS import OPD2
from engine.GLELEMENTS import GLButton

click_count = 0

def on_click():
    global click_count
    click_count += 1
    print("Click count:", click_count)

app = OPD2(600, 400, "OpenGL Game")

button = GLButton(
    200, 150,
    200, 80,
    (0.1, 0.7, 0.3),
    on_click
)

while not app.should_close():
    app.begin_frame()
    button.update(app.window)
    button.draw()
    app.end_frame()

app.terminate()
```

> Each click prints **click count** in the terminal.

![Cravexi Core Preview](assets/openglgame.png)













# TURKİSH

# 🛠️ CRAVEXİ CORE — Game Engine

CravexiCore, Python tabanlı **yüksek performanslı Terminal (CLI)** oyunları ve **modern OpenGL (GUI)** uygulamaları geliştirmek için tasarlanmış **hibrit bir oyun motorudur**.

---

## 📖 CravexiCore Nedir?

CravexiCore, oyun geliştirme sürecindeki karmaşık *boilerplate* (tekrarlayan kod) kısımlarını minimize eden bir çekirdektir. Özellikle **düşük RAM kullanımı**, **esnek kayıt sistemi** ve **hızlı prototipleme** odaklıdır.

### Kullanım Alanları

* **Retro Tarzı Oyunlar:** Terminal tabanlı RPG veya strateji oyunları
* **Modern 2D/3D Uygulamalar:** OpenGL tabanlı grafiksel arayüzler
* **Veri Odaklı Simülasyonlar:** Optimize RAM yönetimi ile büyük veri setleri
* **Çok Oyunculu Testler:** Yerleşik TCP altyapısı ile multiplayer denemeleri

---

## ✨ Features

### 🛠️ 1. Mimari Özellikler

* **Hybrid Engine Core:** Aynı kod tabanı ile CLI veya OpenGL GUI çalıştırma
* **Unity-Style Behaviour System:** `awake`, `start`, `update`, `draw` yaşam döngüsü
* **Automatic Project Scaffolding:** `New_Game` ile otomatik klasör yapısı

### 🚀 2. Performans ve Bellek

* **RAMManager:** Disk I/O yerine RAM tamponlama
* **Delta Time (dt):** FPS bağımsız oyun akışı
* **Target FPS Control:** CPU kullanım optimizasyonu

### 🎨 3. UI / UX

* **GLELEMENTS:** OpenGL üzerinde kolay UI bileşenleri
* **Event-Based UI:** `on_click` gibi olaylar
* **Responsive Koordinatlar:** Normalize edilmiş pozisyon sistemi

### 💾 4. Veri ve Ağ

* **Registry:** Merkezi varlık kaydı
* **JSON SaveSystem:** Tek satırda kayıt / yükleme
* **TCP Network Driver:** Asenkron sunucu–istemci mimarisi

---

## 📘 Lessons Learned

### 🏗️ 1. Projeyi Başlatmak — `New_Game`

```python
from ecosystem import New_Game

# "EjderhaAvı" adında, ağsız bir proje oluşturur
New_Game.new_game("EjderhaAvı", networking=False)
```

---

### 🔄 2. Nesne Sistemi — `Behaviour`

```python
from ecosystem import Behaviour

class Dusman(Behaviour):
    def start(self):
        self.can = 100

    def update(self, dt):
        self.can -= 5 * dt
```

---

### 🧠 3. Bellek Yönetimi — `RAMManager`

```python
from ecosystem import RAMManager

hafiza = RAMManager(size_kb=2048)
hafiza.store("yuksek_skor", 5000)
skor = hafiza.load("yuksek_skor")
```

---

### 🎨 4. OpenGL Arayüz — `GUIS` & `GLELEMENTS`

```python
from GUIS import OPD2
from GLELEMENTS import GLButton

pencere = OPD2(800, 600, "Cravexi Penceresi")

def selam_ver():
    print("Merhaba Oyuncu!")

btn = GLButton(
    x=0,
    y=0,
    w=0.2,
    h=0.1,
    color=(1, 0, 0),
    on_click=selam_ver
)
```

---

### 📦 5. Registry & SaveSystem

```python
from registry import Registry
from ecosystem import SaveSystem

Registry.register_item("Alev_Kilici", {"hasar": 45, "fiyat": 100})

envanter = ["Alev_Kilici", "Kalkan"]
SaveSystem.save_inventory("EjderhaAvı", envanter)
```

---

### 🌐 6. Ağ Sistemi

```python
from network_driver import create_server

create_server("127.0.0.1", 5555, 10)
```

---

## 🕹️ Demo Oyunlar

### 🖥️ Terminal Tabanlı Oyun

```python
from engine.ecosystem import GameLoop, Behaviour, New_Game, SaveSystem
from engine.inventory import Inventory
from engine.items import load_vanilla_item
from engine.GUIS import Scene, Button, SceneManager, start_input_thread, Label

New_Game.new_game("TerminalGame", networking=False)
load_vanilla_item()

inventory = Inventory()
SaveSystem.load_inventory("TerminalGame", inventory)

scene_manager = SceneManager()
menu = Scene("Menu")

info_label = Label("Henüz taş toplanmadı")

def collect_stone():
    inventory.add_item("game:stone", 1)
    count = inventory.items.get("game:stone", 0)
    info_label.text = f"[+] Taş toplandı x{count}"

def save_and_exit():
    SaveSystem.save_inventory("TerminalGame", inventory)
    info_label.text = "[✓] Oyun kaydedildi. Çıkılıyor..."
    exit()

menu.ui_manager.add(info_label)
menu.ui_manager.add(Button("Taş Topla", collect_stone))
menu.ui_manager.add(Button("Kaydet & Çık", save_and_exit))

class TerminalGame(Behaviour):
    def update(self, dt):
        scene_manager.update(dt)

start_input_thread(scene_manager)
scene_manager.change_scene(menu)

loop = GameLoop()
loop.add(TerminalGame())

try:
    loop.run()
finally:
    SaveSystem.save_inventory("TerminalGame", inventory)
```

> Bu oyunda **Taş Topla** veya **Kaydet & Çık** seçildiğinde `database/TerminalGame/*.json` dosyasına taş sayısı kaydedilir.
>
> 
> ![Cravexi Core Preview](assets/terminal1.png)




> ![Cravexi Core Preview](assets/terminal2.png)




> ![Cravexi Core Preview](assets/terminal3.png)
---

### 🪟 OpenGL Tabanlı Oyun

```python
from engine.GUIS import OPD2
from engine.GLELEMENTS import GLButton

click_count = 0

def on_click():
    global click_count
    click_count += 1
    print("Tıklama sayısı:", click_count)

app = OPD2(600, 400, "OpenGL Game")

button = GLButton(
    200, 150,
    200, 80,
    (0.1, 0.7, 0.3),
    on_click
)

while not app.should_close():
    app.begin_frame()
    button.update(app.window)
    button.draw()
    app.end_frame()

app.terminate()
```

> Butona her tıklamada terminal çıktısı olarak **tıklama sayısı** yazdırılır.

![Cravexi Core Preview](assets/openglgame.png)

