"""
Studi Kasus 1: Analisis Nilai Mahasiswa
Konsep: list comprehension, lambda, filtering, dan sorting.
"""

data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dimas", "nim": "230104", "tugas": 78, "uts": 82, "uas": 80},
    {"nama": "Eka", "nim": "230105", "tugas": 95, "uts": 92, "uas": 96},
    {"nama": "Farhan", "nim": "230106", "tugas": 80, "uts": 75, "uas": 78},
]

BOBOT_TUGAS = 0.30
BOBOT_UTS = 0.30
BOBOT_UAS = 0.40

# Transformasi data dan perhitungan nilai akhir menggunakan list comprehension.
hasil_analisis = [
    {
        **mahasiswa,
        "nilai_akhir": round(
            mahasiswa["tugas"] * BOBOT_TUGAS
            + mahasiswa["uts"] * BOBOT_UTS
            + mahasiswa["uas"] * BOBOT_UAS,
            2,
        ),
    }
    for mahasiswa in data_mahasiswa
]

# Mahasiswa berprestasi: nilai akhir di atas 80.
mahasiswa_berprestasi = list(
    filter(lambda m: m["nilai_akhir"] > 80, hasil_analisis)
)

# Ranking dari nilai tertinggi ke terendah.
ranking = sorted(
    hasil_analisis, key=lambda m: m["nilai_akhir"], reverse=True
)

print("=" * 68)
print("              SISTEM ANALISIS NILAI MAHASISWA")
print("=" * 68)
print(f"{'No':<4}{'Nama':<14}{'NIM':<12}{'Tugas':>8}{'UTS':>8}{'UAS':>8}{'Akhir':>10}")
print("-" * 68)
for nomor, m in enumerate(ranking, start=1):
    print(
        f"{nomor:<4}{m['nama']:<14}{m['nim']:<12}"
        f"{m['tugas']:>8}{m['uts']:>8}{m['uas']:>8}{m['nilai_akhir']:>10.2f}"
    )

print("\nMAHASISWA BERPRESTASI (NILAI AKHIR > 80)")
for m in mahasiswa_berprestasi:
    print(f"- {m['nama']} ({m['nim']}): {m['nilai_akhir']:.2f}")

terbaik = ranking[0]
print("\nMAHASISWA TERBAIK")
print(f"Nama        : {terbaik['nama']}")
print(f"NIM         : {terbaik['nim']}")
print(f"Nilai Tugas : {terbaik['tugas']}")
print(f"Nilai UTS   : {terbaik['uts']}")
print(f"Nilai UAS   : {terbaik['uas']}")
print(f"Nilai Akhir : {terbaik['nilai_akhir']:.2f}")
print("=" * 68)
