# gspread

>* 1.สร้างโปรเจกต์ https://console.developers.google.com/cloud-resource-manager

>* 2.สร้างcredential กดขีด3ขีดด้านซ้าย เลือก APIs&Services > credential. กด CREATE CREDENTIALS > Service Account 

>* 3.Create Key เลือกไฟล์Json ดาวน์โหลด แล้วเปลี่ยนชื่อไฟล์ ย้ายไปโฟลเดอร์เดียวกับที่เราจะเขียนโค้ด

>* 4.Libary >Enable Google Sheets API >Enable Google Drive API

>* 5.สร้าง spreadsheet https://docs.google.com/spreadsheets/u/2/

>* 6.แชร์speadsheet ให้สิทธิ์เมล์ที่มากับไฟล์credential ตรงบรรทัด client_email



#ขั้้นเขียนโค้ด

>* 1.ลงlib > pip3 install --upgrade oauth2client PyOpenSSL gspread

2 ```py
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = [“https://www.googleapis.com/auth/spreadsheets”] 
```
>* 3.from oauth2client.service_account import ServiceAccountCredentials

>* 4.scope = [“https://www.googleapis.com/auth/spreadsheets”] 

>* 5.credentials = ServiceAccountCredentials.from_json_keyfile_name(‘credentials.json’, scope)

>* 6.gc = gspread.authorize(credentials)

>* 7.sheet = gc.open_by_url("<<file_url>>")

>* 8.worksheet = sheet.get_worksheet(0)

เท่านี้โค้ดเราก็เชื่อมต่อกับspread sheet เรียบร้อย

#ตัวอย่างคำสั่ง

```py
worksheet = sheet.get_worksheet(0)
```
