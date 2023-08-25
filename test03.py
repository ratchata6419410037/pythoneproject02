#รับค่า/ป้อนทางแป้นพิมพ์ ใช็ฟังก์ชั่น input() โดยสิ่งที่ป้อนทั้งหมดถือเป็น String

#ตัวแปร variable เป็น indentifier มีหน้าที่เก็บข้อมูลที่เกิดขึ้นในโปรแกรม ข้อมูลที่เก็บจะอยู่ใน RAM 
#identifier คือ ชื่อที่ dev. ตั้งขึ้นมาเอง ต้องเป็นไปตามกฏการตั้งชื่อของภาษานั้นๆ

std_id = input('ป้อนรหัสนักศึกษา : ')
std_name = input('ป้อนชื่อนักศึกษา : ')
stdYearBorn = input('ป้อนปีเกิด : ')
print('----------------')
print(f"ยินดีต้อนรับ {std_id} ชื่อ {std_name}")
stdAge = 2023 - int(stdYearBorn) #ต้องแปลง String เป็น number -> int( ), float( )
print(f"ยินดีต้อนรับ {std_id} ชื่อ {std_name}")
print(f"คุณเกิดปี {stdYearBorn} อายุ {std_name}")
print() #ใช้ ,
print("ยินดีต้อนรับ",std_id,"ชื่อ",std_name)
print("คุณเกิดปี",stdYearBorn,"อายุ",stdAge,)
print('..................................')
print() #ใช้+
print("ยินดีต้อนรับ "+str(std_id)+' ชื่อ '+str(std_name))
print("คุณเกิดปี "+str(stdYearBorn)+' อายุ '+str(stdAge))
print('..................................')
print() #ใช้ เมธอต format
print("ยินดีต้อนรับ {} ชื่อ {} ".format(std_id,std_name))
print("คุณเกิดปี {} อายุ {} ".format(stdYearBorn,stdAge))
print('..................................')
print() #ใช้ %
print("ยินดีต้อนรับ %s ชื่อ %s " %(std_id,std_name))
print("คุณเกิดปี %s อายุ %s " %(stdYearBorn,stdAge))