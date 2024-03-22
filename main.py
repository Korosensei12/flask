from flask import Flask,render_template
import random
import string

app = Flask(__name__)

def sifreolusturma(length=12):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    şifre = ''.join(random.choice(karakterler) for _ in range(length))
    return şifre 

@app.route("/")
def hello_world():
    return "<h1>Merhabalar!</h1> <a href='/gercekler'>Rastgele gercekler! </a> <a href='/deneme'>Deneme! </a> </a> <a href='/4'>Dört! </a> <a href='/tools'>Araçlar! </a>"  

@app.route("/deneme")
def deneme():
    return "<h1> Bu bir denemedir.</h1> <a href='/gercekler'>Rastgele gercekler! </a> <a href='/'>Ana sayfa! </a>"

@app.route("/gercekler")
def gercekler():
    gercekler=["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
           "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
           "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
           "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
           "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
           "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
           "Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor",
           "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."
    
]
    return f"<h1> İşte size bir kaç rastgele gerçek! </h1> <p>{random.choice(gercekler)}</p> <a href='/'>Ana sayfa! </a>"
    
@app.route("/4")
def dort():
    return render_template("index.html")

@app.route("/tools")
def oyun():
    return "<a href='/yazitura'>Yazı Tura </a> <a href='/sifre'>Şifre oluşturucu </a> <a href='/resim'>Resimler </a> <a href='/'>Ana Sayfa </a>"

@app.route("/yazitura")
def yazitura():
    return f"<h1> İşte sonuç! </h1> <p>{random.choice(['Yazı', 'Tura'])}</p> <a href='/sifre'> Şifre oluşturucu </a> <a href='/resim'> Resimler </a> <a href='/'> Ana Sayfa </a>"

@app.route("/sifre")
def sifre():
    return f"<h1> İşte şifreniz! </h1> {sifreolusturma(12)}"        



if __name__ == "__main__":
    app.run(debug=True)
