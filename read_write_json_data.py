import json

def read_data(filename):
    with open(filename,"r") as infile:
        results = json.loads(infile.read())
        print(len(results),"tweets read from",filename)
        return results

def write_data(results,filename):
    with open(filename,"w") as outfile:
        outfile.write(json.dumps(results))
        print(len(results),"written to",filename)

def append_data(results,filename):
    with open(filename,"r") as infile:
        earlier_results = json.loads(infile.read())
    with open(filename,"w") as outfile:
        total_results = earlier_results + results
        outfile.write(json.dumps(total_results))
        print(len(earlier_results),"earlier tweets written to",filename)
        print(len(results),"new tweets written to",filename)
