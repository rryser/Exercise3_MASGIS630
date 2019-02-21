import arcpy
arcpy.env.workspace = r'C:\Users\rryser\Desktop\Ex3\Exercise_3.gdb\Exercise_3.gdb'
arcpy.env.overwriteOutput = True

#Add crime explanation field here
arcpy.AddField_management('CallsforService','Crime_Explanation','TEXT')
print('Added new field')

#Create feature layer from CallsforService
arcpy.MakeFeatureLayer_management(r"C:\Users\rryser\Desktop\Ex3\Exercise_3.gdb\Exercise_3.gdb\CallsforService","CallsforService_lyr")
print('Created feature layer')

#Write "This is a burglary" into the crime explanation field if the value of field ‘CFSType’ is Burglary Call
data = arcpy.SelectLayerByAttribute_management('CallsforService_lyr', 'NEW_SELECTION', "CFSType = 'Burglary Call'")
print('Finished select by attribute')

inTable = data
fieldName = 'Crime_Explanation'
expression = "This is a burglary"
print('Defined fields for field calc')

#Calculate Field
newField = arcpy.CalculateField_management(inTable, fieldName, expression)
print('Finished calculating field')

# Write the selected features to a different feature class
arcpy.CopyFeatures_management(newField, 'CallsforService')
print("Copied features to CallsforService")

