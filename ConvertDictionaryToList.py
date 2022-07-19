#!/usr/bin/env python3


# Convert Dictionary To List
Dictionary={"Nama:":"Ruben Leonardo Sigalingging",
"Hobby:":"Learn Computer Science",
"Message":"Use Your Imagination To Learn Computer Science",
"Married:":True,
"Favorite Movies:":["Unbreakable","The Expendables 2","The Expendables"]
}
print(f"Tipe Data Awal: {type(Dictionary)}")


# Convert Dictionary To List
Dictionary=list(Dictionary)
print(f"Tipe Data Sesudah Dikonversi: {type(Dictionary)}")
print(Dictionary)
print(f"Nilai Index Ke-3: {Dictionary[3]}")


# UBAH NILAI INDEX KE-3:
Dictionary[3]="Menikah!"
print(Dictionary)
print(f"Nilai Index Ke-3, Setelah Diubah: {Dictionary[3]}")