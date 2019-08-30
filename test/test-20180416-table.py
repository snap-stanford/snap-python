import snap

#tsv_file = "data-table1.txt"
tsv_file = "data/data-table.txt"

print("writing table")
context = snap.TTableContext()
schema = snap.Schema()
schema.Add(snap.TStrTAttrPr("srcID", snap.atInt))
schema.Add(snap.TStrTAttrPr("dstID", snap.atInt))
schema.Add(snap.TStrTAttrPr("distance", snap.atFlt))
#schema.Add(snap.TStrTAttrPr("distance", snap.atStr))

table = snap.TTable.LoadSS(schema, tsv_file, context, "\t", snap.TBool(False))
#FOut = snap.TFOut(table_file)
#table.Save(FOut)
#FOut.Flush()

tmp = table.BegRI()
while tmp < table.EndRI():
    #print(str(tmp))
    #print(tmp.GetFltAttr('distance'))
    print(tmp.GetIntAttr('srcID'), tmp.GetIntAttr('dstID'), tmp.GetFltAttr('distance'))
    #print(tmp.GetIntAttr('srcID'), tmp.GetIntAttr('dstID'), tmp.GetStrAttr('distance'))
    tmp.Next()

