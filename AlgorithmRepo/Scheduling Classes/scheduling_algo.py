import sys
sys.path.insert(0,"../communication_module")

import random
import copy
import ast 
import communication_module
import statistics
from _thread import *
import threading 
from operator import itemgetter



old_str=""
new_str=""
tststr=""

class_details={}
map_room_sub={} #actual schedule
map_subj_all={}
map_sid_room={}
map_room_sid={}
capacity_room=list()
map_sid_subj_prof={}
acadoffile_email=""


def Sort(sub_li):
	# sub_li.sort(key = lambda x: x[0])
	# print("!!!!!!!!!!",sub_li) 
	# return sub_li 
	return(sorted(sub_li, key = lambda x: x[0]))

def mycmp(a, b):
  res = cmp(a[0], b[0])
  if res == 0:
     return cmp(a[1], b[1])
  return res


'''  
# Driver Code 
sub_li =[['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]] 
print(Sort(sub_li))
'''


def create_schedule(msg):
	#msg ={"senid1:[120,200]","senid2:[150,250]","senid3:[180,200]"}
	print("rec:",msg)
	message = msg
	if (isinstance(message, dict)):
		res=message	
	else:
		res = ast.literal_eval(message)

	global class_details,map_subj_all,map_room_sub,map_sid_room,map_room_sid
	global capacity_room,map_sid_subj_prof,acadoffile_email,tststr
	lisoflis=[]
	for i in res:
		# l1=[]
		l1=res[i]
		l1.append(i)
		lisoflis.append(l1)

	##lisoflis[[120,200,senid1],[150,250,senid2],[180,200,senid3]]

	# sortedlisoflis=Sort(lisoflis)
	sortedlisoflis=lisoflis
	sortedlisoflis.sort(key=lambda x: x[0])


	###sortedlisoflis[[120,200,senid1],[150,250,senid2],[180,200,senid3]]

	### lislis =[capacity,room] sorted list capacity_room

	
	subj_prof_newroom=[]#######to be printed

	for i in sortedlisoflis:
		newlis=[]

		sid=i[2]
		
		prof= map_sid_subj_prof[sid][1]
		subj= map_sid_subj_prof[sid][0]

		curattend=i[0]
		newlis.append(subj)
		newlis.append(prof)

		flgset=[]

		for j in capacity_room:
			if (j[0]>=curattend) and j not in flgset:
				newlis.append(j[0])
				flgset.append(j)
				break

		subj_prof_newroom.append(newlis)


	print("updated schedule",subj_prof_newroom)

	# tststr=""
	tststr="Subject  Old Room  New Room \n\n"
	for i in map_room_sub:
		val=""
		for j in subj_prof_newroom:
			if j[0]==map_room_sub[i]:
				val=j[2]
				break
		tststr=tststr+str(map_room_sub[i])+" "+str(i)+" : "+val+"\n"

	print(tststr)#######subject old room and new room 
	tempmap={}
	for i in subj_prof_newroom:
		# tempmap[i[0]]=[i[1],i[2]]
		l1=[]
		nsid=map_room_sid(i[2])
		tempmap[nsid]=[i[0],i[1]]

	map_sid_subj_prof.clear()

	map_sid_subj_prof=copy.deepcopy(tempmap)
	##1 prf email->roomno
	##2 acadoffile : (roomno->subj)for all

	lis1tosend=[]
	lis2tosend=[]
	lis2tosend.append(acadoffile_email)

	for i in newsid_subj_prof:
		listemp=[]
		listemp2=[]
		listemp.append(i[2])
		listemp.append(map_sid_room[i[0]])
		lis1tosend.append(listemp)

		listemp2.append(map_sid_room[i[0]])
		listemp2.append(i[1])
		lis2tosend.append(listemp2)

	mess1={}
	mess1['UserID']=acadoffile_email
	mess1['App_Name']="Reschedule"
	mess1['Action_type']="Notification"
	mess1['Output']=lis2tosend

	communication_module.RuntimeServer_to_ActionServer_Producer_interface(mess1)
	
	# mess12={}
	for i in lis1tosend:
		email=i[0]
		roomno=i[1]
		mess1={}
		mess1['UserID']=email
		mess1['App_Name']="Reschedule"
		mess1['Action_type']="Notification"
		mess1['Output']=roomno

		communication_module.RuntimeServer_to_ActionServer_Producer_interface(mess1)

	# communication_module.RuntimeServer_to_ActionServer_Producer_interface(lis2tosend)





	# var++;
	###update data current

fun1=create_schedule

def threaded_cls_detaisl():
	while True:
		communication_module.common_Attendence_interface(fun1)

def read_init_data(sensor_data):
	global class_details,map_subj_all,map_room_sub,map_sid_room,capacity_room,map_sid_subj_prof,map_room_sid,acadoffile_email

	f1=open("../Application Manager/config/extra_data/schedule.txt")
	lines1=f1.readlines()
	# print(lines1)
	# based on current data_current schd=edule for tomorrow
	#
	j=0
	k=-1
	for i in lines1:
		j=j+1
		k=k+1
		if(j==1 or j==2):
			if j==1:
				l1=i.strip()
				l2=l1.split("-")
				acadoffile_email=l2[1]
			continue
		l1=i.strip()
		ls=l1.split(":")
		class_details[ls[0]]=[sensor_data[k][1],ls[5]]### {class_no: [sensor , capacity] }

		map_room_sub[ls[0]]=ls[3]
		map_subj_all[ls[3]]=[ls[0],ls[1],ls[2],ls[4],ls[5],sensor_data[k][1]]
		map_sid_room[sensor_data[k][1]]=ls[0]
		map_room_sid[ls[0]]=sensor_data[k][1]
		ll=[int(ls[5]),int(ls[0])]

		capacity_room.append(ll)
		
		map_sid_subj_prof[sensor_data[k][1]]=[ls[3],ls[2]]

	# for i in class_details:
	# 	print(i)
	# random.shuffle(capacity_room)

	print(capacity_room)
	# print(type(capacity_room[0]))
	capacity_room.sort(key=lambda x: x[0])
	print("\n\n\n\n")
	print(capacity_room)







print("Algo Started")
sensor_count=int(sys.argv[1])

sensor_data=[]
x=2
y=3
for i in range(sensor_count):
	topic=sys.argv[x]
	id=sys.argv[y]
	x=x+2
	y=y+2
	for val in communication_module.Sersor_Stream(topic,id):
		print("val:::",val,type(val))
		lis=val.split(":")
		lis.append(id)
		#lis= [atnd, cap, senid]
		sensor_data.append(lis)
		break



read_init_data(sensor_data)
# start_new_thread(threaded_cls_detaisl,())
x=2
y=3

while(1):
	time.sleep(30)
	sensor_data={}

	for i in range(sensor_count):
		topic=sys.argv[x]
		id=sys.argv[y]
		x=x+2
		y=y+2
		lis=list()
		for val in communication_module.Sersor_Stream(topic,id):
			lis=val.split(":")
			break
		sensor_data[id]=lis

	create_schedule(sensor_data)
