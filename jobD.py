import json
import urllib2

class Job:

	count = 0;

	def __init__(self, jobDict):
		if jobDict == 0:
			self.name = 1
		else:
			self.name = jobDict["account_name"]
			self.qtime = jobDict["qtime"]
			self.queue = jobDict["queue"]
			self.state = jobDict["job_state"]
			self.wallrequest = jobDict["walltime_req"]
			self.starttime = jobDict["start_time"]
			self.mtime = jobDict["mtime"]
			self.owner = jobDict["job_owner"]
			self.node = jobDict["nodect"]
			self.id = jobDict["job_id"]
			self.core = jobDict["ppn"]
    
			self.color = "I don't know"
			self.size = "I don't konw"
    
	def getData(self):
		req = urllib2.Request('http://sentinel.sdsc.edu/data/jobs/gordon')
		response = urllib2.urlopen(req, 'r')
		jsonStr = response.read()
		data = json.loads(jsonStr)["jobs"]
		dic = {}
		for x in range(0, len(data)):
			dic[x] = Job(data[x])
		return dic

    
	def displayJob(self):
		print "Name : ", self.name, ", qitme : ", self.qtime, ", queue : ", self.queue, ", state : ", self.state, ", wallrequest : ", self.wallrequest, self.color      
 	
#Job_1 = Job(1,2,3,4,5,6,7,8,9,10,11)
#Job_1.displayJob();