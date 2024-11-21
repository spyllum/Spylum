meme_sozlugu = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "ROFL bir şakaya karşılıktır, LOL gibidir"
}

tekrar_sayisi = int(input("İşlemi kaç kez tekrarlamak istersiniz? (5, 10, 15 seçin): "))

if tekrar_sayisi in [5, 10, 15]:
    for _ in range(tekrar_sayisi):
        kelime = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
        if kelime in meme_sozlugu.keys():
            print(meme_sozlugu[kelime])
        else:
            print("Henüz bu kelimeye sahip değiliz... Ama üzerinde çalışıyoruz!")
else:
    print("Lütfen sadece 5, 10 veya 15 seçeneklerinden birini girin!")
