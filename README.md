# gspread

>* 1.สร้างโปรเจกต์ https://console.developers.google.com/cloud-resource-manager

>* 2.สร้างcredential กดขีด3ขีดด้านซ้าย เลือก APIs&Services > credential. กด CREATE CREDENTIALS > Service Account 

>* 3.Create Key เลือกไฟล์Json ดาวน์โหลด แล้วเปลี่ยนชื่อไฟล์ ย้ายไปโฟลเดอร์เดียวกับที่เราจะเขียนโค้ด

>* 4.สร้าง spreadsheet https://docs.google.com/spreadsheets/u/2/

>* 5.แชร์speadsheet ให้สิทธิ์เมล์ที่มากับไฟล์credential ตรงบรรทัด client_email


#ขั้้นเขียนโค้ด

>* 1.ลงlib > pip3 install --upgrade oauth2client PyOpenSSL gspread

>* 2.import gspread
  from oauth2client.service_account import ServiceAccountCredentials
