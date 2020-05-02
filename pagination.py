class Pagination:

	def __init__(self, items=[], pageSize=10):    
		self.pageSize = pageSize
		count = 0
		dcount = 1
		dict = {}
		for i in range(int(len(items)/self.pageSize)+1):
			dict[dcount] = items[count*self.pageSize:count*self.pageSize+self.pageSize]
			dcount += 1
			count += 1
		if str(len(items))[-1] == '1':
			dict[dcount] = [items[-1]]
		self.items = dict
		self.totalPages = len(self.items)
		self.currentPage = 1
		
	def getItems(self):
		return self.items[self.currentPage]
		
	def getPageSize(self):
		return self.pageSize
		
	def getCurrentPage(self):
		return self.currentPage
		
	def prevPage(self):
		if self.currentPage == 1:
			return self
		self.currentPage -= 1
		return self
		
	def nextPage(self):
		if self.currentPage == self.totalPages:
			return self
		self.currentPage += 1
		return self
		
	def firstPage(self):
		self.currentPage = 1
		return self
		
	def lastPage(self):
		self.currentPage = self.totalPages
		return self
		
	def goToPage(self, page):
		page = int(page)
		if page > self.totalPages:
			self.currentPage = self.totalPages
		if page < 1:
			self.currentPage = 1
		if page > 1 and page > self.totalPages:
			self.currentPage = page
		return self
			
	def getVisibleItems(self):
		return self.items[self.currentPage]
		
