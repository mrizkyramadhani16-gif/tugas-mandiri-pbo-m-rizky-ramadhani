"""
Studi Kasus 2: Streaming Data Sensor IoT
Konsep: generator, yield, iterator, dan efisiensi memori.
"""

def baca_sensor(jumlah_data=10):
    """Menghasilkan data suhu satu per satu, bukan membuat list besar."""
    suhu_sensor = [18.5, 19.8, 20.0, 22.4, 25.6, 29.9, 30.0, 31.2, 34.7, 37.5]
    for indeks in range(jumlah_data):
        # Simulasi pembacaan bertahap; yield mengembalikan satu data setiap diminta.
        yield suhu_sensor[indeks % len(suhu_sensor)]


def kategorikan_suhu(suhu):
    if suhu < 20:
        return "Dingin"
    if suhu <= 30:
        return "Normal"
    return "Panas"


def main():
    print("=" * 52)
    print("          MONITORING SUHU SENSOR IoT")
    print("=" * 52)
    print(f"{'Pembacaan':<14}{'Suhu':<14}{'Status'}")
    print("-" * 52)

    # Objek generator adalah iterator; data dikonsumsi satu per satu.
    data_stream = baca_sensor(10)
    nomor = 1
    while True:
        try:
            suhu = next(data_stream)
        except StopIteration:
            break

        status = kategorikan_suhu(suhu)
        print(f"{nomor:<14}{suhu:>5.1f} °C{'':<7}{status}")
        nomor += 1

    print("-" * 52)
    print("Selesai: 10 data sensor telah diproses secara bertahap.")
    print("=" * 52)


if __name__ == "__main__":
    main()
