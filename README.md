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