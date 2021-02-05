import xml.dom.minidom
dom = xml.dom.minidom.parseString(xmlString)
xml = dom.toprettyxml()
print(xml)
