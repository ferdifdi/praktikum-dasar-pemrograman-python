# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:54:11 2019

@author: USER
"""

import csv
import operator

print("#####")
print("BudayaKB Lite v1.0")
print("~Kalau bukan kita yang melestarikan budaya, siapa lagi?~")
print("#####")
print()
      
print("DAFTAR PERINTAH")
daftar_perintah = [
    ["IMPOR <file.csv>", "Mengimpor file warisan budaya", "IMPOR kb.csv"],
    ["CARINAMA <namawarisanbudaya>","Mencari nama dari warisan budaya", "CARINAMA Tari Legong"],
    ["CARITIPE <tipe>","Mencari tipe dari warisan budaya", "CARITIPE TARIAN"],
    ["CARIPROV <provinsi>","Mencari warisan budaya berdasarkan provinsi", "CARIPROV Aceh"],
    ["TAMBAH <namawarisanbudaya>;;;<tipe>;;;<provinsi>;;;<referenceurl>",
     "Menambahkan warisan budaya","TAMBAH Tari Legong;;;Makanan;;;Bali;;;www.baliprov.go.id"],
    ["UPDATE <namawarisanbudaya>;;;<tipe>;;;<provinsi>;;;<referenceurl>",
     "Mengganti data dari warisan budaya yang sudah ada",
      "UPDATE Tari Legong;;;Tarian;;;Bali;;;www.baliprov.go.id"],
    ["HAPUS <namawarisanbudaya>","Menghapus warisan budaya", "HAPUS Tari Legog"],
    ["STAT","Menghitung jumlah warisan budaya", "STAT"],
    ["STATTIPE","Menghitung jumlah warisan budaya berdasarkan tipe", "STATTIPE"],
    ["EKSPOR <file.csv>","Mengekspor file warisan budaya", "EKSPOR kb_rev01.csv"],
    ["KELUAR","Mengakhiri Program", "KELUAR"],
    ["HELP","Memunculkan daftar perintah kembali", "HELP"], 
    ["CETAK","Mencetak data", "CETAK"],     
]

#mencetak daftar perintah    
def HELP():
    #mencetak daftar perintah dari list daftar_perintah
    for i in range(len(daftar_perintah)):
        print(f'{i+1:2d} {daftar_perintah[i][0]}') #perintah
        print(f'{"":2s} Fungsi: {daftar_perintah[i][1]}') #fungsi dari perintah
        print(f'{"":2s} Contoh: {daftar_perintah[i][2]}') #contoh perintah

#mencetak daftar perintah sebelum memasukkan perintah
HELP()
        
#FITUR mengubah struktur data

#mengubah list menjadi dictionary
def dct(lst): 
    #dictionary diubah menjadi list 2 dimensi
    #secara berulang pengubahan dilakukan sebanyak indeks dimensi pertamanya
    #dimensi keduanya, indeks ke-0 dijadikan key
        #sedangkan, indeks ke-1 sampai ke-3 nya dijadikan value-value key tersebut
    list_to_dict = {lst[i][0]: (lst[i][1],lst[i][2],lst[i][3]) for i in range(0, len(lst))} 
    return list_to_dict 

#mengubah dictionary menjadi list
def lst(dct):     
    dct_to_lst = [] #list kosong untuk menampung data nantinya
    for key, value in dct.items():    #untuk setiap item dari dictionary yang berisi key dan value  
        #key dan value-valuenya ditambahkan ke list kosong tadi
        dct_to_lst.append([key,value[0],value[1],value[2]]) 
    return dct_to_lst

#FITUR fungsi        
def IMPOR(file_imp):       
    try:    
        kb_file = open(file_imp, "r") #membuka dan membaca file
        reader = csv.reader(kb_file) #membaca file berformat csv
        data_list = []
        for row in reader:
            data_list.append(row) #setiap baris yang dibaca, ditambahkan ke list
        kb_file.close() #menutup file
        #print(impor)
        global data_dict #membuat data_dict dapat diakses secara global (berarti, dapat diakses semua fungsi)        
        data_dict = dct(data_list) #mengubah list data_list menjadi dictionary data_dict
        #print(data_dict)
        print("Terimpor {} baris".format(len(data_dict))) #mencetak banyak baris / pasangan key value
        return data_dict
    except FileNotFoundError: 
        print("file tidak ada")
    
    #jika isi dari file yang diimpor tidak sesuai format
        #di mana formatnya adalah file csv dengan 4 kolom
            #maka akan tercetak "file tidak sempurna"
                #karena di saat list diubah menjadi dictionary dengan ketentuan 4 kolom
                    #berarti indeksnya error
    except IndexError: 
        print("file tidak sempurna")
 
#mencari nama warisan budaya       
def CARINAMA(nama):
    try:
        #print(data_dict)
        for key,value in data_dict.items(): #perulangan yang mengecek seluruh pasangan key dan value-nya
            if nama == key: #jika nama yang dicari ada di key (key menyimpan data nama)
                print(key+","+value[0]+","+value[1]+","+value[2]) #maka seluruh info warisan budaya tersebut dicetak 
        if nama not in data_dict.keys(): #jika nama yang dicari tidak ada di key (key menyimpan data nama)
            print("{} tidak ditemukan".format(nama)) #dicetak bahwa nama tsb tidak ditemukan
    
    #jika sebelumnya kita belum mengimpor file
        #di mana fungsi tersebut mengeksekusi file
            #maka nama variabel yang menyimpan file tersebut tidak terdefinisikan
                #berarti name-nya error
    except NameError: 
        print("IMPOR file terlebih dahulu")

#mencari tipe dari warisan budaya        
def CARITIPE(tipe):
    try:
        i = 0
        for key,value in data_dict.items(): #perulangan yang mengecek seluruh pasangan key dan value-nya
            if tipe == value[0]: #jika tipe yang dicari ada di value[0] (value[0] menyimpan data tipe)
                print(key+","+value[0]+","+value[1]+","+value[2]) #maka seluruh info warisan budaya tersebut 
                i = i+1 #jika ditemukan, banyak warisan budaya pada tipe tsb bertambah
        print("*Ditemukan {} {}*".format(i,value[0])) #dicetak banyak warisan budaya pada tipe tsb yang ditemukan 
    except NameError:
        print("IMPOR file terlebih dahulu")

#mencari provinsi dari warisan budaya 
def CARIPROV(prov):
    try:
        i = 0
        for key,value in data_dict.items(): #perulangan yang mengecek seluruh pasangan key dan value-nya
            if prov == value[1]: #jika provinsi yang dicari ada di value[1] (value[1] menyimpan data provinsi)
                print(key+","+value[0]+","+value[1]+","+value[2]) #maka seluruh info warisan budaya tersebut
                i = i+1 #jika ditemukan, banyak warisan budaya pada provinsi tsb bertambah
        print("*Ditemukan {} warisan budaya*".format(i)) #dicetak banyak warisan budaya pada provinsi tsb yang ditemukan
    except NameError:
        print("IMPOR file terlebih dahulu")

#menambahkan warisan budaya baru
def TAMBAH(tambah):
    try:
        key, value0, value1, value2 = tambah.split(";;;")
        if key not in data_dict.keys(): #jika warisan budaya belum ada, 
            data_dict[key] = value0, value1, value2 #maka warisan budaya ditambahkan
            #print(data_dict)
            print(key," ditambahkan")
            return data_dict
        else:
            print("Data yang ingin ditambah sudah ada")     
    
    #Jika data yang ditambahkan tidak sesuai format
        #Hal itu membuat ValueError karena tidak cukup value yang dimasukkan
    except ValueError: 
        print("Masukkan sesuai format: <namawarisanbudaya>;;;<tipe>;;;<provinsi>;;;<referenceurl>")
    except NameError:
        print("IMPOR file terlebih dahulu")

#mengupdate warisan budaya yang sudah ada
def UPDATE(update):
    try:
        key, value0, value1, value2 = update.split(";;;")
        if key in data_dict.keys(): #jika warisan budaya sudah ada,
            data_dict[key]  =  value0, value1, value2 #maka warisan budaya diupdate
            #print(data_dict)
            print(key," diupdate")
            return data_dict            
        else: #jika warisan budaya tidak ada,
            print("Data yang ingin diupdate tidak ditemukan") #tercetak bahwa data yang ingin diupdate tidak ada
    except ValueError:
        print("Masukkan sesuai format: <namawarisanbudaya>;;;<tipe>;;;<provinsi>;;;<referenceurl>")
    except NameError:
        print("IMPOR file terlebih dahulu")

#menghapus warisan budaya
def HAPUS(hapus):
    try:
        del data_dict[hapus] #menghapus isi dictionary berdasarkan key (key menyimpan nama warisan budaya)
        #print(data_dict)
        print("{} dihapus".format(hapus))
    except KeyError: #KeyError jika Key / nama warisan budaya yang ingin dihapus tidak ada
        print("Data yang ingin dihapus tidak ditemukan")
    except NameError:
        print("IMPOR file terlebih dahulu")        

#menghitung banyak warisan budaya
def STAT():
    try:
        print("Terdapat {} warisan budaya".format(len(data_dict)))
    except NameError:
        print("IMPOR file terlebih dahulu")

#menghitung statistik banyak warisan budaya berdasarkan tipenya
def STATTIPE():
    try:
        #menghitung statistik warisan budaya berdasarkan tipe / value[0]
        stattipe = {}
        for key,value in data_dict.items():
            if value[0] in stattipe:
                stattipe[value[0]] += 1
            else:
                stattipe[value[0]] = 1
        STtoList = [(k, v) for k, v in stattipe.items()] #mengubah dictionary menjadi list of tuple
        
        #urutkan berdasarkan elemen kedua dari tuple dari terbesar
        STtoList.sort(key = operator.itemgetter(1), reverse = True)
        
        print(STtoList)
    except NameError:
        print("IMPOR file terlebih dahulu")

#menghitung statistik banyak warisan budaya berdasarkan provinsinya   
def STATPROV():
    try:
        #menghitung statistik warisan budaya berdasarkan provinsi / value[1]
        statprov = {}
        for key,value in data_dict.items():
            if value[1] in statprov:
                statprov[value[1]] += 1
            else:
                statprov[value[1]] = 1
        SPtoList = [(k, v) for k, v in statprov.items()] #mengubah dictionary menjadi list of tuple
        
        #urutkan berdasarkan elemen kedua dari tuple dari terbesar
        SPtoList.sort(key = operator.itemgetter(1), reverse = True)
        
        print(SPtoList)
    except NameError:
        print("IMPOR file terlebih dahulu")
 
#mengekspor data
def EKSPOR(file_eks):  
    try:
        dct_to_lst = lst(data_dict) #mengubah dictionary data_dict menjadi list dct_to_list
        with open(file_eks, 'w', newline='') as csvFile: #membuka file dan menulisnya (baris baru dihilangkan)
            writer = csv.writer(csvFile) #membaca file csv
            writer.writerows(dct_to_lst) #menuliskan / menambahkan setiap barisnya ke list
        csvFile.close() #menutup file
        print("Terekspor {} baris".format(len(data_dict)))
    except NameError:
        print("IMPOR file terlebih dahulu")

#mencetak data warisan budaya sementara     
def CETAK():
    try:
        for key,value in data_dict.items(): #untuk setiap pasangan key dan value / data warisan budaya
            print(key+","+value[0]+","+value[1]+","+value[2]) #cetak semua informasinya
    except NameError:
        print("IMPOR file terlebih dahulu")
    

#COMMAND
        
#perulangan masukan input perintah
i = 1
while i != 0: #Perulangan terus berjalan selama i tidak 0
    perintah = input("> Masukkan perintah: ") 
    perintah_split = perintah.split(" ") 
    if perintah == "KELUAR":
        i = 0 
        #i = 0. Perulangan terus berjalan selama i tidak 0. 
        #Berarti, perulangan akan berakhir jika perintahnya "KELUAR"
        print("~Sampai jumpa, jangan lupa mencintai warisan budaya Indonesia!~ ")
        
    #perintah_split[0] untuk menentukan fungsi mana yang dijalankan
    #perintah_split[1:] untuk menentukan inputan yang akan dieksekusi fungsi tsb
    #(' '.join(perintah_split[1:])) split akan menghasilkan list. List tsb diubah menjadi string agar bisa dieksekusi
    
    elif perintah_split[0] == "HELP":
        HELP()
    elif perintah_split[0] == "CETAK":
        CETAK()
    elif perintah_split[0] == "IMPOR":
        file_imp = (' '.join(perintah_split[1:]))
        IMPOR(file_imp)
    elif perintah_split[0] == "CARINAMA":
        nama = (' '.join(perintah_split[1:]))
        CARINAMA(nama)        
    elif perintah_split[0] == "CARITIPE":
        tipe = (' '.join(perintah_split[1:]))
        CARITIPE(tipe)
    elif perintah_split[0] == "CARIPROV":
        prov = (' '.join(perintah_split[1:]))
        CARIPROV(prov)
    elif perintah_split[0] == "TAMBAH":
        tambah = (' '.join(perintah_split[1:]))
        TAMBAH(tambah)
    elif perintah_split[0] == "UPDATE":
        update = (' '.join(perintah_split[1:]))
        UPDATE(update)
    elif perintah_split[0] == "TAMBAH":
        tambah = (' '.join(perintah_split[1:]))
        TAMBAH(tambah)
    elif perintah_split[0] == "HAPUS":
        hapus = (' '.join(perintah_split[1:]))
        HAPUS(hapus)
    elif perintah_split[0] == "STAT":
        STAT()
    elif perintah_split[0] == "STATTIPE":
        STATTIPE()
    elif perintah_split[0] == "STATPROV":
        STATPROV()
    elif perintah_split[0] == "STATPROV":
        STATPROV()
    elif perintah_split[0] == "EKSPOR":
        file_eks = (' '.join(perintah_split[1:]))
        EKSPOR(file_eks)    
    else:
        print("Masukkan perintah yang benar")