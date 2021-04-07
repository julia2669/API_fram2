import  xlrd
from common.public import filePath
from utils.operationYaml import OperationYaml
from common.public import *

class ExcelVarles:
	caseID=0
	des=1
	url=2
	method=3
	data=4
	expect=5

	@property
	def getCaseID(self):
		return self.caseID

	@property
	def description(self):
		return self.des

	@property
	def getUrl(self):
		return self.url

	@property
	def getMethod(self):
		return self.method

	@property
	def getData(self):
		return self.data

	@property
	def getExpect(self):
		return self.expect

class OperationExcel(OperationYaml):
	def getSheet(self):
		book=xlrd.open_workbook(filePath('data','books.xlsx'))
		return book.sheet_by_index(0)

	@property
	def getRows(self):
		'''获取总行数'''
		return self.getSheet().nrows

	@property
	def getCols(self):
		'''获取总列数'''
		return self.getSheet().ncols

	def getValue(self,row,col):
		return self.getSheet().cell_value(row,col)

	def getCaseID(self,row):
		return self.getValue(row=row,col=ExcelVarles().getCaseID)

	def getUrl(self,row):
		url=self.getValue(row=row, col=ExcelVarles().getUrl)
		if '{bookID}' in url:
			return str(url).replace('{bookID}',readContent())
		else:
			return url

	def getMethod(self,row):
		return self.getValue(row=row, col=ExcelVarles().getMethod)

	def getData(self,row):
		return self.getValue(row=row,col=ExcelVarles().getData)

	def getJson(self,row):
		return self.dictYaml()[self.getData(row=row)]

	def getExpect(self,row):
		return self.getValue(row=row, col=ExcelVarles().getExpect)

if __name__ == '__main__':
    obj=OperationExcel()
    print(obj.getJson(row=2))
    print(type(obj.getJson(row=2)))


