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
    

