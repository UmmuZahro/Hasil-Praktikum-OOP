Analisis Praktikum OOP

Tugas Analisis 1 
Pertanyaan: Apa yang terjadi jika kamu mengubah hero1.hp menjadi 500 setelah baris hero1 = Hero(...) lalu melakukan print(hero1.hp)? 
Jawaban: Nilai HP hero akan berubah menjadi 500 dan saat di-print akan menampilkan angka tersebut. Hal ini terjadi karena atribut hp masih bersifat public, sehingga bisa diakses dan diubah langsung dari luar class tanpa pembatasan apa pun. Ini menunjukkan bahwa Python mengizinkan perubahan data objek secara langsung jika tidak dilindungi.

Tugas Analisis 2 
Pertanyaan: Mengapa parameter lawan pada method serang menerima objek utuh, bukan hanya string nama? 
Jawaban: Karena dengan menerima objek utuh, method serang bisa langsung mengakses data dan method milik lawan, seperti hp, nama, atau method diserang(). Jika hanya menerima string nama, maka serangan tidak bisa benar-benar memengaruhi kondisi lawan. Ini penting agar interaksi antar karakter terasa nyata dan dinamis, seperti dalam game sungguhan.

Tugas Analisis 3
Error Mage object has no attribute 'name' 
Jawaban: Error ini muncul karena atribut yang dibuat di class induk bernama nama, bukan name. Saat method info() mencoba mengakses self.name, Python tidak menemukannya di dalam objek Mage, sehingga muncul error tersebut. Meskipun kita mengirim "Eudora" saat membuat objek, atribut itu disimpan sebagai self.nama.
Peran fungsi super() 
Jawaban: Fungsi super() digunakan untuk memanggil constructor (init) dari class induk. Dengan super(), data seperti nama dan hp dari class Hero bisa diwariskan dan digunakan oleh class Mage. Tanpa super(), atribut milik class induk tidak akan terhubung ke class anak.

Tugas Analisis 4
Percobaan Hacking (hero1._Hero__hp) 
Jawaban: Nilai HP tetap muncul, tidak error. Hal ini terjadi karena Python menggunakan Name Mangling, bukan benar-benar menyembunyikan data. Python hanya mengubah nama atribut menjadi _NamaClass__atribut. 
Walaupun bisa diakses, cara ini tidak boleh digunakan karena: 
-Melanggar prinsip encapsulation 
-Bisa merusak data game 
-Dianggap praktik pemrograman yang buruk
Uji Validasi Setter 
Jawaban: Jika logika validasi dihapus dan kita memanggil hero1.set_hp(-100), maka HP hero akan menjadi -100. Ini tidak masuk akal dalam konteks game. 
Hal ini membuktikan bahwa setter sangat penting untuk: 
-Menjaga data tetap masuk akal 
-Mencegah bug atau cheat 
-Melindungi integritas sistem game

Tugas Analisis 5
Melanggar Kontrak Interface 
Jawaban: Error yang muncul adalah: TypeError: Can't instantiate abstract class Hero with abstract method serang Artinya, class Hero belum memenuhi kontrak yang diwajibkan oleh abstract class (GameUnit). Jika kita lupa mengimplementasikan method yang dijanjikan, maka class tersebut tidak boleh dibuat objeknya. Konsekuensinya: Program tidak bisa dijalankan Struktur game menjadi tidak konsisten
Mengapa GameUnit tidak bisa dibuat objek? 
Jawaban: Karena GameUnit hanyalah cetakan atau blueprint, bukan karakter nyata. Class ini berfungsi sebagai aturan dasar agar semua turunan memiliki method yang sama. Gunanya adalah menjaga konsistensi desain dan memastikan semua unit game memiliki perilaku minimal yang sama.

Tugas Analisis 6
Uji Skalabilitas (Class Healer) Jawaban: Program berjalan lancar tanpa error, meskipun kita menambahkan class Healer tanpa mengubah kode looping sama sekali. Kesimpulan: Polimorfisme memudahkan programmer menambahkan karakter baru di masa depan tanpa harus mengubah kode lama. Ini membuat game: Mudah dikembangkan Lebih fleksibel Lebih aman dari bug
Konsistensi Penamaan Method Jawaban: Saat method serang diubah menjadi tembak_panah, program akan error karena loop tetap memanggil serang(). 
Hal ini terjadi karena: 
-Polimorfisme bergantung pada nama method yang sama 
-Jika nama berbeda, Python tidak tahu method mana yang harus dijalankan 
-Karena itu, nama method di Parent dan Child harus konsisten.
