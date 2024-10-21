#--------TURN-BASED GAME AUTO BATTLE SIMULATION--------#

#--------IMPORT--------#
from tabulate import tabulate
import random

#--------HEADER TABULATE--------#
headers = ["ID", "Name", "Profile", "ATK", "HP", "DEF"]

#--------DATA OF CHARACTERS,WEAPONS, OFF-HAND WEAPONS, ARMOR, MONSTERS--------#
#----CHARACTERS----#
Character = {
"LS": {
    "Name"              : "Lyra Stormwind",
    "Profile"           : "Elven Bard",
    "Attack"            : 70,
    "HP"                : 130,
    "Defense"           : 55,
},
"GS": {
    "Name"              : "Grimlock Steelhammer",
    "Profile"           : "Dwarven Paladin",
    "Attack"            : 65,
    "HP"                : 160,
    "Defense"           : 75,
},
"ZN": {
    "Name"              : "Zara Nightshade",
    "Profile"           : "Human Assassin",
    "Attack"            : 75,
    "HP"                : 120,
    "Defense"           : 60,
},
"CF": {
    "Name"              : "Cyrus Flamecaller",
    "Profile"           : "Gnome Pyromancer",
    "Attack"            : 80,
    "HP"                : 110,
    "Defense"           : 50,
},
"BS": {
    "Name"              : "Branka Skullcrusher",
    "Profile"           : "Half-Orc Barbarian",
    "Attack"            : 85,
    "HP"                : 150,
    "Defense"           : 65,
}
}

#----WEAPONS----#
Weapons = {
"TB": {
    "Name"              : "Thunderbolt",
    "Profile"           : "A crackling lightning-imbued sword",
    "Attack"            : 5,
    "HP"                : 2,
    "Defense"           : 0,
},
"WB": {
    "Name"              : "Whisperwind Bow",
    "Profile"           : "An enchanted bow that fires silent arrows",
    "Attack"            : 4,
    "HP"                : 4,
    "Defense"           : 1,
},
"FD": {
    "Name"              : "Frostbite Dagger",
    "Profile"           : "A dagger that freezes enemies on contact",
    "Attack"            : 3,
    "HP"                : 6,
    "Defense"           : 2,
},
"SR": {
    "Name"              : "Soulreaver Axe",
    "Profile"           : "A massive axe that drains life force",
    "Attack"            : 7,
    "HP"                : -2,
    "Defense"           : 0,
},
"SA": {
    "Name"              : "Staff of the Ancients",
    "Profile"           : "A powerful magical staff with ancient runes",
    "Attack"            : 4,
    "HP"                : 6,
    "Defense"           : 1,
}
}

#---- OFF-HAND WEAPONS ----#
OffHandWeapons = {
"AS": {
    "Name"              : "Aegis Shield",
    "Profile"           : "A sturdy shield with a magical barrier",
    "Attack"            : 0,
    "HP"                : 8,
    "Defense"           : 4,
},
"SD": {
    "Name"              : "Shadowcloak Dagger",
    "Profile"           : "A small dagger that grants stealth",
    "Attack"            : 2,
    "HP"                : 4,
    "Defense"           : 3,
},
"TA": {
    "Name"              : "Tome of Arcane Secrets",
    "Profile"           : "A spellbook that enhances magical abilities",
    "Attack"            : 3,
    "HP"                : 6,
    "Defense"           : 2,
},
"OR": {
    "Name"              : "Orb of Radiance",
    "Profile"           : "A glowing orb that emits blinding light",
    "Attack"            : 2,
    "HP"                : 8,
    "Defense"           : 3,
},
"TB": {
    "Name"              : "Thornguard Buckler",
    "Profile"           : "A small shield covered in sharp thorns",
    "Attack"            : 1,
    "HP"                : 6,
    "Defense"           : 4,
}
}

#----ARMORS----#
Armor = {
"DB": {
    "Name"              : "Dragonscale Breastplate",
    "Profile"           : "Armor forged from dragon scales",
    "Attack"            : 0,
    "HP"                : 10,
    "Defense"           : 5,
},
"SC": {
    "Name"              : "Shadowweave Cloak",
    "Profile"           : "A cloak that bends light around the wearer",
    "Attack"            : 1,
    "HP"                : 8,
    "Defense"           : 4,
},
"IC": {
    "Name"              : "Ironbark Cuirass",
    "Profile"           : "Chest armor made from enchanted wood",
    "Attack"            : 0,
    "HP"                : 8,
    "Defense"           : 5,
},
"SF": {
    "Name"              : "Sunfire Robes",
    "Profile"           : "Robes imbued with the power of the sun",
    "Attack"            : 2,
    "HP"                : 6,
    "Defense"           : 3,
},
"FP": {
    "Name"              : "Frostforged Plate",
    "Profile"           : "Armor tempered in magical ice",
    "Attack"            : 0,
    "HP"                : 10,
    "Defense"           : 5,
}
}

#----MONSTERS----#
Monster = {
"SM": {
    "Name"              : "Shadowmaw",
    "Profile"           : "Dire Bear",
    "Attack"            : 80,
    "HP"                : 180,
    "Defense"           : 70,
},
"FF": {
    "Name"              : "Frostfang",
    "Profile"           : "Ice Wyrm",
    "Attack"            : 85,
    "HP"                : 160,
    "Defense"           : 75,
},
"TH": {
    "Name"              : "Thornhide",
    "Profile"           : "Ancient Treant",
    "Attack"            : 75,
    "HP"                : 200,
    "Defense"           : 85,
},
"VW": {
    "Name"              : "Voidwalker",
    "Profile"           : "Shadow Demon",
    "Attack"            : 90,
    "HP"                : 140,
    "Defense"           : 65,
},
"IB": {
    "Name"              : "Ironhide Behemoth",
    "Profile"           : "Armored Rhino",
    "Attack"            : 70,
    "HP"                : 220,
    "Defense"           : 90,
}
}

#--------INISIASI PENAMBAHAN DATA, PEMILIHAN KARAKTER DAN LAWAN--------#
EquippedCharacter = {} #{Nama, ATK, HP, DEF}
Opponent = {} #{Nama, ATK, HP, DEF}
AddSomething = {} ##{ID, Nama, Profile, ATK, HP, DEF}

#--------TAMPILKAN TABEL KARAKTER--------#
def CharacterList():
    if bool(Character)==True:
        print(f"===Character Lists===")
        print(tabulate([[name, *inner.values()] for name, inner in Character.items()], headers, tablefmt="fancy_outline"))
    else :
        print("Data karakter tidak ditemukan!")

#--------TAMPILKAN TABEL SENJATA--------#
def WeaponList():
    if bool(Weapons)==True:
        print(f"===Weapon Lists===")
        print(tabulate([[name, *inner.values()] for name, inner in Weapons.items()], headers, tablefmt="fancy_outline"))
    else :
        print("Data senjata tidak ditemukan!")

#--------TAMPILKAN TABEL SENJATA TANGAN KOSONG--------#
def OffHandWeaponList():
    if bool(OffHandWeapons)==True:
        print(f"===Off-hand Weapon Lists===")
        print(tabulate([[name, *inner.values()] for name, inner in OffHandWeapons.items()], headers, tablefmt="fancy_outline"))
    else :
        print("Data senjata tangan kosong tidak ditemukan!")

#--------TAMPILKAN TABEL ARMOR--------#
def ArmorList():
    if bool(Armor)==True:
        print(f"===Armor Lists===")
        print(tabulate([[name, *inner.values()] for name, inner in Armor.items()], headers, tablefmt="fancy_outline"))
    else :
        print("Data armor tidak ditemukan!")

#--------TAMPILKAN TABEL MONSTER--------#
def MonsterList():
    if bool(Monster)==True:
        print(f"===Monster Lists===")
        print(tabulate([[name, *inner.values()] for name, inner in Monster.items()], headers, tablefmt="fancy_outline"))
    else :
        print("Data monster tidak ditemukan!")

#--------TAMPILKAN SEMUA TABEL, TABEL TERTENTU, ATAU DATA SPESIFIK --------#
def StatList():
    #----TAMPILAN MENU----#
    print("""
          ====Stat Karakter, Perlengkapan, dan Monster====
          
          Silahkan pilih yang ingin anda lakukan : 
          1. Lihat Stat Semua
          2. Lihat Stat Karakter
          3. Lihat Stat Perlengkapan
          4. Lihat Stat Monster
          5. Lihat Stat Karakter Tertentu
          6. Lihat Stat Senjata Tertentu
          7. Lihat Stat Senjata Tangan Kosong Tertentu
          8. Lihat Stat Armor Tertentu          
          9. Lihat Stat Monster Tertentu
          10. Kembali ke Menu Awal
          """)
    
    #----INISIASI----#
    Opsi1 = 0

    #----PEMILIHAN OPSI----#
    while Opsi1!=10:
        try:
            Opsi1 = int(input("Masukkan angka menu yang ingin dijalankan : "))
            #--LIHAT STAT SEMUA--#
            if Opsi1==1:
                CharacterList()
                WeaponList()
                OffHandWeaponList()
                ArmorList()
                MonsterList()
                return StatList()
            #--LIHAT STAT KARAKTER--#
            elif Opsi1==2:
                CharacterList()
                return StatList()
            #--LIHAT STAT PERLENGKAPAN--#
            elif Opsi1==3:
                WeaponList()
                OffHandWeaponList()
                ArmorList()
                return StatList()
            #--LIHAT STAT MONSTER--#
            elif Opsi1==4:
                MonsterList()
                return StatList()
            #--LIHAT STAT KARAKTER TERTENTU--#
            elif Opsi1==5:
                if bool(Character)==True:
                    input1= input("Masukkan ID karakter yang ingin anda cari : ").upper()
                    if input1 in Character:
                        print(f"===Character Lists===")
                        CekInput = {input1 : Character[input1]}
                        print(tabulate([[name, *inner.values()] for name, inner in CekInput.items()], headers, tablefmt="fancy_outline"))
                        return StatList()
                    else :
                        print("Karakter tidak tersedia")
                        return StatList()
                else :
                    print("Data karakter tidak ditemukan!")
                    return StatList()
            #--LIHAT STAT SENJATA TERTENTU--#
            elif Opsi1==6:
                if bool(Weapons)==True:
                    input1= input("Masukkan ID senjata yang ingin anda cari : ").upper()
                    if input1 in Weapons:
                        CekInput = {input1 : Weapons[input1]}
                        print(tabulate([[name, *inner.values()] for name, inner in CekInput.items()], headers, tablefmt="fancy_outline"))
                        return StatList()
                    else :
                        print("Senjata Tidak Tersedia")
                        return StatList()
                else :
                    print("Data senjata tidak ditemukan!")
                    return StatList()
            #--LIHAT STAT SENJATA TANGAN KOSONG TERTENTU--#
            elif Opsi1==7:
                if bool(OffHandWeapons)==True:
                    input1= input("Masukkan ID senjata tangan kosong yang ingin anda cari : ").upper()
                    if input1 in OffHandWeapons:
                        CekInput = {input1 : OffHandWeapons[input1]}
                        print(tabulate([[name, *inner.values()] for name, inner in CekInput.items()], headers, tablefmt="fancy_outline"))
                        return StatList()
                    else :
                        print("Senjata Tangan Kosong Tidak Tersedia")
                        return StatList()
                else :
                    print("Data senjata tangan kosong tidak ditemukan!")
                    return StatList()
            #--LIHAT STAT ARMOR TERTENTU--#
            elif Opsi1==8:
                if bool(Armor)==True:
                    input1= input("Masukkan ID armor yang ingin anda cari : ").upper()
                    if input1 in Armor:
                        CekInput = {input1 : Armor[input1]}
                        print(tabulate([[name, *inner.values()] for name, inner in CekInput.items()], headers, tablefmt="fancy_outline"))
                        return StatList()
                    else :
                        print("Armor Tidak Tersedia")
                        return StatList()
                else :
                    print("Data armor tidak ditemukan!")
                    return StatList()
            #--LIHAT STAT MONSTER TERTENTU--#
            elif Opsi1==9:
                if bool(Monster)==True:
                    input1= input("Masukkan ID monster yang ingin anda cari : ").upper()
                    if input1 in Monster:
                        CekInput = {input1 : Weapons[input1]}
                        print(tabulate([[name, *inner.values()] for name, inner in CekInput.items()], headers, tablefmt="fancy_outline"))
                        return StatList()
                    else :
                        print("Monster Tidak Tersedia")
                        return StatList()
                else :
                    print("Data monster tidak ditemukan")
                    return StatList()
            #--KEMBALI KE MAIN MENU--#
            elif Opsi1==10:
                return
            else:
                print("Masukkan angka yang tersedia!")
                return StatList()
        except :
            print("Tolong masukkan format angka!")
            return StatList()

#--------FUNGSI PENAMBAHAN STAT--------#
def Adding():
    ListTambahan = {"Name" : "","Profile" : "", "Attack" : 0, "HP" : 0, "Defense" : 0}
    ListTambahan["Name"] += input("Masukkan nama yang ingin ditambahkan : ")
    ListTambahan["Profile"] += input("Masukkan profil yang ingin ditambahkan : ")
    while True:
        try:
            ListTambahan["Attack"] += int(input("Masukkan Attack yang ingin ditambahkan : "))
        except:
            print("Tolong Masukkan Angka!")
            continue
        while True:
            try:
                ListTambahan["HP"] += int(input("Masukkan HP yang ingin ditambahkan : "))
            except:
                print("Tolong Masukkan Angka!")
                continue
            while True:
                try:                 
                    ListTambahan["Defense"]+= int(input("Masukkan Defense yang ingin ditambahkan : "))
                    AddSomething.clear()
                    AddSomething.update(ListTambahan)
                    return
                except:
                    print("Tolong Masukkan Angka!")
                    continue


#--------PENAMBAHAN KARAKTER, PERLENGKAPAN, DAN MONSTER--------#
def AddList():
    print("""
          ====Menambahkan Karakter, Perlengkapan, atau Monster====
          
          Silahkan pilih yang ingin anda lakukan : 
          1. Menambahkan Karakter
          2. Menambahkan Senjata
          3. Menambahkan Senjata Tangan Kosong
          4. Menambahkan Armor
          5. Menambahkan Monster
          6. Kembali ke Main Menu
          """)

    #----INISIASI----#
    Opsi2=0
    
    #----PEMILIHAN OPSI----#
    while Opsi2!=6:
        try:
            Opsi2 = int(input("Masukkan angka menu yang ingin dijalankan : "))
            #--PENAMBAHAN KARAKTER--#
            if Opsi2==1:
                #--PENGECEKAN ID--#
                input2 = input("Masukkan ID karakter yang ingin ditambahkan : ").upper()
                if input2 in Character:
                    print("Karakter sudah tersedia")
                    return AddList()
                else :
                    Adding()
                    DataPreUpdate = {input2 : AddSomething}
                    print(tabulate([[name, *inner.values()] for name, inner in DataPreUpdate.items()], headers, tablefmt="fancy_outline"))
                    SaveData= input("Apakah anda sudah yakin (ya/tidak)? ").lower()
                    if SaveData=="ya":
                        Character.update({input2 : AddSomething})
                        print("Karakter sudah dibuat!")
                        CharacterList()
                        return AddList()
                    elif SaveData=="tidak":
                        return AddList()
                    else:
                        print("""
                        Input yang dimasukkan tidak sesuai!
                        Program akan kembali ke menu sebelumnya
                        """)
                        return AddList()
                        
            #--PENAMBAHAN SENJATA--#
            if Opsi2==2:
                #--PENGECEKAN ID--#
                input2 = input("Masukkan ID senjata yang ingin ditambahkan : ").upper()
                if input2 in Weapons:
                    print("Senjata sudah tersedia")
                    return AddList()
                else :                
                    Adding()
                    DataPreUpdate = {input2 : AddSomething}
                    print(tabulate([[name, *inner.values()] for name, inner in DataPreUpdate.items()], headers, tablefmt="fancy_outline"))
                    SaveData= input("Apakah anda sudah yakin (ya/tidak)? ").lower()
                    if SaveData=="ya":
                        Weapons.update({input2 : AddSomething})
                        print("Senjata sudah dibuat!")
                        WeaponList()
                        return AddList()
                    elif SaveData=="tidak":
                        return AddList()
                    else:
                        print("""
                        Input yang dimasukkan tidak sesuai!
                        Program akan kembali ke menu sebelumnya
                        """)
                        return AddList()
            #--PENAMBAHAN SENJATA TANGAN KOSONG--#
            if Opsi2==3:
                #--PENGECEKAN ID--#
                input2 = input("Masukkan ID senjata tangan kosong yang ingin ditambahkan : ").upper()
                if input2 in OffHandWeapons:
                    print("Senjata Tangan Kosong sudah tersedia")
                    return AddList()
                else :         
                    Adding()
                    DataPreUpdate = {input2 : AddSomething}
                    print(tabulate([[name, *inner.values()] for name, inner in DataPreUpdate.items()], headers, tablefmt="fancy_outline"))
                    SaveData= input("Apakah anda sudah yakin (ya/tidak)? ").lower()
                    if SaveData=="ya":
                        OffHandWeapons.update({input2 : AddSomething})
                        print("Senjata tangan kosong sudah dibuat!")
                        OffHandWeaponList()
                        return AddList()
                    elif SaveData=="tidak":
                        return AddList()
                    else:
                        print("""
                        Input yang dimasukkan tidak sesuai!
                        Program akan kembali ke menu sebelumnya
                        """)
                        return AddList()
            #--PENAMBAHAN ARMOR--#
            if Opsi2==4:
                #--PENGECEKAN ID--#
                input2 = input("Masukkan ID armor yang ingin ditambahkan : ").upper()
                if input2 in Armor:
                    print("Armor sudah tersedia")
                    return AddList()
                else:
                    Adding()
                    DataPreUpdate = {input2 : AddSomething}
                    print(tabulate([[name, *inner.values()] for name, inner in DataPreUpdate.items()], headers, tablefmt="fancy_outline"))
                    SaveData= input("Apakah anda sudah yakin (ya/tidak)? ").lower()
                    if SaveData=="ya":
                        Armor.update({input2 : AddSomething})
                        print("Armor sudah dibuat!")
                        ArmorList()
                        return AddList()
                    elif SaveData=="tidak":
                        return AddList()
                    else:
                        print("""
                        Input yang dimasukkan tidak sesuai!
                        Program akan kembali ke menu sebelumnya
                        """)
                        return AddList()
            #--PENAMBAHAN MONSTER--#
            if Opsi2==5:
                #--PENGECEKAN ID--#
                input2 = input("Masukkan ID monster yang ingin ditambahkan : ").upper()
                if input2 in Monster:
                    print("Monster sudah tersedia")
                    return AddList()
                else:
                    Adding()
                    DataPreUpdate = {input2 : AddSomething}
                    print(tabulate([[name, *inner.values()] for name, inner in DataPreUpdate.items()], headers, tablefmt="fancy_outline"))
                    SaveData= input("Apakah anda sudah yakin (ya/tidak)? ").lower()
                    if SaveData=="ya":
                        Monster.update({input2 : AddSomething})
                        print("Monster sudah dibuat!")
                        MonsterList()
                        return AddList()
                    elif SaveData=="tidak":
                        return AddList()
                    else:
                        print("""
                        Input yang dimasukkan tidak sesuai!
                        Program akan kembali ke menu sebelumnya
                        """)
                        return AddList()
            #--KEMBALI KE MAIN MENU--#
            if Opsi2==6:
                return
            else :
                print("Tolong masukkan angka yang tersedia!")
                return AddList()
        except:
            print("Tolong masukkan format yang benar!")
            return AddList()

#--------PENGHAPUSAN KARAKTER, PERLENGKAPAN, DAN MONSTER--------#
def RemoveList():
    print("""
        ====Menghapus Karakter, Perlengkapan, atau Monster====
        
        Silahkan pilih yang ingin anda lakukan : 
        1. Menghapus Karakter Tertentu
        2. Menghapus Senjata Tertentu
        3. Menghapus Senjata Tangan Kosong Tertentu
        4. Menghapus Armor Tertentu
        5. Menghapus Monster Tertentu
        6. Menghapus Semua Karakter
        7. Menghapus Semua Senjata
        8. Menghapus Semua Senjata Tangan Kosong
        9. Menghapus Semua Armor
        10. Menghapus Semua Monster
        11. Kembali ke Main Menu
        """)
    
    #----INISIASI----#
    Opsi3=0

    #----PEMILIHAN OPSI----#
    while Opsi3!=6:
        try:
            Opsi3= int(input("Masukkan angka menu yang ingin dijalankan : "))
            #--PENGHAPUSAN KARAKTER--#
            if Opsi3==1:
                if bool(Character)==True:
                    CharacterList()
                    input3 = input("Masukkan ID karakter yang ingin dihapus : ")
                    if input3.upper() in Character:
                        CekInput = {input3 : Character[input3]}
                        print(tabulate([[name, *inner.values()] for name, inner in CekInput.items()], headers, tablefmt="fancy_outline"))
                        SaveData = input("Apakah anda yakin ingin menghapus karakter tersebut (ya/tidak)? ")
                        if SaveData.lower()=="ya":
                            Character.pop(input3.upper())
                            print("Karakter berhasil dihapus!")
                            CharacterList()
                            return RemoveList()
                        elif SaveData.lower()=="tidak":
                            return RemoveList()
                        else:
                            print("""
                            Input yang dimasukkan tidak sesuai!
                            Program akan kembali ke menu sebelumnya
                            """)
                            return RemoveList()
                    else:
                        print("Karakter tidak tersedia")
                        return RemoveList()
                else :
                    print("Tidak ada karakter yang dapat dihapus!")
                    return RemoveList()
            #--PENGHAPUSAN SENJATA--#
            elif Opsi3==2:
                if bool(Weapons)==True:
                    WeaponList()
                    input3 = input("Masukkan ID senjata yang ingin dihapus : ")
                    if input3.upper() in Weapons:
                        CekInput = {input3 : Weapons[input3]}
                        print(tabulate([[name, *inner.values()] for name, inner in CekInput.items()], headers, tablefmt="fancy_outline"))
                        SaveData = input("Apakah anda yakin ingin menghapus senjata tersebut (ya/tidak)? ")
                        if SaveData.lower()=="ya":
                            Weapons.pop(input3.upper())
                            print("Senjata berhasil dihapus!")
                            WeaponList()
                            return RemoveList()
                        elif SaveData.lower()=="tidak":
                            return RemoveList()
                        else:
                            print("""
                            Input yang dimasukkan tidak sesuai!
                            Program akan kembali ke menu sebelumnya
                            """)
                            return RemoveList()
                    else:
                        print("Senjata tidak tersedia")
                        return RemoveList()
                else :
                    print("Tidak ada senjata yang dapat dihapus!")
                    return RemoveList()
            #--PENGHAPUSAN SENJATA TANGAN KOSONG--#
            elif Opsi3==3:
                if bool(OffHandWeapons)==True:
                    OffHandWeaponList()
                    input3 = input("Masukkan ID senjata tangan kosong yang ingin dihapus : ")
                    if input3.upper() in OffHandWeapons:
                        CekInput = {input3 : OffHandWeapons[input3]}
                        print(tabulate([[name, *inner.values()] for name, inner in CekInput.items()], headers, tablefmt="fancy_outline"))
                        SaveData = input("Apakah anda yakin ingin menghapus senjata tangan kosong tersebut (ya/tidak)? ")
                        if SaveData.lower()=="ya":
                            OffHandWeapons.pop(input3.upper())
                            print("Senjata tangan kosong berhasil dihapus!")
                            OffHandWeaponList()
                            return RemoveList()
                        elif SaveData.lower()=="tidak":
                            return RemoveList()
                        else:
                            print("""
                            Input yang dimasukkan tidak sesuai!
                            Program akan kembali ke menu sebelumnya
                            """)
                            return RemoveList()
                    else:
                        print("Senjata tangan kosong tidak tersedia")
                        return RemoveList()
                else :
                    print("Tidak ada senjata tangan kosong yang dapat dihapus!")
                    return RemoveList()
            #--PENGHAPUSAN ARMOR--#
            elif Opsi3==4:
                if bool(Armor)==True:
                    ArmorList()
                    input3 = input("Masukkan ID armor yang ingin : ")
                    if input3.upper() in Armor:
                        CekInput = {input3 : Armor[input3]}
                        print(tabulate([[name, *inner.values()] for name, inner in CekInput.items()], headers, tablefmt="fancy_outline"))
                        SaveData = input("Apakah anda yakin ingin menghapus armor tersebut (ya/tidak)? ")
                        if SaveData.lower()=="ya":
                            Armor.pop(input3.upper())
                            print("Armor berhasil dihapus!")
                            ArmorList()
                            return RemoveList()
                        elif SaveData.lower()=="tidak":
                            return RemoveList()
                        else:
                            print("""
                            Input yang dimasukkan tidak sesuai!
                            Program akan kembali ke menu sebelumnya
                            """)
                            return RemoveList()
                    else:
                        print("Armor tidak tersedia")
                        return RemoveList()
                else :
                    print("Tidak ada armor yang dapat dihapus!")
                    return RemoveList()
            #--PENGHAPUSAN MONSTER--#
            elif Opsi3==5:
                if bool(Monster)==True:
                    MonsterList()
                    input3 = input("Masukkan ID monster yang ingin dihapus : ")
                    if input3.upper() in Monster:
                        CekInput = {input3 : Monster[input3]}
                        print(tabulate([[name, *inner.values()] for name, inner in CekInput.items()], headers, tablefmt="fancy_outline"))
                        SaveData = input("Apakah anda yakin ingin menghapus monster tersebut (ya/tidak)? ")
                        if SaveData.lower()=="ya":
                            Monster.pop(input3.upper())
                            print("Monster berhasil dihapus!")
                            MonsterList()
                            return RemoveList()
                        elif SaveData.lower()=="tidak":
                            return RemoveList()
                        else:
                            print("""
                            Input yang dimasukkan tidak sesuai!
                            Program akan kembali ke menu sebelumnya
                            """)
                            return RemoveList()
                    else:
                        print("Monster tidak tersedia")
                        return RemoveList()
                else :
                    print("Tidak ada monster yang dapat dihapus!")
                    return RemoveList()
            #--PENGHAPUSAN SEMUA KARAKTER--#
            elif Opsi3==6:
                if bool(Character)==True:
                    CharacterList()
                    SaveData = input("Apakah anda yakin ingin menghapus semua karakter (ya/tidak)? ")
                    if SaveData.lower()=="ya":
                        Character.clear()
                        return RemoveList()
                    elif SaveData.lower()=="tidak":
                        return RemoveList()
                    else:
                        print("""
                        Input yang dimasukkan tidak sesuai!
                        Program akan kembali ke menu sebelumnya
                        """)
                        return RemoveList()
                else :
                    print("Tidak ada karakter yang dapat dihapus!")
            #--PENGHAPUSAN SEMUA SENJATA--#
            elif Opsi3==7:
                if bool(Weapons)==True:
                    WeaponList()
                    SaveData = input("Apakah anda yakin ingin menghapus semua senjata (ya/tidak)? ")
                    if SaveData.lower()=="ya":
                        Weapons.clear()
                        return RemoveList()
                    elif SaveData.lower()=="tidak":
                        return RemoveList()
                    else:
                        print("""
                        Input yang dimasukkan tidak sesuai!
                        Program akan kembali ke menu sebelumnya
                        """)
                        return RemoveList()
                else :
                    print("Tidak ada senjata yang dapat dihapus!")
            #--PENGHAPUSAN SEMUA SENJATA TANGAN KOSONG--#
            elif Opsi3==8:
                if bool(OffHandWeapons)==True:
                    OffHandWeaponList()
                    SaveData = input("Apakah anda yakin ingin menghapus semua senjata tangan kosong (ya/tidak)? ")
                    if SaveData.lower()=="ya":
                        OffHandWeapons.clear()
                        return RemoveList()
                    elif SaveData.lower()=="tidak":
                        return RemoveList()
                    else:
                        print("""
                        Input yang dimasukkan tidak sesuai!
                        Program akan kembali ke menu sebelumnya
                        """)
                        return RemoveList()
                else :
                    print("Tidak ada senjata tangan kosong yang dapat dihapus!")
            #--PENGHAPUSAN SEMUA ARMOR--#
            elif Opsi3==9:
                if bool(Armor)==True:
                    ArmorList()
                    SaveData = input("Apakah anda yakin ingin menghapus semua armor (ya/tidak)? ")
                    if SaveData.lower()=="ya":
                        Armor.clear()
                        return RemoveList()
                    elif SaveData.lower()=="tidak":
                        return RemoveList()
                    else:
                        print("""
                        Input yang dimasukkan tidak sesuai!
                        Program akan kembali ke menu sebelumnya
                        """)
                        return RemoveList()
                else :
                    print("Tidak ada armor yang dapat dihapus!")
            #--PENGHAPUSAN SEMUA MONSTER--#
            elif Opsi3==10:
                if bool(Monster)==True:
                    MonsterList()
                    SaveData = input("Apakah anda yakin ingin menghapus semua monster (ya/tidak)? ")
                    if SaveData.lower()=="ya":
                        Monster.clear()
                        return RemoveList()
                    elif SaveData.lower()=="tidak":
                        return RemoveList()
                    else:
                        print("""
                        Input yang dimasukkan tidak sesuai!
                        Program akan kembali ke menu sebelumnya
                        """)
                        return RemoveList()
                else :
                    print("Tidak ada monster yang dapat dihapus!")
            #--KEMBALI KE MAIN MENU--#
            elif Opsi3==11:
                return
            else:
                print("Tolong masukkan angka yang tersedia!")
                return RemoveList()
        except:
            print("Tolong masukkan format yang benar!")
            return RemoveList()

#--------MELAKUKAN UPDATE KARAKTER, PERLENGKAPAN, DAN MONSTER--------#
def UpdateList():
    print("""
    ====Melakukan Update Karakter, Perlengkapan, atau Monster====
    
    Silahkan pilih yang ingin anda lakukan : 
    1. Melakukan Update Karakter
    2. Melakukan Update Senjata
    3. Melakukan Update Senjata Tangan Kosong
    4. Melakukan Update Armor
    5. Melakukan Update Monster
    6. Kembali ke Main Menu
    """)

    #----INISIASI----#
    Opsi4=0

    #----PEMILIHAN OPSI----#
    while Opsi4!=6:
        try:
            Opsi4=int(input("Masukkan angka menu yang ingin dijalankan : "))
            #--MELAKUKAN UPDATE KARAKTER--#
            if Opsi4==1:
                CharacterList()
                InputID = input("Masukkan ID karakter yang ingin dilakukan update : ")
                if InputID.upper() in Character:
                    CekInput = {InputID : Character[InputID.upper()]}
                    print(tabulate([[name, *inner.values()] for name, inner in CekInput.items()], headers, tablefmt="fancy_outline"))
                    input4 = input("Apakah anda yakin ingin melanjutkan update (ya/tidak)? ")
                    if input4.lower()=="ya":
                        InputAtribut= input("Silahkan pilih atribut yang ingin dilakukan update : ")
                        #-MENGUBAH ID-#
                        if InputAtribut.lower()=="id":
                            InputAtribut= input("Silahkan isi ID yang baru : ")
                            SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                            if SaveData.lower()=="ya":
                                    Character[InputAtribut]= Character.pop(InputID.upper())
                                    print("Karakter berhasil dilakukan update!")
                                    CharacterList()
                                    return UpdateList()
                            elif SaveData.lower()=="tidak":
                                return UpdateList()
                            else:
                                print("""
                                Input yang dimasukkan tidak sesuai!
                                Program akan kembali ke menu sebelumnya
                                """)
                                return UpdateList()
                        #-MENGUBAH NAMA-#
                        if InputAtribut.lower()=="name" or InputAtribut.lower()=="nama":
                            InputAtribut= input("Silahkan isi nama yang baru : ")
                            SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                            if SaveData.lower()=="ya":
                                Character[InputID.upper()]["Name"]= InputAtribut
                                print("Karakter berhasil dilakukan update!")
                                CharacterList()
                                return UpdateList()
                            elif SaveData.lower()=="tidak":
                                return UpdateList()
                            else:
                                print("""
                                Input yang dimasukkan tidak sesuai!
                                Program akan kembali ke menu sebelumnya
                                """)
                                return UpdateList()
                        #-MENGUBAH PROFILE-#
                        if InputAtribut.lower()=="profile" or InputAtribut.lower()=="profil":
                            InputAtribut= input("Silahkan isi profil yang baru : ")
                            SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                            if SaveData.lower()=="ya":
                                Character[InputID.upper()]["Profile"]= InputAtribut
                                print("Karakter berhasil dilakukan update!")
                                CharacterList()
                                return UpdateList()
                            elif SaveData.lower()=="tidak":
                                return UpdateList()
                            else:
                                print("""
                                Input yang dimasukkan tidak sesuai!
                                Program akan kembali ke menu sebelumnya
                                """)
                                return UpdateList()
                        #-MENGUBAH ATTACK-#
                        elif InputAtribut.lower()=="atk" or InputAtribut.lower()=="attack":
                            while True:
                                try:
                                    InputAtribut= int(input("Silahkan isi nilai ATK yang baru : "))
                                    SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                                    if SaveData.lower()=="ya":
                                        Character[InputID.upper()]["Attack"]= InputAtribut
                                        print("Karakter berhasil dilakukan update!")
                                        CharacterList()
                                        return UpdateList()
                                    elif SaveData.lower()=="tidak":
                                        return UpdateList()
                                    else:
                                        print("""
                                        Input yang dimasukkan tidak sesuai!
                                        Program akan kembali ke menu sebelumnya
                                        """)
                                        return UpdateList()
                                except:
                                    print("Nilai harus berupa bilangan bulat!")
                                    continue
                        #-MENGUBAH HP-#
                        elif InputAtribut.lower()=="hp":
                            while True:
                                try:
                                    InputAtribut= int(input("Silahkan isi nilai HP yang baru : "))
                                    SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                                    if SaveData.lower()=="ya":
                                        Character[InputID.upper()]["HP"]= InputAtribut
                                        print("Karakter berhasil dilakukan update!")
                                        CharacterList()
                                        return UpdateList()
                                    elif SaveData.lower()=="tidak":
                                        return UpdateList()
                                    else:
                                        print("""
                                        Input yang dimasukkan tidak sesuai!
                                        Program akan kembali ke menu sebelumnya
                                        """)
                                        return UpdateList()
                                except:
                                    print("Nilai harus berupa bilangan bulat!")
                                    continue
                        #-MENGUBAH DEFENSE-#
                        elif InputAtribut.lower()=="def" or InputAtribut.lower()=="defense": 
                            while True:
                                try:
                                    InputAtribut= int(input("Silahkan isi nilai DEF yang baru : "))
                                    SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                                    if SaveData.lower()=="ya":
                                        Character[InputID.upper()]["Defense"]= InputAtribut
                                        print("Karakter berhasil dilakukan update!")
                                        CharacterList()
                                        return UpdateList()
                                    elif SaveData.lower()=="tidak":
                                        return UpdateList()
                                    else:
                                        print("""
                                        Input yang dimasukkan tidak sesuai!
                                        Program akan kembali ke menu sebelumnya
                                        """)
                                        return UpdateList()
                                except:
                                    print("Nilai harus berupa bilangan bulat!")
                                    continue
                        else :
                            print("""
                            Atribut yang ingin diubah tidak tersedia!
                            Program akan kembali ke menu sebelumnya
                            """)
                    elif input4.lower()=="tidak":
                        return UpdateList()
                    else:
                        print("""
                        Input yang dimasukkan tidak sesuai!
                        Program akan kembali ke menu sebelumnya
                        """)
                        return UpdateList()
                else :
                    print("""
                    Karakter tidak tersedia!
                    Program akan kembali ke menu sebelumnya
                    """)
                    return UpdateList()
            #--MELAKUKAN UPDATE SENJATA--#
            elif Opsi4==2:
                WeaponList()
                InputID = input("Masukkan ID senjata yang ingin dilakukan update : ")
                if InputID.upper() in Weapons:
                    CekInput = {InputID : Weapons[InputID.upper()]}
                    print(tabulate([[name, *inner.values()] for name, inner in CekInput.items()], headers, tablefmt="fancy_outline"))
                    input4 = input("Apakah anda yakin ingin melanjutkan update (ya/tidak)? ")
                    if input4.lower()=="ya":
                        InputAtribut= input("Silahkan pilih atribut yang ingin dilakukan update : ")
                        #-MENGUBAH ID-#
                        if InputAtribut.lower()=="id":
                            InputAtribut= input("Silahkan isi ID yang baru : ")
                            SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                            if SaveData.lower()=="ya":
                                    Weapons[InputAtribut]= Weapons.pop(InputID.upper())
                                    print("Senjata berhasil dilakukan update!")
                                    WeaponList()
                                    return UpdateList()
                            elif SaveData.lower()=="tidak":
                                return UpdateList()
                            else:
                                print("""
                                Input yang dimasukkan tidak sesuai!
                                Program akan kembali ke menu sebelumnya
                                """)
                                return UpdateList()
                        #-MENGUBAH NAMA-#
                        if InputAtribut.lower()=="name" or InputAtribut.lower()=="nama":
                            InputAtribut= input("Silahkan isi nama yang baru : ")
                            SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                            if SaveData.lower()=="ya":
                                Weapons[InputID.upper()]["Name"]= InputAtribut
                                print("Senjata berhasil dilakukan update!")
                                WeaponList()
                                return UpdateList()
                            elif SaveData.lower()=="tidak":
                                return UpdateList()
                            else:
                                print("""
                                Input yang dimasukkan tidak sesuai!
                                Program akan kembali ke menu sebelumnya
                                """)
                                return UpdateList()
                        #-MENGUBAH PROFILE-#
                        if InputAtribut.lower()=="profile" or InputAtribut.lower()=="profil": # Mengubah Profile
                            InputAtribut= input("Silahkan isi profil yang baru : ")
                            SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                            if SaveData.lower()=="ya":
                                Weapons[InputID.upper()]["Profile"]= InputAtribut
                                print("Senjata berhasil dilakukan update!")
                                WeaponList()
                                return UpdateList()
                            elif SaveData.lower()=="tidak":
                                return UpdateList()
                            else:
                                print("""
                                Input yang dimasukkan tidak sesuai!
                                Program akan kembali ke menu sebelumnya
                                """)
                                return UpdateList()
                        #-MENGUBAH ATTACK-#
                        elif InputAtribut.lower()=="atk" or InputAtribut.lower()=="attack": # Mengubah Attack
                            while True:
                                try:
                                    InputAtribut= int(input("Silahkan isi nilai ATK yang baru : "))
                                    SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                                    if SaveData.lower()=="ya":
                                        Weapons[InputID.upper()]["Attack"]= InputAtribut
                                        print("Senjata berhasil dilakukan update!")
                                        WeaponList()
                                        return UpdateList()
                                    elif SaveData.lower()=="tidak":
                                        return UpdateList()
                                    else:
                                        print("""
                                        Input yang dimasukkan tidak sesuai!
                                        Program akan kembali ke menu sebelumnya
                                        """)
                                        return UpdateList()
                                except:
                                    print("Nilai harus berupa bilangan bulat!")
                                    continue
                        #-MENGUBAH HP-#
                        elif InputAtribut.lower()=="hp":
                            while True:
                                try:
                                    InputAtribut= int(input("Silahkan isi nilai HP yang baru : "))
                                    SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                                    if SaveData.lower()=="ya":
                                        Weapons[InputID.upper()]["HP"]= InputAtribut
                                        print("Senjata berhasil dilakukan update!")
                                        WeaponList()
                                        return UpdateList()
                                    elif SaveData.lower()=="tidak":
                                        return UpdateList()
                                    else:
                                        print("""
                                        Input yang dimasukkan tidak sesuai!
                                        Program akan kembali ke menu sebelumnya
                                        """)
                                        return UpdateList()
                                except:
                                    print("Nilai harus berupa bilangan bulat!")
                                    continue
                        #-MENGUBAH DEFENSE-#
                        elif InputAtribut.lower()=="def" or InputAtribut.lower()=="defense": # Mengubah Defense
                            while True:
                                try:
                                    InputAtribut= int(input("Silahkan isi nilai DEF yang baru : "))
                                    SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                                    if SaveData.lower()=="ya":
                                        Weapons[InputID.upper()]["Defense"]= InputAtribut
                                        print("Senjata berhasil dilakukan update!")
                                        WeaponList()
                                        return UpdateList()
                                    elif SaveData.lower()=="tidak":
                                        return UpdateList()
                                    else:
                                        print("""
                                        Input yang dimasukkan tidak sesuai!
                                        Program akan kembali ke menu sebelumnya
                                        """)
                                        return UpdateList()
                                except:
                                    print("Nilai harus berupa bilangan bulat!")
                                    continue
                        else :
                            print("""
                            Atribut yang ingin diubah tidak tersedia!
                            Program akan kembali ke menu sebelumnya
                            """)
                    elif input4.lower()=="tidak":
                        return UpdateList()
                    else:
                        print("""
                        Input yang dimasukkan tidak sesuai!
                        Program akan kembali ke menu sebelumnya
                        """)
                        return UpdateList()
                else :
                    print("""
                    Senjata tidak tersedia!
                    Program akan kembali ke menu sebelumnya
                    """)
                    return UpdateList()
            #--MELAKUKAN UPDATE SENJATA TANGAN KOSONG--#
            if Opsi4==3:
                OffHandWeaponList()
                InputID = input("Masukkan ID senjata tangan kosong yang ingin dilakukan update : ")
                if InputID.upper() in OffHandWeapons:
                    CekInput = {InputID : OffHandWeapons[InputID.upper()]}
                    print(tabulate([[name, *inner.values()] for name, inner in CekInput.items()], headers, tablefmt="fancy_outline"))
                    input4 = input("Apakah anda yakin ingin melanjutkan update (ya/tidak)? ")
                    if input4.lower()=="ya":
                        InputAtribut= input("Silahkan pilih atribut yang ingin dilakukan update : ")
                        #-MENGUBAH ID-#
                        if InputAtribut.lower()=="id":
                            InputAtribut= input("Silahkan isi ID yang baru : ")
                            SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                            if SaveData.lower()=="ya":
                                    OffHandWeapons[InputAtribut]= OffHandWeapons.pop(InputID.upper())
                                    print("Senjata tangan kosong berhasil dilakukan update!")
                                    OffHandWeaponList()
                                    return UpdateList()
                            elif SaveData.lower()=="tidak":
                                return UpdateList()
                            else:
                                print("""
                                Input yang dimasukkan tidak sesuai!
                                Program akan kembali ke menu sebelumnya
                                """)
                                return UpdateList()
                        #-MENGUBAH NAMA-#
                        if InputAtribut.lower()=="name" or InputAtribut.lower()=="nama":
                            InputAtribut= input("Silahkan isi nama yang baru : ")
                            SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                            if SaveData.lower()=="ya":
                                OffHandWeapons[InputID.upper()]["Name"]= InputAtribut
                                print("Senjata tangan kosong berhasil dilakukan update!")
                                OffHandWeaponList()
                                return UpdateList()
                            elif SaveData.lower()=="tidak":
                                return UpdateList()
                            else:
                                print("""
                                Input yang dimasukkan tidak sesuai!
                                Program akan kembali ke menu sebelumnya
                                """)
                                return UpdateList()
                        #-MENGUBAH PROFILE-#
                        if InputAtribut.lower()=="profile" or InputAtribut.lower()=="profil": # Mengubah Profile
                            InputAtribut= input("Silahkan isi profil yang baru : ")
                            SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                            if SaveData.lower()=="ya":
                                OffHandWeapons[InputID.upper()]["Profile"]= InputAtribut
                                print("Senjata tangan kosong berhasil dilakukan update!")
                                OffHandWeaponList()
                                return UpdateList()
                            elif SaveData.lower()=="tidak":
                                return UpdateList()
                            else:
                                print("""
                                Input yang dimasukkan tidak sesuai!
                                Program akan kembali ke menu sebelumnya
                                """)
                                return UpdateList()
                        #-MENGUBAH ATTACK-#
                        elif InputAtribut.lower()=="atk" or InputAtribut.lower()=="attack": # Mengubah Attack
                            while True:
                                try:
                                    InputAtribut= int(input("Silahkan isi nilai ATK yang baru : "))
                                    SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                                    if SaveData.lower()=="ya":
                                        OffHandWeapons[InputID.upper()]["Attack"]= InputAtribut
                                        print("Senjata tangan kosong berhasil dilakukan update!")
                                        OffHandWeaponList()
                                        return UpdateList()
                                    elif SaveData.lower()=="tidak":
                                        return UpdateList()
                                    else:
                                        print("""
                                        Input yang dimasukkan tidak sesuai!
                                        Program akan kembali ke menu sebelumnya
                                        """)
                                        return UpdateList()
                                except:
                                    print("Nilai harus berupa bilangan bulat!")
                                    continue
                        #-MENGUBAH HP-#
                        elif InputAtribut.lower()=="hp":
                            while True:
                                try:
                                    InputAtribut= int(input("Silahkan isi nilai HP yang baru : "))
                                    SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                                    if SaveData.lower()=="ya":
                                        OffHandWeapons[InputID.upper()]["HP"]= InputAtribut
                                        print("Senjata tangan kosong berhasil dilakukan update!")
                                        OffHandWeaponList()
                                        return UpdateList()
                                    elif SaveData.lower()=="tidak":
                                        return UpdateList()
                                    else:
                                        print("""
                                        Input yang dimasukkan tidak sesuai!
                                        Program akan kembali ke menu sebelumnya
                                        """)
                                        return UpdateList()
                                except:
                                    print("Nilai harus berupa bilangan bulat!")
                                    continue
                        #-MENGUBAH DEFENSE-#
                        elif InputAtribut.lower()=="def" or InputAtribut.lower()=="defense": 
                            while True:
                                try:
                                    InputAtribut= int(input("Silahkan isi nilai DEF yang baru : "))
                                    SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                                    if SaveData.lower()=="ya":
                                        OffHandWeapons[InputID.upper()]["Defense"]= InputAtribut
                                        print("Senjata tangan kosong berhasil dilakukan update!")
                                        OffHandWeaponList()
                                        return UpdateList()
                                    elif SaveData.lower()=="tidak":
                                        return UpdateList()
                                    else:
                                        print("""
                                        Input yang dimasukkan tidak sesuai!
                                        Program akan kembali ke menu sebelumnya
                                        """)
                                        return UpdateList()
                                except:
                                    print("Nilai harus berupa bilangan bulat!")
                                    continue
                        else :
                            print("""
                            Atribut yang ingin diubah tidak tersedia!
                            Program akan kembali ke menu sebelumnya
                            """)
                    elif input4.lower()=="tidak":
                        return UpdateList()
                    else:
                        print("""
                        Input yang dimasukkan tidak sesuai!
                        Program akan kembali ke menu sebelumnya
                        """)
                        return UpdateList()
                else :
                    print("""
                    Senjata tangan kosong tidak tersedia!
                    Program akan kembali ke menu sebelumnya
                    """)
                    return UpdateList()
            #--MELAKUKAN UPDATE ARMOR--#
            if Opsi4==4:
                ArmorList()
                InputID = input("Masukkan ID Armor yang ingin dilakukan update : ")
                if InputID.upper() in Armor:
                    CekInput = {InputID : Armor[InputID.upper()]}
                    print(tabulate([[name, *inner.values()] for name, inner in CekInput.items()], headers, tablefmt="fancy_outline"))
                    input4 = input("Apakah anda yakin ingin melanjutkan update (ya/tidak)? ")
                    if input4.lower()=="ya":
                        InputAtribut= input("Silahkan pilih atribut yang ingin dilakukan update : ")
                        #-MENGUBAH ID-#
                        if InputAtribut.lower()=="id":
                            InputAtribut= input("Silahkan isi ID yang baru : ")
                            SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                            if SaveData.lower()=="ya":
                                    Armor[InputAtribut]= Armor.pop(InputID.upper())
                                    print("Armor berhasil dilakukan update!")
                                    ArmorList()
                                    return UpdateList()
                            elif SaveData.lower()=="tidak":
                                return UpdateList()
                            else:
                                print("""
                                Input yang dimasukkan tidak sesuai!
                                Program akan kembali ke menu sebelumnya
                                """)
                                return UpdateList()
                        #-MENGUBAH NAMA-#
                        if InputAtribut.lower()=="name" or InputAtribut.lower()=="nama":
                            InputAtribut= input("Silahkan isi nama yang baru : ")
                            SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                            if SaveData.lower()=="ya":
                                Armor[InputID.upper()]["Name"]= InputAtribut
                                print("Armor berhasil dilakukan update!")
                                ArmorList()
                                return UpdateList()
                            elif SaveData.lower()=="tidak":
                                return UpdateList()
                            else:
                                print("""
                                Input yang dimasukkan tidak sesuai!
                                Program akan kembali ke menu sebelumnya
                                """)
                                return UpdateList()
                        #-MENGUBAH PROFILE-#
                        if InputAtribut.lower()=="profile" or InputAtribut.lower()=="profil":
                            InputAtribut= input("Silahkan isi profil yang baru : ")
                            SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                            if SaveData.lower()=="ya":
                                Armor[InputID.upper()]["Profile"]= InputAtribut
                                print("Armor berhasil dilakukan update!")
                                ArmorList()
                                return UpdateList()
                            elif SaveData.lower()=="tidak":
                                return UpdateList()
                            else:
                                print("""
                                Input yang dimasukkan tidak sesuai!
                                Program akan kembali ke menu sebelumnya
                                """)
                                return UpdateList()
                        #-MENGUBAH ATTACK-#
                        elif InputAtribut.lower()=="atk" or InputAtribut.lower()=="attack":
                            while True:
                                try:
                                    InputAtribut= int(input("Silahkan isi nilai ATK yang baru : "))
                                    SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                                    if SaveData.lower()=="ya":
                                        Armor[InputID.upper()]["Attack"]= InputAtribut
                                        print("Armor berhasil dilakukan update!")
                                        ArmorList()
                                        return UpdateList()
                                    elif SaveData.lower()=="tidak":
                                        return UpdateList()
                                    else:
                                        print("""
                                        Input yang dimasukkan tidak sesuai!
                                        Program akan kembali ke menu sebelumnya
                                        """)
                                        return UpdateList()
                                except:
                                    print("Nilai harus berupa bilangan bulat!")
                                    continue
                        #-MENGUBAH HP-#
                        elif InputAtribut.lower()=="hp":
                            while True:
                                try:
                                    InputAtribut= int(input("Silahkan isi nilai HP yang baru : "))
                                    SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                                    if SaveData.lower()=="ya":
                                        Armor[InputID.upper()]["HP"]= InputAtribut
                                        print("Armor berhasil dilakukan update!")
                                        ArmorList()
                                        return UpdateList()
                                    elif SaveData.lower()=="tidak":
                                        return UpdateList()
                                    else:
                                        print("""
                                        Input yang dimasukkan tidak sesuai!
                                        Program akan kembali ke menu sebelumnya
                                        """)
                                        return UpdateList()
                                except:
                                    print("Nilai harus berupa bilangan bulat!")
                                    continue
                        #-MENGUBAH DEFENSE-#
                        elif InputAtribut.lower()=="def" or InputAtribut.lower()=="defense": 
                            while True:
                                try:
                                    InputAtribut= int(input("Silahkan isi nilai DEF yang baru : "))
                                    SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                                    if SaveData.lower()=="ya":
                                        Armor[InputID.upper()]["Defense"]= InputAtribut
                                        print("Armor berhasil dilakukan update!")
                                        ArmorList()
                                        return UpdateList()
                                    elif SaveData.lower()=="tidak":
                                        return UpdateList()
                                    else:
                                        print("""
                                        Input yang dimasukkan tidak sesuai!
                                        Program akan kembali ke menu sebelumnya
                                        """)
                                        return UpdateList()
                                except:
                                    print("Nilai harus berupa bilangan bulat!")
                                    continue
                        else :
                            print("""
                            Atribut yang ingin diubah tidak tersedia!
                            Program akan kembali ke menu sebelumnya
                            """)
                    elif input4.lower()=="tidak":
                        return UpdateList()
                    else:
                        print("""
                        Input yang dimasukkan tidak sesuai!
                        Program akan kembali ke menu sebelumnya
                        """)
                        return UpdateList()
                else :
                    print("""
                    Armor tidak tersedia!
                    Program akan kembali ke menu sebelumnya
                    """)
                    return UpdateList()
            #--MELAKUKAN UPDATE MONSTER--#
            if Opsi4==5:
                MonsterList()
                InputID = input("Masukkan ID monster yang ingin dilakukan update : ")
                if InputID.upper() in Monster:
                    CekInput = {InputID : Monster[InputID.upper()]}
                    print(tabulate([[name, *inner.values()] for name, inner in CekInput.items()], headers, tablefmt="fancy_outline"))
                    input4 = input("Apakah anda yakin ingin melanjutkan update (ya/tidak)? ")
                    if input4.lower()=="ya":
                        InputAtribut= input("Silahkan pilih atribut yang ingin dilakukan update : ")
                        #-MENGUBAH ID-#
                        if InputAtribut.lower()=="id":
                            InputAtribut= input("Silahkan isi ID yang baru : ")
                            SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                            if SaveData.lower()=="ya":
                                    Monster[InputAtribut]= Monster.pop(InputID.upper())
                                    print("Monster berhasil dilakukan update!")
                                    MonsterList()
                                    return UpdateList()
                            elif SaveData.lower()=="tidak":
                                return UpdateList()
                            else:
                                print("""
                                Input yang dimasukkan tidak sesuai!
                                Program akan kembali ke menu sebelumnya
                                """)
                                return UpdateList()
                        #-MENGUBAH NAMA-#
                        if InputAtribut.lower()=="name" or InputAtribut.lower()=="nama":
                            InputAtribut= input("Silahkan isi nama yang baru : ")
                            SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                            if SaveData.lower()=="ya":
                                Monster[InputID.upper()]["Name"]= InputAtribut
                                print("Monster berhasil dilakukan update!")
                                MonsterList()
                                return UpdateList()
                            elif SaveData.lower()=="tidak":
                                return UpdateList()
                            else:
                                print("""
                                Input yang dimasukkan tidak sesuai!
                                Program akan kembali ke menu sebelumnya
                                """)
                                return UpdateList()
                        #-MENGUBAH PROFILE-#
                        if InputAtribut.lower()=="profile" or InputAtribut.lower()=="profil":
                            InputAtribut= input("Silahkan isi profil yang baru : ")
                            SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                            if SaveData.lower()=="ya":
                                Monster[InputID.upper()]["Profile"]= InputAtribut
                                print("Monster berhasil dilakukan update!")
                                MonsterList()
                                return UpdateList()
                            elif SaveData.lower()=="tidak":
                                return UpdateList()
                            else:
                                print("""
                                Input yang dimasukkan tidak sesuai!
                                Program akan kembali ke menu sebelumnya
                                """)
                                return UpdateList()
                        #-MENGUBAH ATTACK-#
                        elif InputAtribut.lower()=="atk" or InputAtribut.lower()=="attack":
                            while True:
                                try:
                                    InputAtribut= int(input("Silahkan isi nilai ATK yang baru : "))
                                    SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                                    if SaveData.lower()=="ya":
                                        Monster[InputID.upper()]["Attack"]= InputAtribut
                                        print("Monster berhasil dilakukan update!")
                                        MonsterList()
                                        return UpdateList()
                                    elif SaveData.lower()=="tidak":
                                        return UpdateList()
                                    else:
                                        print("""
                                        Input yang dimasukkan tidak sesuai!
                                        Program akan kembali ke menu sebelumnya
                                        """)
                                        return UpdateList()
                                except:
                                    print("Nilai harus berupa bilangan bulat!")
                                    continue
                        #-MENGUBAH HP-#
                        elif InputAtribut.lower()=="hp":
                            while True:
                                try:
                                    InputAtribut= int(input("Silahkan isi nilai HP yang baru : "))
                                    SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                                    if SaveData.lower()=="ya":
                                        Monster[InputID.upper()]["HP"]= InputAtribut
                                        print("Monster berhasil dilakukan update!")
                                        MonsterList()
                                        return UpdateList()
                                    elif SaveData.lower()=="tidak":
                                        return UpdateList()
                                    else:
                                        print("""
                                        Input yang dimasukkan tidak sesuai!
                                        Program akan kembali ke menu sebelumnya
                                        """)
                                        return UpdateList()
                                except:
                                    print("Nilai harus berupa bilangan bulat!")
                                    continue
                        #-MENGUBAH DEFENSE-#
                        elif InputAtribut.lower()=="def" or InputAtribut.lower()=="defense":
                            while True:
                                try:
                                    InputAtribut= int(input("Silahkan isi nilai DEF yang baru : "))
                                    SaveData=input("Apakah anda yakin ingin melakukan update (ya/tidak)? ")
                                    if SaveData.lower()=="ya":
                                        Monster[InputID.upper()]["Defense"]= InputAtribut
                                        print("Monster berhasil dilakukan update!")
                                        MonsterList()
                                        return UpdateList()
                                    elif SaveData.lower()=="tidak":
                                        return UpdateList()
                                    else:
                                        print("""
                                        Input yang dimasukkan tidak sesuai!
                                        Program akan kembali ke menu sebelumnya
                                        """)
                                        return UpdateList()
                                except:
                                    print("Nilai harus berupa bilangan bulat!")
                                    continue
                        else :
                            print("""
                            Atribut yang ingin diubah tidak tersedia!
                            Program akan kembali ke menu sebelumnya
                            """)
                    elif input4.lower()=="tidak":
                        return UpdateList()
                    else:
                        print("""
                        Input yang dimasukkan tidak sesuai!
                        Program akan kembali ke menu sebelumnya
                        """)
                        return UpdateList()
                else :
                    print("""
                    Monster tidak tersedia!
                    Program akan kembali ke menu sebelumnya
                    """)
                    return UpdateList()
            #--KEMBALI KE MAIN MENU--#
            elif Opsi4==6:
                return
            else:
                print("Tolong masukkan angka yang tersedia!")
                return UpdateList()
        except:
            print("Tolong masukkan format yang benar!")
            return UpdateList()

#--------PEMILIHAN KARAKTER UNTUK SIMULASI--------#
def ChooseCharacter():
    CharacterList()
    #----PILIH KARAKTER YANG AKAN DIPAKAI----#
    PilihKarakter = input("Silahkan pilih karakter yang ingin digunakan berdasarkan ID : ")
    if PilihKarakter.upper() in Character:
        SaveData = input("Apakah anda yakin ingin memilih karakter tersebut (ya/tidak)?")
        if SaveData.lower()=="ya":
            Nama_Karakter = Character[PilihKarakter.upper()]["Name"]
            ATK_Karakter = Character[PilihKarakter.upper()]["Attack"]
            HP_Karakter = Character[PilihKarakter.upper()]["HP"]
            DEF_Karakter = Character[PilihKarakter.upper()]["Defense"]
            WeaponList()
            #----PILIH SENJATA YANG AKAN DIPAKAI----#
            PilihSenjata= input("Silahkan pilih senjata yang ingin digunakan berdasarkan ID : ")
            if PilihSenjata.upper() in Weapons:
                SaveData = input("Apakah anda yakin ingin memilih senjata tersebut (ya/tidak)? \n(Note : Anda akan balik ke menu pemilihan karakter apabila anda tidak yakin saat memilih perlengkapan!)")
                if SaveData.lower()=="ya":
                    ATK_Karakter += Weapons[PilihSenjata.upper()]["Attack"]
                    HP_Karakter += Weapons[PilihSenjata.upper()]["HP"]
                    DEF_Karakter += Weapons[PilihSenjata.upper()]["Defense"]
                    OffHandWeaponList()
                    #----PILIH SENJATA TANGAN KOSONG YANG AKAN DIPAKAI----#
                    PilihSenjataOF = input("Silahkan pilih senjata tangan kosong yang ingin digunakan berdasarkan ID : ")
                    if PilihSenjataOF.upper() in OffHandWeapons:
                        SaveData = input("Apakah anda yakin ingin memilih senjata tangan kosong tersebut (ya/tidak)? \n(Note : Anda akan balik ke menu pemilihan karakter apabila anda tidak yakin saat memilih perlengkapan!)")
                        if SaveData.lower()=="ya":
                            ATK_Karakter += OffHandWeapons[PilihSenjataOF.upper()]["Attack"]
                            HP_Karakter += OffHandWeapons[PilihSenjataOF.upper()]["HP"]
                            DEF_Karakter += OffHandWeapons[PilihSenjataOF.upper()]["Defense"]
                            ArmorList()
                            #----PILIH ARMOR YANG AKAN DIPAKAI----#
                            PilihArmor = input("Silahkan pilih armor yang ingin digunakan berdasarkan ID : ")
                            if PilihArmor.upper() in Armor:
                                SaveData = input("Apakah anda yakin ingin memilih armor tersebut (ya/tidak)? \n(Note : Anda akan balik ke menu pemilihan karakter apabila anda tidak yakin saat memilih perlengkapan!)")
                                if SaveData.lower()=="ya":
                                    ATK_Karakter += Armor[PilihArmor.upper()]["Attack"]
                                    HP_Karakter += Armor[PilihArmor.upper()]["HP"]
                                    DEF_Karakter += Armor[PilihArmor.upper()]["Defense"]
                                    print(f"Karakter yang dipilih adalah {Nama_Karakter} dengan Attack {ATK_Karakter}, HP {HP_Karakter}, dan Defense {DEF_Karakter}")
                                    temp_dict= {"Name" : Nama_Karakter, "Attack" : ATK_Karakter, "HP" : HP_Karakter, "Defense" : DEF_Karakter}
                                    #--MEMBERSIHKAN ISI DICT JIKALAU SUDAH PERNAH TERISI--#
                                    EquippedCharacter.clear()
                                    #--MENGISI DICT--#
                                    EquippedCharacter.update(temp_dict)
                                    return Gameplay()
                                elif SaveData.lower()=="tidak":
                                    return Gameplay()
                                else :
                                    print("""
                                    Input yang dimasukkan tidak sesuai!
                                    Program akan kembali ke menu sebelumnya
                                    """)
                                    return Gameplay()
                        elif SaveData.lower()=="tidak":
                            return Gameplay()
                        else :
                            print("""
                            Input yang dimasukkan tidak sesuai!
                            Program akan kembali ke menu sebelumnya
                            """)
                            return Gameplay()
                elif SaveData.lower()=="tidak":
                    return Gameplay()
                else :
                    print("""
                    Input yang dimasukkan tidak sesuai!
                    Program akan kembali ke menu sebelumnya
                    """)
                    return Gameplay()
        elif SaveData.lower()=="tidak":
            return Gameplay()
        else :
            print("""
            Input yang dimasukkan tidak sesuai!
            Program akan kembali ke menu sebelumnya
            """)
            return Gameplay()
    else :
        print("Karakter tidak tersedia!")
        return Gameplay()

#--------PEMILIHAN MONSTER UNTUK SIMULASI--------#
def ChooseMonster():
    MonsterList()
    PilihMonster = input("Silahkan pilih monster yang ingin dilawan berdasarkan ID : ")
    if PilihMonster.upper() in Monster:
        SaveData = input("Apakah anda yakin ingin melawan monster tersebut (ya/tidak)? ")
        if SaveData.lower()=="ya":
            Nama_Monster = Monster[PilihMonster.upper()]["Name"]
            ATK_Monster = Monster[PilihMonster.upper()]["Attack"]
            HP_Monster = Monster[PilihMonster.upper()]["HP"]
            DEF_Monster = Monster[PilihMonster.upper()]["Defense"]
            temp_dict= {"Name" : Nama_Monster, "Attack" : ATK_Monster, "HP" : HP_Monster, "Defense" : DEF_Monster}
            Opponent.clear() #Membersihkan Isi List jikalau sudah pernah terisi
            Opponent.update(temp_dict)
            return Gameplay()
        elif SaveData.lower()=="tidak":
            return Gameplay()
        else :
            print("""
            Input yang dimasukkan tidak sesuai!
            Program akan kembali ke menu sebelumnya
            """)
            return Gameplay()

#--------SIMULASI--------#
def FightSimulation():
    #----MEMASUKKAN STAT KE DALAM VARIABEL----#
    Nama_Karakter = EquippedCharacter["Name"]
    ATK_Karakter = EquippedCharacter["Attack"]
    HP_Karakter = EquippedCharacter["HP"]
    DEF_Karakter = EquippedCharacter["Defense"]
    Nama_Monster = Opponent["Name"]
    ATK_Monster = Opponent["Attack"]
    HP_Monster = Opponent["HP"]
    DEF_Monster = Opponent["Defense"]
    #----CEK HP----#
    while HP_Karakter>0 and HP_Monster>0:
        print(f"{Nama_Karakter} melakukkan serangan!")
        #--NILAI ATTACK KARAKTER--#
        AttackKarakterRandom= random.randint((ATK_Karakter-2), (ATK_Karakter+2))
        #--RANDOM CRIT--#
        RandomCrit= random.randint(1,100)
        #--CEK ATTACK KARAKTER DAN DEFENSE MONSTER--#
        if AttackKarakterRandom>DEF_Monster:
            if RandomCrit<=5:
                print(f"{Nama_Karakter} akan melakukan serangan critical!")
                RandomCritTrigger = (AttackKarakterRandom - DEF_Monster)*2
                HP_Monster -= RandomCritTrigger
            else :
                HP_Monster -= AttackKarakterRandom - DEF_Monster
            if HP_Monster<0:
                HP_Monster=0
        else :
            HP_Monster-= 1
            if HP_Monster<0:
                HP_Monster=0
        if (AttackKarakterRandom - DEF_Monster)>0:
            if RandomCrit<=5:
                print(f"{Nama_Monster} terkena serangan sebesar {RandomCritTrigger}, HP tersisa {HP_Monster}\n")
            else :
                print(f"{Nama_Monster} terkena serangan sebesar {AttackKarakterRandom - DEF_Monster}, HP tersisa {HP_Monster}\n")
        else :
            print(f"{Nama_Monster} terkena serangan sebesar 1, HP tersisa {HP_Monster}\n")
        #----CEK HP----#
        if HP_Monster>0:
            print(f"{Nama_Monster} melakukkan serangan!")
            #--NILAI ATTACK MONSTER--#
            AttackMonsterRandom= random.randint((ATK_Monster-2), (ATK_Monster+2))
            #--RANDOM CRIT--#
            RandomCrit= random.randint(1,100)
            #--CEK ATTACK MONSTER DAN DEFENSE KARAKTER--#
            if AttackMonsterRandom>DEF_Karakter:
                if RandomCrit<=5:
                    print(f"{Nama_Monster} akan melakukan serangan critical!")
                    RandomCritTrigger = (AttackMonsterRandom - DEF_Karakter)*2
                    HP_Karakter -= RandomCritTrigger
                else :
                    HP_Karakter -= AttackMonsterRandom - DEF_Karakter
                if HP_Karakter<0:
                    HP_Karakter=0
            else :
                HP_Karakter-= 1
                if HP_Karakter<0:
                    HP_Karakter=0
            if (AttackMonsterRandom - DEF_Karakter)>0:
                if RandomCrit<=5:
                    print(f"{Nama_Karakter} terkena serangan sebesar {RandomCritTrigger}, HP tersisa {HP_Karakter}\n")
                else :
                    print(f"{Nama_Karakter} terkena serangan sebesar {AttackMonsterRandom - DEF_Karakter}, HP tersisa {HP_Karakter}\n")
            else :
                print(f"{Nama_Karakter} terkena serangan sebesar 1, HP tersisa {HP_Karakter}\n")
    #----MONSTER MENANG----#
    if HP_Karakter<=0:
        print(f"{Nama_Karakter} dikalahkan, {Nama_Monster} menang!!!")
        return Gameplay()
    #----MONSTER MENANG----#
    elif HP_Monster<=0:
        print(f"{Nama_Monster} dikalahkan, {Nama_Karakter} menang!!!")
        return Gameplay()
        
#--------SIMULASI PERMAINAN OTOMATIS--------#
def Gameplay():

    #----INISIASI----#
    OpsiGP=0
    
    print(f"""
          ====Simulasi Permainan Otomatis====
          
          Silahkan pilih menu bagian yang ingin anda lakukan :
          1. Pilih Karakter
          2. Pilih Monster
          3. Lakukan Simulasi Permainan Otomatis
          4. Kembali ke Menu Utama
          """)
    
    #----PEMILIHAN OPSI----#
    while OpsiGP!=4:
        try:
            OpsiGP=int(input("Masukkan angka yang ingin dijalankan : "))
            if OpsiGP==1:
                ChooseCharacter()
            elif OpsiGP==2:
                ChooseMonster()
            elif OpsiGP==3:
                #--CEK JIKA KARAKTER SUDAH DIPILIH--#
                if bool(EquippedCharacter)==True:
                    #--CEK JIKA MONSTER SUDAH DIPILIH--#
                    if bool(Opponent)==True:
                        FightSimulation()
                    else :
                        print("Anda belum memilih lawan!")
                        return Gameplay()
                else :
                    print("Anda belum memilih karakter")
                    return Gameplay()
            elif OpsiGP==4:
                return
            else :
                print("Tolong masukkan angka yang tersedia!")
                return Gameplay()
        except:
            print("Tolong masukkan sesuai format!")
            return Gameplay()

#--------MAIN MENU--------#
def MainMenu():

    #----INISIASI----#
    OpsiMM=0

    #----PEMILIHAN OPSI----#
    while OpsiMM!=6:
        print(f""" 
          ====TURN-BASED GAME AUTO BATTLE SIMULATION===
          
          Selamat datang di "TURN-BASED GAME AUTO BATTLE SIMULATION"
          Silahkan pilih bagian yang ingin anda lakukan :
          1. Melihat Stat dari Karakter, Perlengkapan, dan Monster
          2. Menambahkan Karakter, Perlengkapan, atau Monster
          3. Menghapus Karakter, Perlengkapan, atau Monster
          4. Melakukan Update dari Karakter, Perlengkapan, atau Monster
          5. Simulasi Permainan Otomatis
          6. Keluar dari Program
          """)
        try:
            OpsiMM=int(input("Masukkan angka yang ingin dijalankan : "))
            if OpsiMM==1:
                StatList()
                continue
            elif OpsiMM==2:
                AddList()
                continue
            elif OpsiMM==3:
                RemoveList()
                continue
            elif OpsiMM==4:
                UpdateList()
                continue
            elif OpsiMM==5:
                Gameplay()
                continue
            elif OpsiMM==6:
                return
            else:
                print("Tolong masukkan angka yang tersedia!")
                continue
        except:
            print("Tolong masukkan sesuai format!")
            continue
MainMenu()
