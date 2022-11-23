function vta_050()
    	'#################################################################
	'ID Prueba: CP_Vta_050
	'Función de Negocio: Ventas
	'TestName: MTC-FT-014-Limite Efectivo Cajas	
	'Aplicacion: XPOS
	'Criticidad: Crítica/Baja
	'Autor: Gabriel Rubio
	'#################################################################
	'sParameter = "&Producto=75021597&NombreProducto=MTC-FT-014-Limite Efectivo Cajas"
	'sParameter = "&Producto=8100000000&NombreProducto=MTC-FT-014-Limite Efectivo Cajas&"
	sParameter = "&Producto=7503003644460&NombreProducto=NOKIA 3200 TELCEL&"
	
	Dim sTestId, sId, sStep, suiteRunId
	Dim sPswd, sValor
	Dim ObjDesM
	sTestId = "MTC-FT-014-Limite Efectivo Cajas"  'MTC-FT-014-Limite Efectivo Cajas
	sProducto1 = Parameter("sProducto1")
	sNombreProducto = Parameter("sNombreProducto")
	
	suiteRunId = Parameter("suiteRunId")
	
	'Funcion de inicio de ejecucion, aqui se llaman funciones basicas 
	'como limpiar scanner o impresora(funciones de incio) y 
	'funciones para generar reporte y demas
	'¡NO ELIMINAR O COMENTARIZAR!
	inicioEjecucion sTestId, suiteRunId
	
	'### Test ###	
	LimpiarImpresora
		writeTextBox "&devname=txtCode&click=SI&enter=SI", ""
	MensajesFlotantes
	
	Menu Array("Opciones","Menú principal", "Configuraciones","Límite de efectivo")	
    '	wait(2)

    '- "Ingresar a "XPOS"Verificar permita ingresar a "Journal"
    '- Ingresar con el usuario de cajero Verificar permita ingresar con usuario cajero 
    '- Seleccionar del menú principal "Opciones" Verificar permita ingresar a opciones
    '- Seleccionar del submenú la opción "Menú Principal" Verificar permita ingresar al Menú Principal
    '- Seleccionar del submenú la opción "Configuraciones" Verificar permita ingresar a Configuraciones
    '- Seleccionar del submenú la opción "Limite de Efectivo" Verificar permita seleccionar "Limite de Crédito"
    '- Ingresar en "Monto Alerta Máximo"  y seleccionar  "Guardar"Verificar permita capturar el "Monto"
    '- Seleccionar del submenú la opción "Volver" Verificar permita regresar a la pantalla anterior
    '- Seleccionar del submenú la opción "Venta" Verificar permita ingresar a "Venta"
    '- Ingresar articulo al  "Journal" y dar repetir para llegar al monto máximo Verificar permita ingresar articulo

	If WpfWindow("classname:=Oxxo.Xpos.Shell").WpfObject("devname:=Limite de Efectivo en Cajas").Exist(4) Then
			'WpfWindow("classname:=Oxxo.Xpos.Shell").WpfEdit("devname:=LimiteEfectivo").Set "3,000.00" 
			writeTextBox "&devname=LimiteEfectivo&click=SI&enter=SI", "3,800.00"
			wait 2
			WpfWindow("classname:=Oxxo.Xpos.Shell").WpfButton("text:=Guardar").Click
			'pressButton "&Label=Guardar&devname=&index=0&wait=0"
		End If
    wait 3

	pressButton "&Label=Home&devname=btnHome&index=0&wait=0"
	pressButton "&Label=Venta&devname=btnMenu&index=0&wait=0"
			
	MensajesFlotantes
	wait 3
	iCodigo=5
	iNota=5
	For iterator = 1 To iNota Step 1
		wait 1
		Window("text:=Microsoft Scanner Simulator").WinObject("nativeclass:=WindowsForms10\.EDIT.*").Type "2*" & sProducto1
	    Window("text:=Microsoft Scanner Simulator").WinObject("text:=Good Scan").Click
		Window("text:=Microsoft Scanner Simulator").WinObject("nativeclass:=WindowsForms10\.EDIT.*").Click 
	 	simulateUserInput "&Keyboard={END}&"
	 	simulateUserInput "&Keyboard=+{HOME}&"
	 	simulateUserInput "&Keyboard={DEL}&"		
	Next
	pressButton "&Label=$(+)&devname=btnTotalizar&index=0"
	If WpfWindow("classname:=Oxxo.Xpos.Shell").WpfButton("text:=NO DESEO ACUMULAR PUNTOS EN ESTA COMPRA","devname:=btnAbandom").Exist(2) Then
		WpfWindow("classname:=Oxxo.Xpos.Shell").WpfButton("text:=NO DESEO ACUMULAR PUNTOS EN ESTA COMPRA","devname:=btnAbandom").Click
	End If
	
	MensajesFlotantes
	MensajesFlotantes
	Redondeo "&redondear=No&"
	pressButton "&Label=Pagar&devname=btn1&index=0&wait=0"

	wait 2
	MensajesFlotantes
	wait 2
    '- Seleccionar subtotalizar "$(+)"Verificar sea subtotalizado
    '- Seleccionar forma de pago Verificar aplicar el pago
    '- Validar se imprima ticket Verificar impresión de ticket
    '- Validar mensaje "Realiza Retiro", seleccionar "Aceptar"Verificar se presente mensaje informativo
    '- Ingresar contraseña de Asesor   y seleccionar [enter]Verificar permita ingresar con usuario "Asesor"
    '- En pantalla "Pesos/Dólares" ingresar "P" y seleccionar  [enter]Verificar se presente la pantalla 
    '- Ingresar el monto y seleccionar [enter]Verificar permita ingresar el monto
    '- Confirmar Monto y seleccionar opción "SI"Verificar permita ingresar el monto
    '- Validar se imprima ticket "CTRL DE RETIROS"Verificar el ticket "CTRL DE RETIROS"

    If Window("regexpwndtitle:=Microsoft PosPrinter Simulator","regexpwndclass:=WindowsForms10.Window.8.app.*").WinObject("window id:=0","regexpwndclass:=WindowsForms10.EDIT.app.*","nativeclass:=WindowsForms10.EDIT.app.*","index:=1").Exist(2) Then
        Window("regexpwndtitle:=Microsoft PosPrinter Simulator","regexpwndclass:=WindowsForms10.Window.8.app.*").WinObject("window id:=0","regexpwndclass:=WindowsForms10.EDIT.app.*","nativeclass:=WindowsForms10.EDIT.app.*","index:=1").highlight
        sToket=Window("regexpwndtitle:=Microsoft PosPrinter Simulator","regexpwndclass:=WindowsForms10.Window.8.app.*").WinObject("window id:=0","regexpwndclass:=WindowsForms10.EDIT.app.*","nativeclass:=WindowsForms10.EDIT.app.*","index:=1").GetROProperty("text")	
        dFechaActual=Date()
        tHoraActual= time()
        Set fso = CreateObject("Scripting.FileSystemObject")
        Set tf = fso.CreateTextFile("C:\\UFT\\Evidencia\\MTC_FT_014_LimiteEfectivoCajas" & Right("0000" & CSTR(Year(DATEVALUE(dFechaActual))), 4) & Right("00" & CSTR(Month(DATEVALUE(dFechaActual))), 2) & Right("00" & CSTR(Day(DATEVALUE(dFechaActual))), 2) & HOUR (tHoraActual) & MINUTE (tHoraActual) & SECOND (tHoraActual) & ".txt", True )
        'msgbox "C:\\UFT\\MTC_FT_014_LimiteEfectivoCajas" & Right("0000" & CSTR(Year(DATEVALUE(dFechaActual))), 4) & Right("00" & CSTR(Month(DATEVALUE(dFechaActual))), 2) & Right("00" & CSTR(Day(DATEVALUE(dFechaActual))), 2) & HOUR (tHoraActual) & MINUTE (tHoraActual) & SECOND (tHoraActual) & ".txt"	
        wait 1
        tf.Write(sToket)	'sFormula
        tf.Close()
        wait 1
    End If

        'Nota: si se necesita guardar evidencia que no sea de la impresora se agrega aqui, 
            'el formato del nombre de le evidencia debe ser asi: idCasoPrueba_YYYYMMDD(concatenar la variable "sTestId")
            'Ejemplo: CP_Fun_001_20220501...
        
        '#### Test #### Antes de esta seccion insertar el codigo para el script.
        
        'Funcion de fin de ejecucion, aqui se llaman funciones como guardar ticket de impresora
        'y otras funciones de fin, ademas las funciones para generar reporte
        '¡NO ELIMINAR O COMENTARIZAR!
        finEjecucion sTestId, suiteRunId    
end function

function vta_51()
    	'#################################################################
	'ID Prueba: CP_Vta_051
	'Función de Negocio: Ventas - Vales
	'TestName:  		MTC-FT-092-Venta de Cerveza pagando con Vales
	'Aplicacion: XPOS
	'Criticidad: Alta
	'Autor: Gabriel Rubio
	'#################################################################
	'sParameter = "&Producto=50196388&NombreProducto=WSK.BUCHAN 750ML&Precio=730.00&Producto2=1&NombreVale= VALE SI VALE"
	'sParameter = "&Producto=7501061601128&NombreProducto=TECATE 12P 355ML&Precio=180.00&Producto2=0&NombreVale= VALE SI VALE"
	'sParameter = "&Producto=75002459&NombreProducto=TECATE 355ML&Precio=15.50&Producto2=0&NombreVale= VALE SI VALE"
	'sParameter = "&Producto=75021597&NombreProducto=MARLBORO 100S CD&Precio=66.00&Producto2=0&NombreVale= VALE SI VALE"
	'sParameter = "&Producto=7501000300730&NombreProducto=PAN BIMBO LINAZA 610&Precio=43.50&Producto2=1&NombreVale= VALE SI VALE"  'Producto2 = "0" (si NO aplica un segundo producto) Producto2 = "1" (si SI aplica un segundo producto) 
	sParameter = datatable("DT_Datos",dtGlobalSheet)
	Dim sTestId, sId, sStep, suiteRunId
	Dim sPswd, sValor
	Dim ObjDesM
	Suma = 0.00  'Double
	sTestId = "MTC-FT-092-Venta de Cerveza pagando con Vales"  'Formas de Pago Vales, En venta de Alcohol y tabaco (Vales)
	sTermina = "0"
	sProducto = Parameter("sProducto")
	sNombreProducto = Parameter ("sNombreProducto")
	sVale = Parameter ("sVale")
	sValor = Parameter ("sValor")
    '	sProd2 = Parameter ("Producto2")
	sPswd = datatable("DT_Psw",dtGlobalSheet)
    '	sProducto2 = "7501000300730"
    '	sValor2 = "43.50"

	suiteRunId = Parameter("suiteRunId")
	
	'Funcion de inicio de ejecucion, aqui se llaman funciones basicas 
	'como limpiar scanner o impresora(funciones de incio) y 
	'funciones para generar reporte y demas
	'¡NO ELIMINAR O COMENTARIZAR!
	inicioEjecucion sTestId, suiteRunId
	

    '**** Función

	
	'Buscar por descripción el producto de Cerveza
	pressButton "&Label=Desc.&devname=btnSearchByDescription&index=0"
	wait 5
	writeTextBox "&devname=txtCode&click=SI&enter=SI", sNombreProducto	
      
	pressButton "&Label=Aceptar&devname=btnAccept&index=0"
	simulateUserInput "&Keyboard={ENTER}&"
	
	
    ''MENSAJE DE ALERTA DE HORARIO (no se realiza venta)
    If WpfWindow("classname:=Oxxo.Xpos.Shell").WpfObject("devname:=TITLE").Exist(2) And WpfWindow("classname:=Oxxo.Xpos.Shell").WpfObject("text:=Venta fuera de Horario*.*").Exist(1) Then
				pressButton "&Label=Aceptar&devname=acceptButton&index=0"
	 
		Else
		
			If WpfWindow("classname:=Oxxo.Xpos.Shell").WpfObject("devname:=TITLE","text:=Alerta").Exist(5) And WpfObject("classname:=Oxxo.Xpos.Shell").WpfObject("text:=No vendas alcohol a menores de edad*.*").Exist(5) Then
					pressButton "&Label=Aceptar&devname=acceptButton&index=0"
			End If
		
	    	pressButton "&Label=$(+)&devname=btnTotalizar&index=0"   
			MensajesFlotantes
		If WpfWindow("classname:=Oxxo.Xpos.Shell").WpfObject("devname:=¿ Quiere ayudar redondeando \?").Exist(1) Then
		   Redondeo "&redondear=No&"
		End If	
	
	    pressButton "&Label=VALES&devname=A01&index=1"
	    wait 1
		If WpfWindow("classname:=Oxxo.Xpos.Shell").WpfObject("devname:=TITLE").Exist(10) AND WpfWindow("classname:=Oxxo.Xpos.Shell").WpfObject("text:=Por disposición oficial queda prohibido pagar bebidas alcohólicas *.*").Exist(10) Then
				WpfWindow("classname:=Oxxo.Xpos.Shell").WpfObject("text:=Por disposición oficial queda prohibido pagar bebidas alcohólicas *.*").Highlight
				WpfWindow("classname:=Oxxo.Xpos.Shell").WpfButton("devname:=acceptButton").Highlight
				pressButton "&Label=Aceptar&devname=acceptButton&index=0"
		Else
			
			If WpfWindow("classname:=Oxxo.Xpos.Shell").WpfObject("devname:=lblDesc","name:=VALES SI VALE").Exist(1) Then
					WpfWindow("classname:=Oxxo.Xpos.Shell").WpfObject("devname:=lblDesc","name:=VALES SI VALE").click
					simulateUserInput "&Keyboard={ENTER}&"	
					WpfWindow("classname:=Oxxo.Xpos.Shell").WpfObject("devname:=TxbAmount","index:=1").set sValor
					simulateUserInput "&Keyboard={ENTER}&"			
				    pressButton "&Label=Regresar&devname=BtnAceptar&index=0"
			'-----ERROR AL PERMITIR VENTA DE ALCOHOL CON VALES.
					call Workbook_Open("Xposs Permite la venta de Tabaco o Alcohol con Vales de Desensa",10)		   
					datatable("DT_Result",dtGlobalSheet) = "KO"
					datatable("DT_APIType",dtGlobalSheet) = "AMBIENTE"	
					datatable("DT_APITitle",dtGlobalSheet) = "AMBIENTE"  & " - " &  sTestId & " - " & sNombreProducto & " KO "		
					sNombreError = "Xposs Permite la venta de Tabaco o Alcohol con Vales de Desensa. Caso Fallado "			
					sCadena= "--op add -ty bug --t " & sNombreError  & " --sr "  & datatable("DT_StepsToReproduce",dtGlobalSheet)  & " --ac "& datatable("DT_AccCriteria",dtGlobalSheet) 
					'systemutil.run "C:\\OXXO\\Genera bugs\\Ejecutable_CreacionBUG\\Oxxo.Xpos.TFS.Api\\Oxxo.Xpos.TFS.Api.exe", sCadena
					Reporter.ReportEvent micFail,  "Caso de Prueba "& sTestId & " Fallado ", "Xposs Permite la venta de Tabaco o Alcohol con Vales de Desensa. Caso Fallado. "
					sTermina = "1"			
			    
			ELSE
				pressButton "&Label=Pagar&devname=btn1&index=0&wait=0"
				sTermina = "1"
			End If	
		End If
		If sTermina = "0" Then
				  pressButton "&Label=Pagar&devname=btn1&index=0&wait=0"	
		End If
    End If 
			'Nota: si se necesita guardar evidencia que no sea de la impresora se agrega aqui, 
		'el formato del nombre de le evidencia debe ser asi: idCasoPrueba_YYYYMMDD(concatenar la variable "sTestId")
		'Ejemplo: CP_Fun_001_20220501...
	
	'#### Test #### Antes de esta seccion insertar el codigo para el script.
	
	'Funcion de fin de ejecucion, aqui se llaman funciones como guardar ticket de impresora
	'y otras funciones de fin, ademas las funciones para generar reporte
	'¡NO ELIMINAR O COMENTARIZAR!
	finEjecucion sTestId, suiteRunId
    
end function