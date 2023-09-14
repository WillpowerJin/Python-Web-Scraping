import sys

from lxml import etree


folder_path = sys.path[0]

with open(f"{folder_path}/page_source.html", "r", encoding="utf-8") as f:
    page_source = f.read()

tree = etree.HTML(page_source)

# tr1
tr1_list = tree.xpath("//div/table/tbody/tr[1]/td/p/span/font/text()")
tr1_list = [i.strip() for i in tr1_list]
# print(tr1_list)
bixuan_number = f"{tr1_list[0]}: {tr1_list[1]}"
fabu_data = f"{tr1_list[2]}: {''.join(tr1_list[3:])}"
# print(bixuan_number, fabu_data)

# tr2
tr2_list = tree.xpath("//div/table/tbody/tr[2]/td/p/span/font/text()")
tr2_list = [i.strip() for i in tr2_list]
bixuan_name = f"{tr2_list[0]}: {tr2_list[1]}"
# print(bixuan_name)

# tbody
tbody_list = tree.xpath("//div/table/tbody//font/text()")
tbody_list = [i.strip() for i in tbody_list]
print(tbody_list)
