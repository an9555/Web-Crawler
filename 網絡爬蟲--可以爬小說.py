import requests
from bs4 import BeautifulSoup
import openpyxl

# 创建Excel工作簿和工作表
workbook = openpyxl.Workbook()
worksheet = workbook.create_sheet(title='Novel Content')

for x in range(60):
    page = x + 1
    url = "https://www.bg3.co/novel/pagea/wanxiangzhiwang-tiancantudou_" + str(page) + ".html"
    # 发送HTTP请求
    response = requests.get(url)
    # 将HTML文档传递给Beautiful Soup
    soup = BeautifulSoup(response.text, "html.parser")
    for content in soup.find_all('p'):
        worksheet.append([content.text])

# 保存Excel文件
workbook.save('novel_content.xlsx')
print("成功保存Excel文件")
