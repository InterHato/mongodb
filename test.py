import json
import sys
if len(sys.argv)>1:
	with open(sys.argv[1]) as json_data:
		data = json.load(json_data)
		print(data)
		from pandas import json_normalize
		finaldata=json_normalize(data)
		
		print(finaldata)
		json1=finaldata.reset_index().to_dict(orient='records')


		[newjson]=json1
		print(newjson)
		del newjson['index']
		print(type(newjson))
		with open('result.json', 'w') as fp:
			json.dump(newjson, fp)
else:
	print("please enter required arguments")