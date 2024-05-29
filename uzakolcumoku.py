import gzip

def gzip_acma(dosya_adi):
    with gzip.open(dosya_adi, 'rb') as f:
        veri = f.read()
    return veri

# gzip ile sıkıştırılmış dosyanın adı
dosya_adi = 'ornek.gz'

# gzip ile sıkıştırılmış dosyayı açma
cozulmus_veri = gzip_acma(dosya_adi)

# Sıkıştırılmış veriyi ekrana yazdırma
print(cozulmus_veri.decode('utf-8')) # eğer veri UTF-8 kodlamasıyla kodlanmış ise
