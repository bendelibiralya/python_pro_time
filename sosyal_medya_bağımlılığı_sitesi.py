from flask import Flask
import random

app = Flask(__name__)
facts_list = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
"2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
"Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.", 
"2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
"Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
"Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
"Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.",
"Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]
yazimi_turami = [ "Yazı!", "Tura!"]
@app.route("/")
def hello_world():
    return '<h1>Facts about social media addiction!</h1> <a href="/rastgele_bilgi"> Sosyal medya bağımlılığı hakkkında rastgele bir gerçeği görüntüle!</a> <a href="/yazi_tura"> Yazı tura oyna!</a>'

@app.route("/yazi_tura")
def yazi_tura():
    return f'<h1>{random.choice(yazimi_turami)}</h1> <a href="/"> <img src ="https://www.webtekno.com/images/editor/default/0001/54/77d9f1e47894f812108d6678aa0fb63dad4cb89c.jpeg"/> Ana sayfaya dön!</a>'

@app.route("/rastgele_bilgi")
def rastgele_bilgi():
    return f'<p>{random.choice(facts_list)}</p> <a href="/"> <img src ="https://i.pinimg.com/736x/23/c9/cb/23c9cb81a4f5d4aabb83aff8720c6c81.jpg" /> Ana sayfaya dön!</a>'
#bu farklı bir sayfa oldu yukardakinin linkine /rastgele_bilgi deyip ulaşıyoruz

app.run(debug=True)
