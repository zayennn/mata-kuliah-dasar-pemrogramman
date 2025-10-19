print("\n=============== check nilai =============== \n")

mahasiswa = [
    {"nama": "Alice", "nim": "12345", "jurusan": "Informatika"},
    {"nama": "Bob", "nim": "67890", "jurusan": "Sistem Informasi"},
    {"nama": "Charlie", "nim": "54321", "jurusan": "Teknik Komputer"},
    {"nama": "Diana", "nim": "98765", "jurusan": "Ilmu Komputer"},
]

for i, msh in enumerate(mahasiswa, start=1):
    print(
        f""" 
    {i}. nama mahasiswa : {msh['nama']},
       nim mahasiswa : {msh['nim']},
       jurusan : {msh['jurusan']}\n"""
    )

nilai = int(input("masukan nilai mahasiswa : "))

def grade(n):
    return (
        "masukan nilai yang valid antara 0 - 100" if n < 0 or n > 100 else
        "nilai mahasiswa : A" if n >= 80 else
        "nilai mahasiswa : B" if n > 70 else
        "nilai mahasiswa : C" if n > 60 else
        "nilai mahasiswa : D" if n > 30 else
        "nilai mahasiswa : E"
    )

print(grade(nilai))



