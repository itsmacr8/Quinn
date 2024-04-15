from selenium import webdriver

edge_options = webdriver.EdgeOptions()
edge_service = webdriver.EdgeService('.\edgedriver\msedgedriver.exe')
DRIVER = webdriver.Edge(options=edge_options, service=edge_service)
