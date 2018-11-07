from BaseData import BaseData

class LocationData(BaseData):
	def __init__(self):
		BaseData.__init__(self, 'Locations!A7:T', "Location")

class DepartmentData(BaseData):
	def __init__(self):
		BaseData.__init__(self, 'Departments!A7:B', "Departments")


class UsersData(BaseData):
	def __init__(self):
		BaseData.__init__(self, 'Users!A8:J', "Users")


class UserRolesData(BaseData):
	def __init__(self):
		BaseData.__init__(self, 'Roles!A12:D', "UserRoles")


class ApprovalRoutingData(BaseData):
	def __init__(self):
		BaseData.__init__(self, 'Approval Routing!A8:F', "ApprovalRouting")


class AccountCodeData(BaseData):
	def __init__(self):
		BaseData.__init__(self, 'Account Codes!A8:F', "AccoutCode")


class BudgetsData(BaseData):
	def __init__(self):
		BaseData.__init__(self, 'Budgets!A11:G', "Budgets")


class VendorListData(BaseData):
	def __init__(self):
		BaseData.__init__(self, 'Vendor List!A3:AA', "VendorList")


class ProductCatalogData(BaseData):
	def __init__(self):
		BaseData.__init__(self, 'Product Catalog!A6:H', "ProductCatalog")
