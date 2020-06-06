# gspread

>* 1.สร้างโปรเจกต์ https://console.developers.google.com/cloud-resource-manager

>* 2.สร้างcredential กดขีด3ขีดด้านซ้าย เลือก APIs&Services > credential. กด CREATE CREDENTIALS > Service Account 

>* 3.Create Key เลือกไฟล์Json ดาวน์โหลด แล้วเปลี่ยนชื่อไฟล์ ย้ายไปโฟลเดอร์เดียวกับที่เราจะเขียนโค้ด

>* 4.Libary >Enable Google Sheets API >Enable Google Drive API

>* 5.สร้าง spreadsheet https://docs.google.com/spreadsheets/u/2/

>* 6.แชร์speadsheet ให้สิทธิ์เมล์ที่มากับไฟล์credential ตรงบรรทัด client_email



#ขั้้นเขียนโค้ด

>* ลงlib > pip3 install --upgrade oauth2client PyOpenSSL gspread

```py
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = [“https://www.googleapis.com/auth/spreadsheets”] 
credentials = ServiceAccountCredentials.from_json_keyfile_name(‘credentials.json’, scope)
gc = gspread.authorize(credentials)
sheet = gc.open_by_url("<<file_url>>")
worksheet = sheet.get_worksheet(0)

```

เท่านี้โค้ดเราก็เชื่อมต่อกับspread sheet เรียบร้อย

#ตัวอย่างคำสั่ง

```py
print(worksheet.get_all_values()) #ปริ้นทั้งหมด
```

```py
print(worksheet.row_values(3)) #ปริ้นrow3
```

```py
print(worksheet.acell('B3').value) #ปริ้นค่าcell B3
```

```py
print(worksheet.cell(3,1).value) #ปริ้นค่าcell R3C1
```

```py
worksheet.update_cell(3,1, 'update R3C1') #อัพเดต R3C1
```

```py
worksheet.update_acell('B2', 'update B2 ') #อัพเดตcell B2 
```

```py
print(worksheet.findall('Key word')) #หาค่า
```
