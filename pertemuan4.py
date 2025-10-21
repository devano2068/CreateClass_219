class PersegiPanjang:
    def _init_(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def luas(self):
        return self.panjang * self.lebar
    
    def _str_(self):
        return f"Persegi Panjang, Panjang {self.panjang} cm,dan lebar {self.lebar} cm"
    

try:
    panjang_input = int(input("Masukkan panjang (cm):"))
    lebar_input = int(input("Masukkan lebar (cm):"))

    pp = PersegiPanjang(panjang_input, lebar_input)
    print("Keliling:", pp.keliling(), "cm")
    print("Luas:", pp.luas(), "cm^2")

except ValueError:
        print("Input harus berupa angka.")