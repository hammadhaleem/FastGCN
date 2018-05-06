import os, json 

from random import shuffle


def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

def read_partition(data_path = "/home/hammad/graphs_in_deep_vis/data/package/all/", parts=3):
	meta_data =[]
	for root, dirs, files in os.walk(data_path, topdown=False):
		for file in files:
			file_path = os.path.join(root, file)
			with open(file_path) as data_file:
				meta_json = json.load(data_file)
				meta_data.append(meta_json)

	shuffle(meta_data)
	shuffle(meta_data)
	shuffle(meta_data)
	shuffle(meta_data)

	ds_part = list(chunkIt(meta_data , parts))

	str_ = "part_"
	count = 1
	for part in ds_part:
		folder_name = str_ + str(count)

		if not os.path.exists(data_path + '/' + folder_name):
			os.makedirs(data_path + '/' + folder_name)

		for item in part:
			name = item['name'] +".json"
			pth = data_path + '/' + folder_name + '/' + name
			print(pth)
			open(pth, "w+").write(json.dumps(item))
		count +=1

read_partition()
