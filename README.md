# hangman

1. İlk olarak, `random` modülü import edilir. Bu modül, rastgele bir kelime seçmek için kullanılacaktır.

2. Ardından, `kelimeler` adında bir sözlük oluşturulur. Bu sözlük, farklı seviyelerdeki kelimeleri içerir. "kolay", "orta" ve "zor" seviyeleri vardır. Her seviyenin altında bir kelime listesi bulunur.

3. Kullanıcıdan `seviye` adında bir giriş alınır. Bu giriş, kullanıcının oyun seviyesini belirlemesini sağlar.

4. Girilen `seviye` değeri, `kelimeler` sözlüğünde bulunan bir anahtar olarak kontrol edilir. Eğer geçerli bir seviye girilmezse, kullanıcıdan tekrar seviye girişi istenir.

5. Seçilen `seviye` değeri ile `kelime_listesi` oluşturulur. Bu liste, belirlenen seviyede bulunan kelimeleri içerir.

6. `random.choice()` fonksiyonu kullanılarak `kelime` değişkenine rastgele bir kelime atanır.

7. Kullanıcıdan `isim` adında bir giriş alınır. Bu giriş, kullanıcının adını temsil eder.

8. Oyuna başlandığını belirten bir mesaj (`hoşgeldin` mesajı) ve kullanıcının adı (`isim`) ekrana yazdırılır.

9. Tahmin işlemi başlar. Kullanıcıya kalan hakkı (`hak`) gösterilir ve her turda kullanıcının bir harf tahmini yapması istenir.

10. Tahmin edilen harf, `tahmin` adlı değişkende tutulur ve `tahmin_string` adlı boş bir stringe eklenir.

11. Ardından, `kelime` üzerinde döngü başlatılır ve her karakter için kontrol yapılır.

12. Eğer karakter, `tahmin_string` içinde bulunuyorsa, karakter ekrana yazdırılır. Eğer karakter `tahmin_string` içinde bulunmuyorsa, bir tire ("-") ekrana yazdırılır ve `k_ekle` değişkeni bir artırılır.

13. `k_ekle` değişkeninin değeri kontrol edilir. Eğer hala sıfır ise, tüm harfler tahmin edilmiştir ve kullanıcı oyunu kazanır. Kazanma mesajı ve doğru kelime ekrana yazdırılır.

14. Eğer `k_ekle` değişkeni sıfır değilse, kullanıcının tahmini yanlıştır ve `hak` değişkeni bir azaltılır. Yanlış tahmin mesajı ve kalan hak sayısı ekrana yazdırılır.

15. `hak` değişkeni kontrol ed

ilir. Eğer sıfır ise, kullanıcının hakları tükenmiştir ve oyun kaybedilir. Kaybetme mesajı ve doğru kelime ekrana yazdırılır.

Bu şekilde, kullanıcıya verilen haklar içinde kelimenin tamamını tahmin etmesi beklenir. Tahmin işlemi, kullanıcının girdiği harfleri kontrol ederek doğru tahminlerde bulunup bulunmadığını denetler ve kullanıcıya geri bildirim sağlar.
