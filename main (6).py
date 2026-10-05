"""
Studi Kasus 3: Sistem Keamanan Akun dan Audit Log Login
Konsep: RegEx, @property, decorator, closure, dan audit log.
"""

import re
from datetime import datetime


class User:
    """Menyimpan kredensial dengan validasi dan enkapsulasi."""

    def __init__(self, username, password):
        self._username = None
        self._password = None
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9]{5,}", value):
            raise ValueError("Username minimal 5 karakter dan hanya boleh huruf/angka.")
        self._username = value

    @property
    def password(self):
        # Password tidak ditampilkan secara langsung.
        return "********" if self._password is not None else None

    @password.setter
    def password(self, value):
        if not isinstance(value, str) or not re.fullmatch(r"(?=.*\d).{8,}", value):
            raise ValueError("Password minimal 8 karakter dan wajib mengandung angka.")
        self._password = value

    def cocokkan_password(self, password):
        return self._password == password


def audit_log(fungsi_login):
    """Decorator dengan closure untuk mencatat setiap percobaan login."""
    def wrapper(user, password):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            hasil = fungsi_login(user, password)
            status = "BERHASIL" if hasil else "DITOLAK"
            alasan = "" if hasil else "Password tidak cocok."
            print(f"[{waktu}] {user.username} | {status}" +
                  (f" | Alasan: {alasan}" if alasan else ""))
            return hasil
        except (ValueError, AttributeError) as error:
            nama = user if isinstance(user, str) else getattr(user, "username", "Tidak diketahui")
            print(f"[{waktu}] {nama} | DITOLAK | Alasan: {error}")
            return False
    return wrapper


@audit_log
def login(user, password):
    """Logika autentikasi sederhana untuk demonstrasi tugas."""
    if not isinstance(user, User):
        raise ValueError("Objek pengguna tidak valid.")
    return user.cocokkan_password(password)


def main():
    print("=" * 68)
    print("             SISTEM KEAMANAN AKUN & AUDIT LOG")
    print("=" * 68)

    print("\n[1] Pengujian username tidak valid")
    login("riz", "Rahasia123")

    print("\n[2] Pengujian password terlalu pendek")
    try:
        User("rizky123", "abc12")
    except ValueError as error:
        print(f"DITOLAK | Alasan: {error}")

    print("\n[3] Pengujian password tanpa angka")
    try:
        User("rizky123", "passwordku")
    except ValueError as error:
        print(f"DITOLAK | Alasan: {error}")

    print("\n[4] Pengujian login sukses")
    pengguna = User("rizky123", "Rahasia123")
    login(pengguna, "Rahasia123")

    print("\n[5] Pengujian password login salah")
    login(pengguna, "Salah1234")

    print("=" * 68)


if __name__ == "__main__":
    main()
