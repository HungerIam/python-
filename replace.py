import os
import sys
#递归遍历文件夹，筛选符合要求的文件，并执行替换重命名
def replaceFileName(rootDir,oldStr,newStr);
	for dir in os.listdir(rootDir):
		filepath=rootDir+"/"+dir
		if os.path.isdir(filepath):
			replaceFileName(filepath,oldStr,newStr)
		else
			#检查文件名称格式
			print("filepath = ",filepath)
			isln=oldStr in dir
			if isIn==true:
				dir=dir.replace(oldStr,newStr)
				print("dir = ",dir)
				os.rename(filepath,rootDir+"/"+dir)+dir)
def  main(argv):
	print("argv = ",argv[0])
	rootDir = argv[1]
	oldStr = argv[2]
	newStr = argv[3]
	replaceFileName(rootDir,oldStr,newStr)
#执行流
	if_name_=='_main_':
		main(sys.argv)	