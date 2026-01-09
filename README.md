🛠️ CravexiCore
A High-Performance Hybrid Game Engine for Python

CravexiCore, Python tabanlı hem Terminal (CLI) hem de OpenGL (GUI) projeleri için tasarlanmış hibrit bir oyun motorudur. Unity-benzeri yaşam döngüsü (Behaviour) ve optimize edilmiş bellek yönetimi (RAMManager) ile geliştiricilere esnek bir çalışma alanı sunar.

🚀 Öne Çıkan Özellikler
Hibrit Arayüz: Aynı çekirdek üzerinde hem CLI hem de OpenGL desteği.

Optimize Bellek: RAMManager ile düşük gecikmeli veri işleme.

Modüler Mimari: Bağımsız çalışan Network, Save ve UI sistemleri.

Hızlı Prototipleme: Saniyeler içinde yeni proje dizini oluşturma.

🏗️ Mimari Yapı
CravexiCore beş ana sütun üzerine inşa edilmiştir:
Modül,Görev
Game Core,Sahne yönetimi ve GameLoop kontrolü.
UI Layer,OpenGL ve Terminal tabanlı hibrit bileşenler.
Data System,JSON tabanlı Save/Load ve Envanter yönetimi.
Memory Manager,Disk I/O yükünü azaltan RAM tamponlama.
Networking,TCP tabanlı hafif siklet çok oyunculu altyapısı.

🛠️ Kurulum ve Başlangıç
1. Yeni Proje Oluşturma
Motorun kalbi olan ecosystem, proje dosyalarını sizin için otomatik olarak hazırlar.

Python

from ecosystem import New_Game

# Otomatik klasör yapısı ve veritabanı kurulumu
New_Game.new_game("MyEpicProject", networking=True)
2. Yaşam Döngüsü (Behaviour)
Tüm oyun nesneleri Behaviour sınıfından türetilir. Bu, nesnenin doğuşundan ölümüne kadar tam kontrol sağlar.

Python

from ecosystem import Behaviour

class Player(Behaviour):
    def awake(self):
        # Kaynak yükleme işlemleri
        self.health = 100

    def update(self, dt):
        # Kare başına mantıksal hesaplamalar
        print(f"Delta Time: {dt}")

    def draw(self):
        # OpenGL çizim komutları
        pass
🖥️ Grafik ve Kullanıcı Arayüzü
OpenGL UI Elementleri
GLELEMENTS modülü ile modern ve etkileşimli arayüzler tasarlayın.

Python

from GLELEMENTS import GLButton
from GUIS import OPD2

def on_click():
    print("Sistem Aktif!")

# Buton Oluşturma
btn = GLButton(x=0.5, y=0.5, w=0.2, h=0.1, color=(0.2, 0.6, 1), on_click=on_click)
💾 Veri Yönetimi
RAMManager & SaveSystem
Performans için verileri RAM'de tutun, kalıcılık için JSON olarak diske yazın.

Python

from ecosystem import RAMManager, SaveSystem

# Bellek Yönetimi
memory = RAMManager(size_kb=2048)
memory.store("player_pos", [10, 20])

# Kalıcı Kayıt
SaveSystem.save_inventory("SpaceQuest", player_items)
🌐 Network Modülü
Basit TCP sunucu yapısı ile çok oyunculu desteği eklemek çok kolay:

Python

from network_driver import create_server

# 4 oyunculu yerel sunucu başlatma
create_server(server_ip="127.0.0.1", port=5555, max_player=4)
📋 Örnek Boilerplate (Hızlı Başlangıç)
Python

from ecosystem import GameLoop
from my_entities import Player

# Motoru Başlat
game = GameLoop(target_fps=60, debug=True)

# Karakteri Ekle
hero = Player()
game.add(hero)

# Döngüyü Çalıştır
game.run()
🤝 Katkıda Bulunma
Bu depoyu çatallayın (Fork).

Yeni bir özellik dalı (Branch) açın.

Değişikliklerinizi kaydedin (Commit).

Bir Pull Request gönderin.

CravexiCore ile neler inşa edeceğinizi görmek için sabırsızlanıyoruz! 🚀
