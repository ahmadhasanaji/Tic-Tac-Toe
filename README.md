# MODUL 6 ARTIFICIAL INTELLIGENCE
# PERMAINAN TIC TAC TOE

Dalam modul praktikum 6, disajikan sebuah program yang bertujuan untuk membuat permainan Tic Tac Toe. Penulis mengaplikasikan modul 'tkinter' dalam bahasa pemrograman Python untuk menciptakan sebuah program sederhana yang memungkinkan permainan Tic-Tac-Toe.

Berikut adalah penjelasan dari setiap bagian program:

1. Mengimpor modul tkinter:\
Program dimulai dengan mengimpor modul tkinter dengan alias tk. Modul ini digunakan untuk menciptakan antarmuka pengguna grafis (Graphical User Interface).\
![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture1.png?raw=true)

2. Kelas GameState:\
Kelas GameState digunakan untuk mendefinisikan beberapa konstanta yang merepresentasikan status permainan. Terdapat empat kemungkinan status permainan, yaitu:
    - PLAYING (sedang berlangsung)
    - DRAW (seri)
    - CROSS_WON (X menang)
    - NOUGHT_WON (O menang)\

    ![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture2.png?raw=true)

3. Kelas Seed:\
Kelas Seed digunakan untuk mendefinisikan konstanta yang merepresentasikan jenis isi dari sel-sel dalam papan permainan. Terdapat tiga kemungkinan isi sel:
    - EMPTY (kosong)
    - CROSS (X)
    - NOUGHT (O)

    ![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture3.png?raw=true)

4. Kelas Cell:\
Kelas Cell merepresentasikan sel dalam papan permainan. Setiap sel memiliki tiga atribut:
    - content untuk menunjukkan isi sel (berdasarkan kelas Seed)
    - row untuk menunjukkan baris sel
    - col untuk menunjukkan kolom sel

    ![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture4.png?raw=true)\
Kelas Cell memiliki dua metode:
    - clear untuk mengosongkan isi sel
    - paint untuk menggambar sel di dalam elemen canvas dengan menggunakan tkinter. Sel yang berisi "X" digambar dengan garis-garis merah, dan sel yang berisi "O" digambar dengan lingkaran biru.

    ![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture5.png?raw=true)

5. Kelas Board:\
Kelas Board merepresentasikan papan permainan Tic-Tac-Toe. Kelas ini memiliki atribut cells yang berupa matriks 3x3 dari objek-objek Cell. Kelas Board memiliki beberapa metode:
    - init untuk mengosongkan sel-sel di papan permainan.\
![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture6.png?raw=true)
    - is_draw untuk memeriksa apakah permainan berakhir seri (semua sel terisi).\
![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture7.png?raw=true)
    - has_won untuk memeriksa apakah ada pemain yang menang dengan melihat baris, kolom, atau diagonal papan permainan.\
![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture8.png?raw=true)
    - paint untuk menggambar papan permainan ke dalam elemen canvas dengan menggunakan objek Cell.\
![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture9.png?raw=true)

6. Kelas GameMain:\
Kelas GameMain adalah kelas utama program yang mengatur permainan dan antarmuka pengguna grafis. Kelas ini memiliki beberapa atribut konstan yang digunakan untuk mengatur tampilan, seperti ukuran sel, lebar garis, dan sebagainya.\
![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture19.png?raw=true)\
Kelas GameMain memiliki beberapa metode:
    - _ _ init _ _ untuk inisialisasi antarmuka pengguna grafis dan papan permainan.\
![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture10.png?raw=true)
    - init_game untuk memulai permainan dengan mengosongkan sel-sel di papan.\
![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture11.png?raw=true)
    - update_game untuk memeriksa apakah ada pemain yang menang atau permainan berakhir seri.\
![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture11.png?raw=true)
    - paint untuk menggambar papan permainan di dalam elemen canvas.\
![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture12.png?raw=true)
    - handle_click untuk menangani klik mouse pengguna dan mengisi sel dengan "X" atau "O" sesuai giliran pemain.\
![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture13.png?raw=true)

8. Membuat instance Tkinter:\
Program membuat instance dari kelas Tk dari modul tkinter sebagai root window.\
![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture14.png?raw=true)

9. Membuat instance GameMain:\
Program membuat instance dari kelas GameMain dengan menggunakan root window sebagai parent.\
![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture15.png?raw=true)

10. Binding Event Click:\
Program menggunakan metode bind untuk menghubungkan event klik kiri mouse ("<Button-1>") ke metode handle_click.\
![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture16.png?raw=true)

11. Memulai Loop Utama:\
Program memanggil metode mainloop() untuk memulai loop utama antarmuka pengguna grafis, yang akan menangani interaksi pengguna dan pembaruan tampilan.\
![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture17.png?raw=true)

Program ini menghasilkan permainan Tic-Tac-Toe yang dapat dimainkan melalui antarmuka pengguna grafis. Pemain dapat mengklik sel-sel pada papan permainan, dan permainan akan memeriksa siapa yang menang atau apakah permainan berakhir seri.

Berikut adalah hasil antarmuka pengguna grafis yang dihasilkan dari program permainan Tic Tac Toe yang dapat langsung dimainkan dengan mengarahkan kursor ke kotak yang sudah tersedia kemudian klik sesuai dengan urutan permainan.\
![alt text](https://github.com/ahmadhasanaji/Tic-Tac-Toe/blob/main/TicTacToe/Picture18.png?raw=true)
