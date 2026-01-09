                                    🛠️CRAVEXİ CORE:Game Engine
                
CravexiCore, Python tabanlı hem yüksek performanslı Terminal (CLI) oyunları hem de modern OpenGL (GUI) uygulamaları geliştirmek için tasarlanmış hibrit bir oyun motorudur.

📖 CravexiCore Nedir?
CravexiCore, oyun geliştirme sürecindeki karmaşık "boilerplate" (tekrarlayan kod) kısımlarını minimize eden bir çekirdektir. Özellikle Düşük RAM kullanımı, Esnek Kayıt Sistemi ve Hızlı Prototipleme odaklıdır.

Kullanım Alanları:
Retro Tarzı Oyunlar: Terminal tabanlı RPG veya strateji oyunları.

Modern 2D/3D Uygulamalar: OpenGL tabanlı grafiksel arayüzler.

Veri Odaklı Simülasyonlar: Optimize edilmiş RAM yönetimi sayesinde büyük veri setleri.

Çok Oyunculu Testler: Yerleşik TCP sunucu altyapısı ile multiplayer denemeleri.



## Features

🛠️ 1. Mimari Özellikler (Mutfak Tarafı)
CravexiCore, geliştiricinin kod yazarken boğulmasını engelleyen katmanlı bir yapı sunar.

Hybrid Engine Core: Motorun en büyük farkı budur. Kodunuzu bir kez yazarsınız; isterseniz bir terminal penceresinde (CLI), isterseniz yüksek performanslı bir OpenGL penceresinde (GUI) çalıştırırsınız.

Unity-Style Behaviour System: Nesnelerin bir yaşam döngüsü vardır. awake, start, update ve draw metodları sayesinde kodun nerede çalışacağı bellidir, "spaghetti kod" oluşmasını engeller.

Automatic Project Scaffolding: New_Game fonksiyonu ile tüm klasör yapısı (database, assets, logs vb.) saniyeler içinde otomatik kurulur.

🚀 2. Performans ve Bellek Özellikleri
Python'un doğası gereği ağır kalabildiği yerlerde CravexiCore devreye girer:

RAMManager (Varlık Tamponlama): Disk üzerindeki dosyaları (JSON, Text, Binary) sürekli okuyup sistemi yormak yerine, bu verileri RAM'de ayrılmış özel bir alanda tutar. Bu, I/O işlemlerini %80-90 oranında hızlandırır.

Delta Time (dt) Entegrasyonu: Oyunun hızı bilgisayarın performansına bağlı kalmaz. $Hiz \times dt$ formülü ile oyun 30 FPS'de de 144 FPS'de de aynı hızda akar.

Target FPS Control: İşlemci kullanımını optimize etmek için kare hızını sabitleyebilirsiniz (Örn: 60 FPS).

🎨 3. Görsel ve Kullanıcı Deneyimi (UI/UX)
Grafik tarafında modern ve hafif araçlar sunar:

GLELEMENTS: OpenGL üzerinde koordinat hesabı yapmanıza gerek kalmadan; buton, panel ve metin alanları oluşturmanıza izin verir.

Olay Odaklı (Event-Based) UI: Butonlara on_click gibi parametreler atayarak, bir tıklama gerçekleştiğinde hangi fonksiyonun çalışacağını kolayca belirleyebilirsiniz.

Responsive Koordinatlar: OpenGL'in -1 ile 1 arasındaki karmaşık sistemini daha anlaşılır (genelde 0-1 arası normalize) hale getiren yardımcı araçlar içerir.

💾 4. Veri ve Ağ (Networking) Özellikleri
Oyunun dünyasını ve oyuncu ilerlemesini yönetmek için yerleşik modüllere sahiptir:

Registry (Merkezi Kayıt): Oyundaki her eşya (kılıç, iksir, düşman tipi) bir kez kaydedilir. Bu, bellekte aynı verinin defalarca kopyalanmasını önler.

JSON SaveSystem: Karmaşık oyuncu verilerini (envanter, yetenekler vb.) tek satırda kaydedip geri yükleyebilir.

TCP Network Driver: Multiplayer projeler için asenkron (eşzamanlı olmayan) bir sunucu-istemci mimarisi sunar. create_server parametresi ile anında sunucu ayağa kalkar.

💡 Özetle CravexiCore:
Eğer hızlı prototipleme yapmak istiyorsan, bellek yönetimini dert etmeden Python ile profesyonel bir oyun mimarisi kurmak istiyorsan CravexiCore tam sana göre. Hem nostaljik terminal oyunları hem de modern grafikli uygulamalar için tek bir çekirdek!

## Lessons Learned

🏗️ 1. Projeyi Başlatmak: New_Game
Her şey bir klasör yapısıyla başlar. CravexiCore senin için tüm dosyaları otomatik oluşturur.

New_Game.new_game(name, networking)
name (İsim): Oyununun klasör adı. (Örn: "UzaySavasi")

networking (Ağ): Eğer oyunun online olacaksa True, olmayacaksa False yapmalısın.

Örnek:
from ecosystem import New_Game
# "EjderhaAvı" adında, internet desteği olmayan bir proje oluşturur.
New_Game.new_game("EjderhaAvı", networking=False)


🔄 2. Nesne Oluşturma: Behaviour
Oyunundaki her şey (oyuncu, düşman, mermi) bir nesnedir. Bu nesnelerin bir hayat hikayesi (Yaşam Döngüsü) vardır.

Ana Metotlar ve Parametreler:
awake(self): Nesne doğduğu an çalışır. (Henüz ekranda değildir).


start(self): Oyun başlamadan hemen önce 1 kez çalışır.


update(self, dt): Oyun çalıştığı sürece sürekli döner.


dt (Delta Time): En önemli parametre! Bilgisayarın hızı ne olursa olsun, karakterin her zaman aynı hızda gitmesini sağlar.

draw(self): Nesnenin ekrana çizilme komutlarını içerir.

Örnek:


from ecosystem import Behaviour

class Dusman(Behaviour):
    def start(self):
        self.can = 100  # Başlangıç canı

    def update(self, dt):
        # Dusman her karede 5 birim canı azalır 
        self.can -= 5 * dt 


🧠 3. Bellek Yönetimi: RAMManager
Bilgisayarlar dosyaları diskten yavaş okur, RAM'den hızlı okur. CravexiCore verilerini RAM'de saklayarak oyununu hızlandırır.

RAMManager(size_kb)
size_kb: RAM'de ne kadar yer ayıracağını belirler (Örn: 1024 = 1MB).

Örnek:


from ecosystem import RAMManager

hafiza = RAMManager(size_kb=2048) # 2MB yer ayır
hafiza.store("yuksek_skor", 5000) # Veriyi sakla
skor = hafiza.load("yuksek_skor") # Veriyi oku



🎨 4. Görsel Arayüz: GUIS ve GLELEMENTS
Oyunun penceresini açmak ve içine butonlar koymak için kullanılır.

OPD2(width, height, window_name)
width / height: Pencerenin genişliği ve yüksekliği.

window_name: Pencerenin üstünde yazacak isim.

GLButton(x, y, w, h, color, on_click)
x, y: Ekran konumu (-1 ile 1 arası).

w, h: Genişlik ve yükseklik.

color: Renk (RGB). Örn: (0, 0, 1) Mavidir.

on_click: Butona basınca hangi fonksiyon çalışsın?

Örnek:

from GUIS import OPD2
from GLELEMENTS import GLButton

pencere = OPD2(800, 600, "Cravexi Penceresi")

def selam_ver():
    print("Merhaba Oyuncu!")

# Ekranın ortasında kırmızı bir buton
btn = GLButton(x=0, y=0, w=0.2, h=0.1, color=(1, 0, 0), on_click=selam_ver)



📦 5. Veritabanı ve Kayıt: Registry & SaveSystem
Eşyaları tanımlamak ve oyuncunun ilerlemesini kaydetmek için kullanılır.

Registry.register_item(id, data)
id: Eşyanın adı.

data: Eşyanın özellikleri (Sözlük/Dict formatında).

SaveSystem.save_inventory(project_name, data)

project_name: Hangi oyunun dosyasına kaydedilsin?

data: Kaydedilecek bilgiler.

Örnek:


from registry import Registry
from ecosystem import SaveSystem

# 1. Eşyayı tanımla
Registry.register_item("Alev_Kilici", {"hasar": 45, "fiyat": 100})

# 2. Oyuncunun envanterini dosyaya kaydet
envanter = ["Alev_Kilici", "Kalkan"]
SaveSystem.save_inventory("EjderhaAvı", envanter)



🌐 6. Ağ Sistemi: network_driver
Çok oyunculu oyunlar için sunucu kurmanı sağlar.

create_server(server_ip, port, max_player)

server_ip: Sunucu adresi (Genelde "127.0.0.1").

port: Kapı numarası (Örn: 5555).

max_player: Kaç kişi bağlanabilir?

Örnek:

from network_driver import create_server

# 10 kişilik bir sunucu başlatır
create_server("127.0.0.1", 5555, 10)

🚀 Özet: Tam Bir Oyun Döngüsü Nasıl Görünür?

from ecosystem import GameLoop
from my_entities import Player # Kendi oluşturduğun oyuncu sınıfı

# 1. Motoru kur (Saniyede 60 kare çalış, debug modunu aç)
game = GameLoop(target_fps=60, debug=True)

# 2. Nesneyi ekle
oyuncu = Player()
game.add(oyuncu)

# 3. Oyunu başlat!
game.run()📝 CravexiCore ile Basit Örnek Oyun Projesi



TERMİNAL TABANLI OYUN:

from engine.ecosystem import GameLoop, Behaviour, New_Game, SaveSystem
from engine.inventory import Inventory
from engine.items import load_vanilla_item
from engine.GUIS import Scene, Button, SceneManager, start_input_thread, Label


# -------------------- GAME SETUP --------------------

New_Game.new_game("TerminalGame", networking=False)
load_vanilla_item()

inventory = Inventory()
SaveSystem.load_inventory("TerminalGame", inventory)


# -------------------- SCENE SETUP --------------------

scene_manager = SceneManager()
menu = Scene("Menu")

info_label = Label("Henüz taş toplanmadı")


def collect_stone():
    inventory.add_item("game:stone", 1)

    stone_count = inventory.items.get("game:stone", 0)
    info_label.text = f"[+] Taş toplandı x{stone_count}"


def save_and_exit():
    SaveSystem.save_inventory("TerminalGame", inventory)
    info_label.text = "[✓] Oyun kaydedildi. Çıkılıyor..."
    exit()


menu.ui_manager.add(info_label)
menu.ui_manager.add(Button("Taş Topla", collect_stone))
menu.ui_manager.add(Button("Kaydet & Çık", save_and_exit))


# -------------------- GAME LOOP --------------------

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




bu oyunda taş topla dediğiniz zaman ve kaydet ve çık dediğiniz zaman
database klasöründe TerminalGame adlı bir klasör oluşuyor ordaki .jsona toplaıdğınız taş sayısı kayıt ediliyor   



OPENGL Tabanlı:
from engine.GUIS import OPD2
from engine.GLELEMENTS import GLButton


click_count = 0


def on_click():
    global click_count
    click_count += 1
    print("Tıklama sayısı:", click_count)


app = OPD2(600, 400, "OpenGL Game")

button = GLButton(
    200, 150,          # x, y
    200, 80,           # width, height
    (0.1, 0.7, 0.3),   # color (RGB)
    on_click
)


while not app.should_close():
    app.begin_frame()

    button.update(app.window)
    button.draw()

    app.end_frame()


app.terminate()


bu kodda butona tıklayınca output olarak tıklandı: tıklama yasısı çıkıyor