import os

print("\n\nLinux Commands")
print()
print()
print("Press 1 for Creating LVM partition")
print()
print()
a=input("Want you want: ")
while(True):

	if(int(a)==1):
		print("press 1: to create physical volume")
		print("press 2: to create volume group")
		print("press 3: to see volume group detail detial")
		print("press 4: to create logical volume(LV)")
		print("press 5: to see lv detail")
		print("press 6: to format lv")
		print("press 7: to mount lv")
		print("press 8: to extend LV")	
		print("press 9: to format new disk")
		print("press 10: to extend vg")
		print("press 11: to see all available disk")
		print("press 12: to exit")


		print()


		c=input("What you want: ")
		if(int(c)==1):
			p=input("Enter disk name e.g. /dev/sdb: ")
			os.system("pvcreate "+p)
			input("press Enter to continue: ")
			os.system("clear")
		if(int(c)==2):
			p=input("Enter Volume group name: ")
			z=input("Enter PV namd space sperated e.g. /dev/sdb /dev/sdc: ")
			os.system("vgcreate "+p+" "+z)
			input("press Enter to continue: ")
			os.system("clear")
		elif(int(c)==3):
			p=input("Enter dvg nane: ")
			os.system("vgdisplay "+p)
			input("press Enter to continue: ")
			os.system("clear")
		elif(int(c)==4):
			p=input("Enter lv nane: ")
			s=input("Enter size: ")
			v=input("Enter vg name: ")
			os.system("lvcreate --size +"+s+" --name "+p+" "+v)
			input("press Enter to continue")
			os.system("clear")
		elif(int(c)==5):
			p=input("Enter vg name: ")
			l=input("Enter lg name: ")
			os.system("lvdisplay "+p+"/"+l)
			input("press Enter to continue")
			os.system("clear")

		elif(int(c)==6):
			p=input("Enter vg name: ")
			l=input("Enter lg name: ")
			os.system("mkfs.ext4 /dev/"+p+"/"+l)
			input("press Enter to continue")
			os.system("clear")
		elif(int(c)==7):
			p=input("Enter vg name: ")
			l=input("Enter lg name: ")
			f=input("Enter floder name: ")
			os.system("mkdir /"+f)
			os.system("mount /dev/"+p+"/"+l+" "+"/"+f)
			input("press Enter to continue")
			os.system("clear")
		elif(int(c)==8):
			p=input("Enter lv nane: ")
			s=input("Enter size: ")
			v=input("Enter vg name: ")
			os.system("lvextend --size +"+s+" /dev/"+v+"/"+p)
			input("press Enter to continue")
			os.system("clear")
		elif(int(c)==9):
			p=input("Enter vg name: ")
			l=input("Enter lg name: ")
			os.system("resize2fs /dev/"+p+"/"+l)
			input("press Enter to continue")
			os.system("clear")
		elif(int(c)==10):
			v=input("Enter vg name: ")
			p=input("Enter pv name: ")
			os.system("vgextend "+v+" "+p)
			input("press Enter to continue")
			os.system("clear")
		elif(int(c)==11):
			os.system("fdisk -l")
			input("press Enter to continue")
			os.system("clear")
		elif(int(c)==12):
			break
		elif(int(c)==13):
			z=input("ENter folder name: ")
			os.system("mkdir /"+z)
			input("press Enter to continue")
			os.system("clear")
