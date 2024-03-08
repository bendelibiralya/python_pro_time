import time
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "CREEPY": "Korkunç",
            "SLAY": "Ortamı yıkıp geçmek, kendine hayran bırakmak",
            "GO GIRL": "Yürü be kızım! anlamına gelen destek için kullanlan söz",
            "TEA": "Dedikodu",
            "MEME": "İnternet üzerinde popüler resim, video, kelime ya da cümleler şeklinde yayılan ve geniş kitlelerce manası bilinen olgular, şakalar"
            }


giris = print("Meme sözlüğüne hoşgeldiniz! Burası eskiler için modern kelimeleri anlamaya yardımcı bir sözlüktür. İstediğiniz kadar soru sorabilirsiniz, iyi öğrenmeler!")

while True:
    
    word = input("Anlamadığınız bir kelime yazın ve size mealini yazalım! (hepsini büyük harflerle yazın!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Bu kelime sözlüğümüzde yok, başka bir kelime deneyiniz")
    
    time.sleep(1)
