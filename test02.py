#1. ใช้ ,
print("Hello...",456,'Hi...',True,10+20,"Hey...")
#2. ใช้ + มีข้อแม้ว่าทุกตัวที่เอามาต่อกนต้องเป็น String
print("Hello... "+str(456)+' Hi... '+str(True)+' '+str(10+20)+" Hey...")
#3 ใช้เมธอด format
print("Hello... {} Hi... {} {} Hey...".format(456,True,10+20))