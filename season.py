def season(month):
   if month == 12 or 1 <= month <= 2:
       print('Winter')
   elif  3 <= month <= 5:
       print('Spring')
   elif 6 <= month <= 8:
       print('Summer')
   elif 9 <= month <= 11:
       print('Autumn')
print(season(7))