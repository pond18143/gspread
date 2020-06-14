import gspread
#ใช้ปรับแต่งแก้ไข spreadsheet
from oauth2client.service_account import ServiceAccountCredentials 


# for read-and-write access
scope = ['https://www.googleapis.com/auth/spreadsheets']

# for read-only access
#scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope) #keyที่เซฟเป็นjson
gc = gspread.authorize(credentials)

#ลิงค์google sheet
sheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1QrOs0PcAxnnP21OwFxhvzsbPShwpdyg7ElXPI6bljTc/edit?usp=sharing")
worksheet = sheet.get_worksheet(1) # เริ่มแผ่น0

print(worksheet.get_all_values()) #ปริ้นทั้งหมด

#print(worksheet.row_values(3)) #ปริ้นrow  แนวนอน
#print(worksheet.col_values(2)) #ปริ้นcol  แนวตั้ง

#print(worksheet.acell('B3')) #ปริ้น Cell R2C1
#print(worksheet.cell(1,2)) #ปริ้น Cell R1C2 '  '

#print(worksheet.acell('B3').value) #ปริ้นค่าcell
#print(worksheet.cell(3,1).value) #ปริ้นค่าcell

#worksheet.update_acell('B2', 'testupdate ') #อัพเดตB2 สามารถลบ_acellได้
#worksheet.update_cell(3,1, 'upup') #อัพเดต r3 c1
#worksheet.update('A2', [[1, 2], [3, 4]])

#print(worksheet.find('Pond')) #หาตำแหน่ง
#print(worksheet.findall('upup')) #ถ้าค่าซ้ำ

#worksheet.delete_row(4)#ลบ

#อัพเดต หลายๆตัว
'''
row =["iam", "poramet", "pond"]
line =11
worksheet.insert_row(row, line)
'''

#ตัวหนา
#worksheet.format('A1:B1', {'textFormat': {'bold': True}})
