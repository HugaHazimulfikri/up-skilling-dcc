def main():
    # Flag disembunyikan dalam variabel
    part1 = "DNCC{pyth0n_"
    part2 = "1s_345y_"
    part3 = "t0_r3v3rs3}"
    
    flag = part1 + part2 + part3
    
    user_input = input("Masukkan password: ")
    if user_input == "admin123":
        print("Bukan ini flagnya, coba baca kodenya lagi!")
    else:
        print("Salah! Coba lihat isi file ini.")

if __name__ == "__main__":
    main()