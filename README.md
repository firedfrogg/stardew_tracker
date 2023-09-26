# Tugas 2
##### Jelaskan bagaimana cara kamu mengimplementasikan *checklist* secara *step-by-step* (bukan hanya sekedar mengikuti tutorial)
1. Langkah pertama dalam mengimplementasikan *checklist* adalah membuat projek Django. Saya melakukan ini dengan membuat proyek Django baru dengan nama "stardew_tracker" dengan sintaks `django-admin startproject stardew_tracker` 
2. Membuat aplikasi Django baru bernama "main" dengan sintaks `python manage.py startapp main`
3. Setelah membuat aplikasi baru, proyek akan dilakukan routing pada `urls.py` agar dapat menjalankan aplikasi "main" dengan sintaks
    ```
    urlpatterns = [
        path('', include('main.urls')),
        path('admin/', admin.site.urls),
    ]
    ```
4. Membuat *class* `Item ` pada `model.py` dan menambahkan atribut-atribut wajib, yaitu `name`, `amount`, dan `description`. Selain itu, saya menambahkan atribut-atribut lain untuk memberikan informasi lebih jelas mengenai suatu *item* dan menyesuaikan tema aplikasi yang ingin dibuat, yaitu `season`, `favorable_weather`, dan `price`.
5. Membuat fungsi `show_main` pada `views.py` yang akan dikembalikan *dictionary* `context` yang berisikan `application_name`, `name`, `item_name`,`season`, `favorable_season`, `price`, `description`, `amount` ke dalam *template* html untuk 
6. Membuat routing pada aplikasi untuk memetakan fungsi `show_main` yang telah dibuat pada `views.py` dengan sintaks
    ```
    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
7. Membuat *test case* untuk aplikasi yang mengkonfirmasi bahwa saat mengakses URL `/main/`, halaman web merespon dengan status kode 200, menggunakan template `main.html`, dan berisi teks 'Stardew Valley's Item Tracker'. Selain itu, *test case* dibuat untuk memastikan *method* `calculate_total` pada *class* `Item` mengembalikan nilai total yang benar dan mengetes *method* `__str__` untuk memastikan *method* tersebut mengembalikan nama *item* yang sesuai.
8. Melakukan *deployment* ke Adaptable dengan memilih `Python App Template` sebagai *template deployment*, memilih `PostgreSQL` sebagai tipe basis data yang digunakan, menggunakan Python versi `3.11`, memasukkan perintah `python manage.py migrate && gunicorn stardew_tracker.wsgi` pada bagian `Start Command`, dan mencentang bagian `HTTP Listener on PORT`. Lalu, mengeklik `Deploy App` untuk memulai proses *deployment* aplikasi 

##### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
*Request Client*:  Merupakan permintaan HTTP yang dikirim oleh browser klien ke aplikasi web Django
|
|
v
` urls.py`: Mengatur routing dan menentukan jalur URL yang akan mengeksekusi fungsi `show_main` di             `views.py`
| 
|
v
`views.py`: Mengekskusi `show_main`. Fungsi tersebut bertanggung jawab untuk mengatur respon yang akan         dikirimkan kembali ke *browser*
|
| 
v
`models.py`: `views.py` dapat berinteraksi dengan model data yang didefinisikan di `models.py`. Model ini mengatur struktur dan logika data aplikasi.
|
| 
v
*Template* `HTML`:Digunakan untuk me-*render* `views.py`
| 
|
v
*Response*: Respon yang dihasilkan oleh Djnago yang berisikan tampilan HTML yang telah di-*render*
| 
|
v
*Client Browser*: Me-*render* halaman web sesuai respons yang diterima

##### Jelaskan mengapa kita menggunakan *virtual environment?* Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*?

- Dengan menggunakan *virtual environment*, aplikasi yang akan dibuat akan tetap stabil dan konsisten dalam *environment-environment* di dalam perangkat lain. *Virtual environment* juga digunakan untuk memastikan bahwa setiap orang yang bekerja pada pembuatan web menggunakan *dependencies* yang sama. Membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment* dapat menyebabkan masalah kompabilitas dan akan menyulitkan konsistensi *environment* ketika akan melakukan proses *deployment*

##### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- MVC (Model-View-Controller): Konsep arsitektur yang digunakan dalam pengembangan web dengan memisahkan *Model*, *View*, dan *Controller*. *Model* digunakan untuk menyimpan data dan logika aplikasi, *View* digunakan untuk menampilkan data dari model yang telah dibuat. *Controller* digunakan untuk menghubungkan *Model* dan *View*. MVC dapat digunakan dalam berbagai platform pengembangan perangkat lunak.
- MVT (Model-View-Template): Konsep arsitektur yang digunakan dalam pengembangan web dengan memisahkan *Model*, *View*, dan *Template*. *Template* digunakan untuk menghubungkan *Model* dan *View*. *Model* digunakan untuk menyimpan data dan logika aplikasi, *View* digunakan untuk menampilkan data dari model yang telah dibuat. MVT adalah konsep khusus dalam Django *framework* untuk pengembangan web.
- MVVM (Model-View-ViewModel): Konsep arsitektur yang digunakan dalam pengembangan aplikasi berbasis *user interface* (UI) dengan memisahkan *Model*, *View*, dan *ViewModel*. *Model* digunakan untuk menyimpan data dan logika aplikasi, *View* digunakan untuk menampilkan data dari model yang telah dibuat, dan *ViewModel* untuk mengelola logika dari aplikasi.MVVM dapat digunakan dalam berbagai platform pengembangan perangkat lunak.

# Tugas 3
## Apa perbedaan antara form POST dan form GET dalam Django?
 - Salah satu Perbedaan antara `POST` dan `GET` dalam Django terletak pada visibilitas data yang akan diberikan di mana `POST` digunakan untuk mengirimkan data-data yang tersembunyi dalam permintaan HTTP dan tidak akan ditampilkan dalam URL, sedangkan `GET` digunakan untuk mengirimkan data-data yang akan ditampilkan pada URL dan dapat dilihat oleh *user*. Selain itu, perbedaan lain adalah method `GET` biasanya digunakan jika ingin mengambil data dari sebuah URL dan method `POST` digunakan untuk mengirim data-data yang bersifat sensitif.
## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- Dalam pengiriman data, JSON menggunakan *key-value* atau *dict* sebagai format untuk komunikasi antar server. Sementara itu, XML dan HTML menggunakan *markup* dengan *tag* dan *attribute* yang mirip satu dengan yang lain, tetapi HTML digunakan untuk membuat tampilan halaman web, sedangkan XML digunakan untuk menyimpan dan mengirim data terstruktur dalam format teks
## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- Di antara aplikasi web modern, JSON adalah format yang sering digunakan dibandingkan format lain karena memiliki banyak kelebihan, yaitu efisiensi dalam penyimpanan data dengan *size* yang relatif kecil. Selain itu, *parser* untuk format JSON tersedia di banyak bahasa pemrograman, membuatnya mudah untuk ditulis dalam kode. JSON juga mudah dibaca oleh manusia dan mendukung tipe-tipe data standar, seperti *String* dan *Integer*.
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Untuk membuat *input* `form`, terlebih dahulu, saya membuat file `forms.py` lalu membuat *class* `Meta` dengan `model` yang berisikan `item` pada `models.py` dan `fields` yang berisikan: `name`, `price`, `description`, `season`, `favorable_weather`, `amount` (Sesuai dengan website yang ingin saya buat). Setelah itu, saya membuat method `create_product` yang nantinya akan menambahkan data *item* secara otomatis ketika *user* menekan tombol *submit* dari *form* dan menambahkan variabel untuk mengambil seluruh object Item yang akan disimpan pada *database* di `views.py` serta menambahkan `path` ke dalam `urls.py` agar *user* dapat mengakses dan meng-*input* produk ke dalam `form`. Lalu, saya membuat file `create_product.html` untuk membuat tampilan dari fungsi `create_product` dan mengubah tampilan `main.html` dengan menambahkan tabel agar dapat menampilkan *database* dari produk yang sudah di-*input*.
- Untuk melihat objek-objek yang sudah ditambahkan ke dalam `database`, saya menggunakan format HTML, XML, JSON, XML by ID, dan JSON by ID yang fungsi-fungsinya akan ditambahkan ke dalam `views.py`. Pada file `views.py`, method `show_main` yang akan digunakan pada file `urls.py` akan mengembalikan method `render()` dengan parameter  `request`, `main.html`, dan `context`. Setelah itu, method `create_product` juga akan dibuat untuk memasukkan objek ke dalam *database* berdasarkan input user yang akan me-*return* `render(request, "create_product.html", context)` di mana `context` berisikan `item`, `item_count` untuk menghitung jumlah item di dalam *database*, `item_total_worth` untuk menghitung total nilai seluruh objek di dalam *database*, dan `days_since_added` yang akan menghitung hari terakhir sejak memasukkan objek ke dalam *database*. Terdapat empat fungsi yang dibuat untuk mengembalikan data dalam berbagai bentuk,  yaitu `show_xml` untuk mengembalikan dengan format XML, `show_json` untuk mengembalikan dengan format JSON, `show_xml_by_id` untuk mengembalikan satu ID di *database* dengan format XML, dan `show_json_by_id` untuk mengembalikan satu ID di *database* dengan format JSON. Pada setiap fungsi yang dibuat, saya membuat variabel `data` yang berisikan seluruh objek dari database yang telah dibuat. Khusus untuk mengembalikan dengan ID, objek pada *database* yang ada akan di-filter sedemikian sehingga hanya terdapat ID sesuai *input* yang menjadi *parameter*. Lalu, untuk masing-masing format, saya akan me-*return* fungsi tersebut dengan *parameter* `HttpResponse` yang berbeda:

Untuk XML, parameter yang digunakan dalam `HttpResponse` adalah:
```
serializers.serialize("xml", data), content_type="application/xml"
```

Untuk JSON, parameter yang digunakan dalam `HttpResponse` adalah:
```
serializers.serialize("json", data), content_type="application/json"
```

Agar kelima fungsi tersebut dapat diakses, pada `urls.py`, *list* `url_patterns` akan ditambahkan beberapa `path` sehingga *list* `url_patterns` akan menjadi sebagai berikut:
```
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('delete-item', delete_item, name='delete_item'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('xml/', show_xml, name='show_xml')
]
```

*Screenshot-screenshot* akses kelima URL menggunakan Postman dapat dilihat di bawah
### XML
![XML](image.png)
### JSON
![JSON](image-1.png)
### XML by ID
![XML by ID](image-2.png)
### JSON by ID
![JSON by ID](image-3.png)
### HTML
![HTML](image-4.png)

# Tugas 4
## Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
- `UserCreationForm` adalah sebuah formulir bawaan Django yang memudahkan *developer* untuk membuat akun pengguna dalam aplikasi web yang sedang dibuat. Biasanya, `UserCreationForm` digunakan untuk melakukan autentikasi dan manajemen pengguna aplikasi web. Karena `UserCreationForm` merupakan formulir bawaan dari Django, *developer* tidak perlu mendesain ulang tampilan untuk autentikasi pengguna dari awal dan dapat langsung meng-*import* dari Django. Selain itu, `UserCreationForm` dapat dengan langsung melakukan validasi *input* akun pengguna, yaitu *username*, *password*, dan *e-mail* tanpa perlu juga mendesain algoritma validasi *input* dari awal serta menyimpannya di *database* untuk dikelola. `UserCreationForm` juga kompatibel untuk versi-versi Django sehingga memudahkan *developer* yang menggunakan *framework* Django dalam berbagai versi untuk menggunakannya. Di sisi lain, `UserCreationForm` tidak cocok untuk pengembangan web dalam bahasa selain Inggris karena segala *error message* di dalam `UserCreationForm` dibuat menggunakan bahasa Inggris sehingga *developer* yang mendesain sebuah web dalam bahasa selain Inggris menggunakan *framework* Django perlu menyesuaikan *error message* dengan bahasa yang ingin digunakan. *Form* pada `UserCreationForm` hanya mencakup informasi-informasi dasar pengguna, seperti *username*, *password*, dan *email* dan memerlukan penyesuaian secara manual untuk menambahkan informasi-informasi pengguna lain, contoh: tanggal lahir, pendidikan terakhir, dsb. Sementara itu, karena `UserCreationForm` bergantung pada *framework* Django, *developer* yang mendesain web menggunakan framework Django akan mengalami kesulitan jika ingin mengubah *framework* lain di masa depan.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
- Autentikasi merupakan proses verifikasi identitas pengguna. Autentikasi sendiri adalah langkah awal dalam memeriksa hak akses suatu pengguna ke aplikasi web yang sedang dibuat. Dalam konteks Django, autentikasi digunakan untuk memastikan bahwa pengguna yang sedang mencoba untuk mengakses aplikasi web yang sedang dibuat benar-benar pengguna yang terdaftar di *database* dan memiliki akun dalam aplikasi web. Autentikasi sendiri diperlukan dalam pengemabangan aplikasi web dengan *framework* Django untuk melindungi fitur dan *resources* aplikasi web yang sedang dikembangkan dari akses yang tidak sah dari pengguna lain dan memberikan keamanan tambahan untuk memastikan fitur serta *resources* tersebut diakses oleh pengguna-pengguna yang sah.
- Otorisasi adalah penentuan hak akses yang dimiliki oleh setiap pengguna dalam aplikas web yang sah. Penentuan hak akses ini melibatkan fitur dan *resources* apa saja yang dapat diakses oleh pengguna, seperti mengakses suatu halaman, mengedit halaman tersebut, atau melakukan tindakan khusus lain dalam sebuah halaman. Biasanya, otorisasi diterapkan dengan menggunakan peran (*roles*), seperti pada aplikasi web Discord atau izin (*permissions*) yang diberikan kepada pengguna. Otorisasi juga penting dalam pengembangan sebuah aplikasi web dengan *framework* Djang untuk melindungi penyalahgunaan suatu *resource* aplikasi web dari pengguna-pengguna yang terdaftar dan mengontrol tingkat akses pengguna yang memastikan bahwa hanya pengguna-pengguna terdaftar tertentu yang memiliki izin untuk melakukan sesuatu di dalam aplikasi web.

## Apa itu *cookies* dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
- Seperti layaknya kue yang berukuran kecil, *cookies* dalam konteks aplikasi web merupakan data dengan ukuran kecil yang disimpan *client* ketika pengguna sedang berinterkasi dengan sebuah aplikasi web. Cookies digunakan untuk menyimpan informasi tertentu yang dapat diakses dan diolah oleh server aplikasi web ketika pengguna melakukan *request* selanjutnya ke dalam situs tersebut. Pada *framework* Django, *cookies* digunakan untuk mengelola sesi suatu pengguna. Ketika pengguna melakukan *log in* ke dalam sebuah aplikasi web, *server* akan membuat *cookie* yang berisikan *unique identifier* untuk sesi pengguna tersebut. *Cookie* ini dapat memunkginkan server untuk tetap mempertahankan sesi *log in* pengguna, seperti detil *log in*, preferensi pengguna ketika menggunakan aplikasi, dan ketika pengguna berpindah halaman atau menutup sebuah browser. Django menggunakan *cookies* untuk mengelola data sesi pengguna dengan `HttpResponseRedirect` dan method `set_cookie()` yang berfungsi untuk membuat *cookie* dan menambahkannya ke dalam `object` `HttpResponseRedirect`.

## Apakah penggunaan *cookies* aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
- Penggunaan *cookies* secara *default* tidak memberikan risiko bawaan yang harus diperhatikan *developer* ketika sedang mengembangkan aplikasi web menggunakan *framework* Django. Namun, *developer* sendiri harus memperhatikan faktor-faktor eksternak, seperti penyalahgunaan *cookies* untuk mencuri informasi sensitif, seperti token otentikasi atau data sesu pengguna. Jika tidak digunakan dengan benar, *cookies* akan sangat rentan diserang, seperti Cross-Site Scripting (XSS) atau Cross-Site Request Forgery (CSRF). Sementara itu, *cookies* pengguna yang dicuri dapat dengan mudah diolah dan dimanipulasi, seperti melacak preferensi pengguna ketika sedang menggunakan aplikasi web untuk keperluan promosi. *Cookies* yang dicuri juga mempunyai risiko lebih jika mengandung informasi-informasi penting, seperti token otentikasi yang dapat dimanfaatkan untuk mengakses dan memanipulasi akun pengguna tanpa izin pengguna tersebut.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Untuk mengimplementasikan fungsi registrasi, *login*, dan *logout*, saya menggunakan *method-method* `authentiate`, `login`, `login_required`, dan `logout` dari `django.contrib.auth`. Pertama, saya membuat *method* `register` yang bertujuan untuk membuat akun pengguna di aplikasi web dengan objek `form` menggunakan `UserCreationForm`. Ketika `form` tersebut sudah valid, `form` yang berisikan informasi pengguna tersebut akan disimpan ke dalam database apikasi web dan akan me-*redirect* aplikasi web ke `show_main`. Kedua, saya membuat *method* `login_user` untuk proses autentikasi dan login pengguna yang valid. Ketika pengguna yang valid telah diautentikasi, aplikasi akan melakukan *redirect* ke `show_main`, sedangkan ketika gagal diautentikasi, program akan menampilkan info berupa *Sorry, incorrect username or password. Please try again.*. Lalu, saya membuat berkas HTML dengan nama `login.html` untuk membuat tampilan untuk autentikasi dan login user. Ketiga, saya membuat *method* *logout* yang bertujuan untuk melakukan *logout* terhadap akun yang sedang dalam *session* dengan memanfaatkan method *logout* pada `django.contrib.auth`. Setelah melakukan logout, aplikasi web akan me-*redirect* ke `login`.
- Selanjutnya, saya membuat dua akun dummy dan menaruh tiga dummy data menggunakan model yang udah ada.
- Kemudian, saya meng-*import* `User` dari `django.contrib.auth.models` untuk menghubungkan model `Item` dengan `User`. Pada model `Item` yang sudah dibuat, saya menambahkan `models.ForeignKey(User, on_delete=models.CASCADE)` ke dalam objek untuk mengasosiasikan `item` dengan seorang pengguna. Di `views.py` yang ada pada subdirektori `main`, saya menambhkan parameter `commit=False` untuk mencegah Django menyimpan lansgung objek yang akan dibuat ke dalam *database*. Hal tersebut memungkinakn kita untuk mengubah terlebih dahulu `product` sebelum selanjutnya disimpan ke dalam *database*. Selanjutnya, saya menambahkan objek `items` yang berisikan `Product.objects.filter(user=request.user)` untuk menampilkan objek `items` yang terasosiasikan dengan pengguna yang sedang melakukan `login`. Pada *dictionary* `context`, saya menambahkan *value* `request.user.username` pada *key* `name` untuk menampilkan *username* pengguna saat sedang *login*. Setelah semuanya selesai, saya melakukan migrasi model dengan `python manage.py makemigrations`, menetapkan *default value* untuk *field user* pada semua row yang telah dibuat pada basis data dengan angka 1 untuk pengguna dengan ID 1 (akun yang pertama kali dibuat). Terakhir, saya melakukan `python manage.py migrate` untuk mengaplikasikan migrasi yang dilakukan pada `manage.py`
- Pada `item` yang sudah ada, saya membuat fitur untuk mengurangi jumlah, menambah jumlah, dan menghapus item tersebut. Ketiga fitur tersebut saya buat di `views.py` dengan method `delete_item`, `reduce_amount`, dan `increase_amount`. Pada *method* `delete_item`, objek `item` yang ada akan dihapus dengan method `delete`. Lalu, pada *method* `reduce_amount`, saya cukup melakukan decrement terhadap `amount` dari `item` yang akan di-klik, sedangkan pada method `increase_amount`, saya cukup melakukan increment terhadap value dari `item` tersebut. Kemudian, saya menambahkan tiga *header* pada *table* di file `main.html` untuk membuat *button* yang bernama *Delete Item*, *Reduce Amount*, dan *Increase Amount*. Lalu, saya menghubungkannnya ke `urls.py` dengan sintaks sebagai berikut:
```
path('delete_item/<int:id>/', delete_item, name='delete_item'),
path('reduce_amount/<int:id>/', reduce_amount, name='reduce_amount'),
path('increase_amount/<int:id>/', increase_amount, name='increase_amount'),
``` 
`<int:id>` menandakan `item` yang akan dihapus