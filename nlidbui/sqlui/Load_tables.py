f = open(r"D:\MSCS\Thesis\Natural Language Interface for Databases\Project\Text2SQL\nlidbui\sqlui\tables.jsonl") 
data=f.readlines()

f2 = open('tables','w')
import json
for l in data:
    l = json.loads(l.strip())
    name = l.get("name")
    if not name:
        name = "table_"+l.get("id").replace("-","_") 
    print("(\"",name.strip(),"\", \"",l.get("id").strip(),"\"),")
    name = name.strip() 
    id = l.get("id").strip()
    f2.write(name+", "+id+",\n")

f2.close()
