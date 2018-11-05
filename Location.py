from BaseData import BaseData

class LocationData(BaseData):
	def __init__(self):
		BaseData.__init__(self, 'Locations!A8:T')

class DepartmentData(BaseData):
	def __init__(self):
		super(DepartmentData, self, 'Departments!A8:B')

