Nurunnisa Fathanah Dz. S. B.
D121211002
Metode Komputasi Numerik Kelas A


A parachutist (Fathanah) of mass 56 kg jumps out of a stationary hot air balloon. The drag coefficient is equal to 12.5 kg/s. Compute velocity when t =30 seconds. The parachutist is initially at rest (v=0 at t=0).


Jadi, sesuai soal yang diberikan beraat dari parachutist mengikuti berat mahasiswa yaitu 56kg (berat Fathanah), kemudian dicari kecepatan jatuhnya setelah 30 detik.


Untuk setiap informasi yang diketahui ditulis ke dalam cell, seperti massa (m), percepatan gravitasi (g), drag coefficient (c), kecepatan(v) dan waktu (t). 


Dik : m = 56kg, g = 9.8 m/s, c = 12.5 kg/s, t = 0s, v = 0 m/s, delta t (dt) = 1 second


Dit: Kecepatan jatuh Fathanah setelah 30 detik = ...?


Penyelesaian:
1. Buat dua kolom untuk keterangan waktu jatuhnya (t), dan nilai kecepatan dalam waktu tersebut.
2. Untuk dua kolom baris pertama, masukkan t = 0, dan v = 0 sesuai informasi yang diberikan soal.
3. Kemudian untuk baris kedua pada kolom t, masukkan rumus (= <kolom t sebelumnya> + <nilai dt>), misalnya untuk baris kedua =B25+$C$20, menggunakan $$ untuk mengunci nilai delta t sehingga ketika ditarik ke bawah nilai B25 bisa berubah sedangkan nilai dari delta t tetap. 
4. Selanjutnya, untuk baris kedua kolom kedua, masukkan rumus (= <nilai vt sebelumnya> + (<nilai g> - (<nilai c> /<nilai m>) * <nilai vt sebelumnya> ) * nilai delta t), misalya untuk baris kedua  =C25+($C$16-($C$17/$C$15)*C25)*$C$20,menggunakan $$ untuk mengunci nilai g, m, c, dan delta t, sehingga ketika ditarik ke bawah nilai C25 (vt sebelumnya) bisa berubah. 

Dengan menggunakan rumus yang ditetapkan, maka kemudian didapatkan Kecepatan jatuh parachutist (Fathanah) setelah 30 detik adalah 43.88 m/s