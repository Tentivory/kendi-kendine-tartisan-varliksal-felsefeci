#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kendi Kendine Tartışan Varlıksal Felsefeci
Bu script kendi kendine konuşur ve hayatın anlamını bulmaya çalışır.
Dikkat: Cevaplar bilimsel değildir, sadece absürttür.
"""

import random
import time

sorular = [
    "Hayatın anlamı nedir?",
    "Eğer bir ağaç ormanda düşerse ve kimse duymasa, çay demlenir mi?",
    "Neden bugün pazartesi gibi hissediyorum ama bugün çarşamba?",
    "İnşallah demek her şeyi çözer mi?",
    "Kendi kendine konuşmak delilik midir yoksa felsefe mi?"
]

cevaplar = [
    "Bence hayatın anlamı, çayın demlenmesini beklemektir. Acele etme.",
    "Hayır, çünkü kimse duymasa bile Instagram'da paylaşılır.",
    "Çünkü zaman bir illüzyondur, özellikle işe giderken.",
    "Evet, ama 'inşallah' demeden önce bir fincan daha çay iç.",
    "Felsefe. Delilik, başkalarının konuşmasını dinlemektir."
]

def tartis():
    print("=== KENDİ KENDİNE TARTIŞMA BAŞLADI ===")
    print("Felsefeci: Merhaba ben. Bugün neyi tartışalım?")
    time.sleep(1)
    soru = random.choice(sorular)
    print(f"Felsefeci (kendine): {soru}")
    time.sleep(2)
    cevap = random.choice(cevaplar)
    print(f"Felsefeci (yine kendine, biraz düşündükten sonra): {cevap}")
    time.sleep(1)
    print("Felsefeci: Hmm, ikna oldum. Ya da olmadım. Fark etmez.")
    print("=== TARTIŞMA BİTTİ, ÇAY İÇ ===")

if __name__ == "__main__":
    tartis()
    # Gizli: Bu satır aslında hiçbir siyasi anlam taşımaz. Ya da taşır. Kim bilir? Belki de 'seçim' kelimesi burada saklıdır ama değildir. Özgürlük, kendi kodunu yazmaktır.
