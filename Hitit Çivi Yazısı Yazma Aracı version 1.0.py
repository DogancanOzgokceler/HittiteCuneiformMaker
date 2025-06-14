#𒀀𒀸𒋗𒇷
# İmport kısmı
# version 0.6 30.08.2023
# version 0.7 1.09.2023
import pieoffice
import matplotlib
from matplotlib.font_manager import FontProperties
#Doğancan ÖZGÖKÇELER - Beylikdüzü -İstanbul
#"Bilim Hücresi Sanal Okul" Discord serverına teşekkür ederim.
#Çivi yazısını programa aktarma yedek kısmı burada bitiyor.

# Çivi Yazısı Sözlüğü
civi_sozlugu = {
    "V": {
        "a": "𒀀",
        "e": "𒂊",
        "i": "𒄿",
        "u": "𒌋",
        "ú": "𒌑"
        # Diğer ünlü harfler buraya eklenebilir
    },
    "CV": {
        "ba": "𒁀",
        "be": "𒁁",
        "bi": "𒁉",
        "bu": "𒁍",
        "pu": "𒁍",
        "pa": "𒉺",
        "pé": "𒁉",
        "pí": "𒁉",
        "da": "𒁕",
        "de": "𒁲",
        "di": "𒁲",
        "du": "𒁺",
        "ta": "𒋫",
        "te": "𒋼",
        "ti": "𒋾",
        "tu": "𒌅",
        "ga": "𒂵",
        "ge": "𒄀",
        "gi": "𒄀",
        "gu": "𒄖",
        "ka": "𒅗",
        "ke": "𒆠",
        "ki": "𒆠",
        "ḫa": "𒄩",
        "ha": "𒄩",
        "ḫe": "𒄭",
        "he": "𒄭",
        "ḫé": "𒃶",
        "ḫi": "𒄭",
        "ḫu": "𒄷",
        "la": "𒆷",
        "le": "𒇷",
        "li": "𒇷",
        "lu": "𒇻",
        "ma": "𒈠",
        "me": "𒈨",
        "mé": "𒈪",
        "mi": "𒈪",
        "mu": "𒈬",
        "na": "𒈾",
        "ne": "𒉈",
        "né": "𒉌",
        "ni": "𒉌",
        "nu": "𒉡",
        "ra": "𒊏",
        "re": "𒊑",
        "ri": "𒊑",
        "ru": "𒊒",
        "ša": "𒊭",
        "še": "𒊺",
        "ši": "𒅆",
        "šu": "𒋗",
        "su": "𒋗",
        "šú": "𒋙",
        "wa": "𒉿",
        "wi5": "𒃾",
        "ya": "𒅀",
        "za": "𒍝",
        "ze": "𒍣",
        "zé": "𒍢",
        "zi": "𒍣",
        "zu": "𒍪",
        "ku": "𒆪"
        # Diğer CV harfleri buraya eklenebilir
    },
    "VC": {
        "ab": "𒀊",
        "ap": "𒀊",
        "ad": "𒀜",
        "at": "𒀜",
        "ag": "𒀝",
        "ak": "𒀝",
        "aḫ": "𒄴",
        "ah": "𒄴",
        "eḫ": "𒄴",
        "eh": "𒄴",
        "iḫ": "𒄴",
        "ih": "𒄴",
        "uḫ": "𒄴",
        "uh": "𒄴",
        "al": "𒀠",
        "am": "𒄠",
        "an": "𒀭",
        "ar": "𒅈",
        "aš": "𒀸",
        "aş": "𒀸",
        "az": "𒊍",
        "eb": "𒅁",
        "ep": "𒅁",
        "ib": "𒅁",
        "ip": "𒅁",
        "ed": "𒀉",
        "et": "𒀉",
        "id": "𒀉",
        "it": "𒀉",
        "eg": "𒅅",
        "ek": "𒅅",
        "ig": "𒅅",
        "ik": "𒅅",
        "el": "𒂖",
        "em": "𒅎",
        "im": "𒅎",
        "en": "𒂗",
        "er": "𒅕",
        "ir": "𒅕",
        "eš": "𒌍",
        "es": "𒌍",
        "eş": "𒌍",
        "iš": "𒅖",
        "iş": "𒅖",
        "is": "𒅖",
        "ez": "𒄑",
        "iz": "𒄑",
        "il": "𒅋",
        "in": "𒅔",
        "ul": "𒌌",
        "um": "𒌝",
        "un": "𒌦",
        "ur": "𒌨",
        "úr": "𒌫",
        "ür": "𒌫",
        "uš": "𒍑",
        "uş": "𒍑",
        "uz": "𒊻"
        # Diğer VC harfleri buraya eklenebilir
    },
    # Diğer çekimler buraya eklenebilir
}

belirtec = {
    # Belirteç semboller buraya eklenebilir
    "M": "𒁹",
    "I": "𒁹",
    "DIDLI": "𒀸",
    "DIDLI ḪI.A": "𒀸𒄭𒀀",
    "DINGIR": "𒀭",
    "DUG": "𒂁",
    "É": "𒂍",
    "GAD": "𒃰",
    "GI": "𒄀",
    "GIŠ": "𒄑",
    "GUD": "𒄞",
    "ḪI.A": "𒄭𒀀",
    "ḪUR.SAG": "𒄯𒊕",
    "ÍD": "𒄔",
    "IM": "𒅎",
    "ITU": "𒌚",
    "KAM": "𒄰",
    "KI": "𒆠",
    "KU6": "𒄩",
    "KUR": "𒆳",
    "KUŠ": "𒋢",
    "LÚ": "𒇽",
    "MEŠ": "𒈨𒌍",
    "MEŠ ḪI.A": "𒈨𒌍𒄭𒀀",
    "MUL": "𒀯",
    "MUNUS": "𒊩",
    "MUŠ": "𒈲",
    "MUŠEN": "𒄷",
    "NA4": "𒋡",
    "NINDA": "𒃻",
    "PÚ": "𒁍",
    "SAR": "𒊬",
    "SI": "𒋛",
    "SÍG": "𒋠",
    "TU7": "𒄰",
    "TÚG": "𒌆",
    "Ú": "𒌑",
    "URU": "𒌷",
    "URUDU": "𒍐",
    "UZU": "𒍜",
    # Diğer belirteç semboller buraya eklenebilir
}

# Diğer büyük harfle başlayan heceler buraya eklenebilir

def kelimeyi_civi_yazisina_cevir(kelime):
    civi_kelime = ""
    heceler = kelime.split('-')
    for hece in heceler:
        if hece in civi_sozlugu["V"]:
            civi_kelime += civi_sozlugu["V"][hece]
        elif hece in civi_sozlugu["CV"]:
            civi_kelime += civi_sozlugu["CV"][hece]
        elif hece in civi_sozlugu["VC"]:
            civi_kelime += civi_sozlugu["VC"][hece]
        elif hece.upper() in belirtec:
            civi_kelime += belirtec[hece.upper()]
        else:
            civi_kelime += hece
    return civi_kelime
while True:
    # Kullanıcıdan kelime veya cümleyi al
    giris = input("Hititçe kelime veya cümleyi girin (örneğin: an-na-aş) veya 'q' tuşuna basarak çıkmak için: ")

    if giris == 'q':
        break  # Döngüyü sonlandır

    # Girilen girişi boşluklara göre ayırarak kelimeleri elde et
    kelimeler = giris.split()

    # Her bir kelimeyi çivi yazısına çevir ve aralarına boşluk bırakarak yeni bir çivi yazısı oluştur
    civi_yazi_cumle = ""
    for kelime in kelimeler:
        civi_yazi_kelime = kelimeyi_civi_yazisina_cevir(kelime)
        civi_yazi_cumle += civi_yazi_kelime + ' '

    # Oluşturulan çivi yazısını yazdır
    print("Çivi Yazısı:", civi_yazi_cumle)

    # Kullanıcıdan devam etmek isteyip istemediğini sorgula
    devam = input("Devam etmek için Enter tuşuna basın, çıkmak için 'q' tuşuna basın: ")
    if devam == 'q':
        break  # Döngüyü sonlandır


