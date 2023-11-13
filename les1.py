# def kopaytir ( * sonlar):
#      kopaytma = 1
#      for son in sonlar:
#       kopaytma*= son
#      return kopaytma
# print (kopaytir (5,5,6))
def talaba_info (ism, familya, **malumotlar):
    malumotlar ["ism"] = ism
    malumotlar ["familya"] = familya
    return malumotlar
talaba1 = talaba_info ("Iqbol", "Xidirov", yosh= 38, tjoy= "Fergana", kasbi ="policeman")
talaba2 = talaba_info ("Dilrabo", "Xidirova", yosh =32, tjoy= "Fergana")
