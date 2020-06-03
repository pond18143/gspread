# gspread

1.สร้างโปรเจกต์ https://console.developers.google.com/cloud-resource-manager

2.เข้าAPIs & Services สร้าง  Credentials

3.Enable googlesheet api

3.ดาวน์โหลดไฟล์json

client_emailคือเมลที่ใช้เชิญ

#print(worksheet.get_all_values()) #ปริ้นทั้งหมด

#print(worksheet.row_values(1)) #ปริ้นrow 
#print(worksheet.col_values(2)) #ปริ้นcol

#print(worksheet.acell('A2')) #ปริ้น A2
#print(worksheet.cell(1,2)) #ปริ้น rown1 column2

#print(worksheet.cell(2,1).value) #ปริ้นค่าcell
#print(worksheet.cell(2,1).row) #บอกว่าอยู่rownไหน .col ได้

#worksheet.update_acell('B2', 'testupdate acell') #อัพเดตB2 เป็นประโยคหลัง สามารถลบ_acellได้
#worksheet.update_cell(3,1, 'upup') #อัพเดต r3 c1
#worksheet.update('A2', [[1, 2], [3, 4]])

#print(worksheet.find('upup')) #หาตำแหน่ง
#print(worksheet.findall('upup')) #ถ้าค่าซ้ำ

#worksheet.delete_row(4)#ลบ


#อัพเดต หลายๆตัว
'''
row =["iam", "poramet", "pond"]
line =5
worksheet.insert_row(row, line)
'''

#ตัวหนา
worksheet.format('A1:B1', {'textFormat': {'bold': True}})
