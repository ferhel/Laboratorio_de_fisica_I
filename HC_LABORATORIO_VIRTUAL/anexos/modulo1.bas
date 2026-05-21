olevba "plantilla.xlsm"
olevba 0.60.2 on Python 3.12.3 - http://decalage.info/python/oletools
===============================================================================
FILE: plantilla.xlsm
Type: OpenXML
WARNING  For now, VBA stomping cannot be detected for files in memory
-------------------------------------------------------------------------------
VBA MACRO Módulo1.bas 
in file: xl/vbaProject.bin - OLE stream: 'VBA/Módulo1'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Sub Posicionconstante()
Attribute Posicionconstante.VB_Description = "Posicion V ctte"
Attribute Posicionconstante.VB_ProcData.VB_Invoke_Func = " \n14"
'
' Posicionconstante Macro
' Posicion V ctte
'

'
    Range("D30").Select
    ActiveCell.FormulaR1C1 = "=R[-9]C+(R[-12]C*R[-6]C)"
    Range("G30").Select
    ActiveCell.FormulaR1C1 = "=R[-9]C+(R[-6]C[-3]*R[-12]C)+(R[-12]C[-3]*R[-6]C)"
    Range("G31").Select
End Sub
Sub aceleracion()
Attribute aceleracion.VB_ProcData.VB_Invoke_Func = " \n14"
'
' aceleracion Macro
'

'
    Range("L31").Select
    ActiveCell.FormulaR1C1 = "=R[-10]C+(R[-13]C*R[-7]C)+(0.5*R[-4]C*R[-7]C*R[-7]C)"
    Range("O31").Select
    ActiveCell.FormulaR1C1 = _
        "=(R[-10]C)+(R[-7]C[-3]*R[-13]C)+((R[-13]C[-3]+(R[-4]C[-3]*R[-7]C[-3]))*R[-7]C)+(0.5*R[-7]C[-3]*R[-7]C[-3]*R[-4]C)"
    Range("O32").Select
End Sub
Sub Vccte_Datos()
Attribute Vccte_Datos.VB_Description = "Generar datos velocidad Constante"
Attribute Vccte_Datos.VB_ProcData.VB_Invoke_Func = " \n14"
'
' Vccte_Datos Macro
' Generar datos velocidad Constante
'

'
    Range("I13").Select
    ActiveCell.FormulaR1C1 = "=0"
    Range("I14").Select
    ActiveCell.FormulaR1C1 = "=R[-1]C+1"
    Range("I14").Select
    Selection.AutoFill Destination:=Range("I14:I23"), Type:=xlFillDefault
    Range("I14:I23").Select
    Range("J13").Select
    ActiveCell.FormulaR1C1 = "=R[-1]C[-3]+(RC[-1]*R[-1]C[-2])"
    Range("J13").Select
    Selection.AutoFill Destination:=Range("J13:J21"), Type:=xlFillDefault
    Range("J13:J21").Select
    Selection.AutoFill Destination:=Range("J13:J23"), Type:=xlFillDefault
    Range("J13:J23").Select
End Sub
Sub Vccte_Grafica()
Attribute Vccte_Grafica.VB_ProcData.VB_Invoke_Func = " \n14"
'
' Vccte_Grafica Macro
'

'
    Range("I13:J23").Select
    ActiveSheet.Shapes.AddChart.Select
    ActiveChart.ChartType = xlXYScatter
    ActiveChart.SetSourceData Source:=Range("Graficación!$I$13:$J$23")
    ActiveChart.PlotArea.Select
    ActiveChart.ChartArea.Select
    ActiveChart.SeriesCollection(1).Select
    ActiveChart.SeriesCollection(1).Trendlines.Add
    ActiveChart.SeriesCollection(1).Trendlines(1).Select
    Selection.DisplayEquation = True
    Selection.DisplayRSquared = True
End Sub
-------------------------------------------------------------------------------
VBA MACRO ThisWorkbook.cls 
in file: xl/vbaProject.bin - OLE stream: 'VBA/ThisWorkbook'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
(empty macro)
-------------------------------------------------------------------------------
VBA MACRO Hoja1.cls 
in file: xl/vbaProject.bin - OLE stream: 'VBA/Hoja1'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
(empty macro)
-------------------------------------------------------------------------------
VBA MACRO Hoja2.cls 
in file: xl/vbaProject.bin - OLE stream: 'VBA/Hoja2'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
(empty macro)
-------------------------------------------------------------------------------
VBA MACRO Hoja3.cls 
in file: xl/vbaProject.bin - OLE stream: 'VBA/Hoja3'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
(empty macro)
-------------------------------------------------------------------------------
VBA MACRO Hoja4.cls 
in file: xl/vbaProject.bin - OLE stream: 'VBA/Hoja4'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
(empty macro)
+----------+--------------------+---------------------------------------------+
|Type      |Keyword             |Description                                  |
+----------+--------------------+---------------------------------------------+
|Suspicious|Hex Strings         |Hex-encoded strings were detected, may be    |
|          |                    |used to obfuscate strings (option --decode to|
|          |                    |see all)                                     |
+----------+--------------------+---------------------------------------------+
