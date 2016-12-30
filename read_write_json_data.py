import json

def read_data(filename):
    with open(filename,"r") as infile:
        results = json.loads(infile.read())
        return results

def write_data(results,filename):
    with open(filename,"w") as outfile:
        outfile.write(json.dumps(results))
