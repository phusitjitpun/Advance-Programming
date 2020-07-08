class Calculate_area:

    # Instance Method เรียกโดยมี object เท่านั้น
    def rectangle_area(self, w, h):
        return w * h

    @classmethod #ใช้ตัวแปลใน cls ได้
    def triangle_area(cls, b, h):
        return 0.5 * b * h

    @staticmethod #ใช้ตัวแปลด้านนอก
    def cicle_area(r):
        return 3.14 * r * r

#Objct
cal = Calculate_area()
cal_rec = cal.rectangle_area(4, 5)
cal_tri = cal.triangle_area(4, 5)
cal_circle = cal.cicle_area(5)

print('Rectangle Area = ', cal_rec)
print('Triangle Area = ', cal_tri)
print('Circle Area = ', cal_circle)

#print('Test Triangle Area', Calculate_area.triangle_area(5, 6))
print('Test Circle Area', Calculate_area.cicle_area(5))
#print('Test Rectangle Area', Calculate_area.rectangle_area(5, 6))
