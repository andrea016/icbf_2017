
function ValidarFormulario(lista,modelo,formulario){
  var correctos =[];
  for (i=0; i<lista.length; i++) {
    if ($("#"+modelo+"_"+lista[i]).val() != ""){
      correctos.push(lista[i]);
    }else{
      validarCampos(modelo,lista[i]);
    }
  }
  if ( correctos.length == lista.length ){
    document.getElementById(formulario).submit();
  }
}

function saveMultiSelect(select,campo){
  lista = [];
  $("#"+select+" :selected").each(function (i,sel) {
    lista.push($(sel).text().toString())
  });
  $("#"+campo).val(lista)
  $("#id_"+campo).val($('#'+select).val())
}

function setMultiSelect(select,multi){
  lista = [];
  for (i=0; i<multi.length; i++) {
    lista.push(multi[i]);
  }
  $("#"+select).val(lista);
}

function setMultiSelect2(select,multi){
  lista = [];
  for (i=0; i<multi.length; i++) {
    lista.push(multi[i]);
  }
  ('#'+select).select2('val',multi);
}


function limpiarMultiSelect2(select){
  for (i=0; i<select.length; i++) {
    $('#'+select[i]).select2('val','');
  }
}

function limpiar(campos){
  for (i=0; i<campos.length; i++) {
    $('#'+campos[i]).val('');
  }
}

function obtenerRespuesta(check,campo){
  // SI YA HE SELCCIONADO UN VALOR LO GUARDO EN EL INPUT
  if ($('input:radio[name='+check+']:checked').val() == 'SI') {
      $("#"+campo).val("S");
  }
  else {
      $("#"+campo).val("N");
  }
  //OBTENER VALOR DEL RADIOBUTTON DETECTANDO EL ONCHANGE
  $('input:radio[name='+check+']').change(function() {
      if (this.value == 'SI') {
          $("#"+campo).val("S");
      }
      else if (this.value == 'NO') {
          $("#"+campo).val("N");
      }
  });
}

//FIJAR EL VALOR DEL RADIOBUTTON
function fijarRespuesta(campo,valor){
  if ($("#"+campo).val() == "S"){
    $("#"+campo+"_"+valor).prop('checked',true);
    return false;
  }
  else if ($("#"+campo).val() == "N") {
    $("#"+campo+"_"+valor).prop('checked',true);
    return false;
  }
}

// FIJA UN SELECT CON UN VALOR
function fijarValorSelect(select_id,valor){
  $("#"+select_id).val(valor);
}

// VERIFICAR QUE UN DATO EXISTA EN UN ARRAY
function VerificarArray(id,lista){
  var array = lista;
  var resultado;
  resultado = $.inArray(id,array);
  if (resultado == -1){
    lista.push(id);
  }
}

// AGREGAR UNA CLASE CSS A UN ARRAY
function AgregarClase(lista,clase){
  for (i=0; i<lista.length; i++) {
    $('#'+lista[i]).addClass(clase);
  }
}

// REMPLAZA TEXTO EN UN ARRAY
function RemplazarTexto(lista,texto){
  for (i=0; i<lista.length; i++) {
    $('#'+lista[i]).text(texto);
  }
}

// CAMBIAR ESTADO DOCUMENTO  SEGUN CHECKED
function estadoDocumento(campo,bandera,formato){
	if ($('input:checkbox[name='+bandera+']:checked').val() == "on"){
		$("#"+formato).attr('required', true);
 }
 else {
		$("#"+formato).attr('required', false);
 }
}

// VALIDAR TIPOS DE ARCHIVO
function ValidarCargaArchivos(modelo,campo,extenciones,check) {
    var _validFileExtensions = extenciones;
    var arrInputs =  $("#"+modelo+"_"+campo);
    for (var i = 0; i < arrInputs.length; i++) {
        var oInput = arrInputs[i];
        if (oInput.type == "file") {
            var sFileName = oInput.value;
            if (sFileName.length > 0) {
                var blnValid = false;
                for (var j = 0; j < _validFileExtensions.length; j++) {
                    var sCurExtension = _validFileExtensions[j];
                    if (sFileName.substr(sFileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {
                        blnValid = true;
                        break;
                    }
                }
                if (!blnValid) {
                    $("#"+modelo+"_"+campo+"_success").hide();
                    $("#"+modelo+"_"+campo+"_error").show();
                    $("#"+modelo+"_"+campo).val("")
                    $(".filename").val("")
                    return false;
                }
            }
        }
    }
    $("#"+modelo+"_"+campo+"_error").hide();
    $("#"+modelo+"_"+campo+"_success").show();
    $("#checkDNI").prop("checked", true);
    return true;
}


// INPUT QUE SOLO ACEPTA NUMEROS
function soloNumeros(e,modelo,id,bandera){
  if (bandera != "NO"){
	   validarCampos(modelo,id);
  }
	var key = window.Event ? e.which : e.keyCode
	return (key >= 48 && key <= 57)
}

// BLOQUEAR INTERFAZ CUANDO SE ENVIAN MULTIPLES PETICIONES AL SERVIDOR (MULTIPLE BORRADO, MULTIPLE EDICION)
function blockPanel(mensaje){
  $.blockUI({
      message: '<i class="icon-spinner10 spinner"></i><div id="custom-message" class="block_ui_font display-block">'+mensaje+'</div>',
      overlayCSS: {
          backgroundColor: '#1b2024',
          opacity: 0.9,
          cursor: 'wait',

      },
      css: {
          border: 0,
          color: 'white',
          padding: 0,
          backgroundColor: 'transparent',
					left: '30%',
					width: '41%',

      }
  });
}


//FUNCION GENERICA PARA BORRAR
function eliminar(url,id,mensaje) {
  var Notify=new PNotify({
  	title: 'ATENCIÓN:',
  	text: 'Una vez eliminado el elemento no podra recuperarse. ¿Esta Seguro?',
    type:"warning",
    addclass: "alert-styled-left",
  	hide: false,
  	confirm: {
  		confirm: true
  	},
  	buttons: {
  		closer: false,
  		sticker: false
  	},
  	history: {
  		history: false
  	}
  }).get().on('pnotify.confirm', function() {
    $.ajax({
        method: "DELETE",
        url: url + id,
    }).done(function (msg) {
        blockPanel(mensaje);
        location.reload();
    });
  }).on('pnotify.cancel', function() {
  })
}

function obtenerGenero(){
	// SI YA HE SELCCIONADO UN VALOR LO GUARDO EN EL INPUT
	if ($('input:radio[name=bedStatus]:checked').val() == 'masculino') {
			$("#genero").val("M");
      fijarGenero();
	}
	else if ($('input:radio[name=bedStatus]:checked').val() == 'femenino') {
			$("#genero").val("F");
      fijarGenero();
	}
	//OBTENER VALOR DEL RADIOBUTTON DETECTANDO EL ONCHANGE
	$('input:radio[name=bedStatus]').change(function() {
			if (this.value == 'masculino') {
					$("#genero").val("M");
          fijarGenero();
			}
			else if (this.value == 'femenino') {
					$("#genero").val("F");
          fijarGenero()
			}
	});

}
//FIJAR EL VALOR DEL RADIOBUTTON
function fijarGenero(){
  if ($("#genero").val() == "M"){
		$( "#masculino" ).prop( "checked", true );
	}
	else if ($("#genero").val() == "F") {
		$( "#femenino" ).prop( "checked", true );
	}
}


//SUBIR IMAGEN
function subirImagen() {
  document.getElementById('archivo').click();
}

$(function() {
  $('#archivo').change(function(e) {
    addImage(e);
  });

   function addImage(e){
    var file = e.target.files[0],
    imageType = /image.*/;

    if (!file.type.match(imageType))
     return;

    var reader = new FileReader();
    reader.onload = fileOnload;
    reader.readAsDataURL(file);
   }

   function fileOnload(e) {
    var result=e.target.result;
    $('#imgSalida').attr("src",result);
		$('#bandera_foto').val("CAMBIO")
   }
});


function adicionarNotas(){
	contacto_id= ($("#contacto_id").val());
	txt_notas = ($("#detallenotas").val().trim());
  validarCampos("notas","detallenotas");
  if (txt_notas != ""){
  	$.ajax({
  	method: "PUT",
  	url: "/guardarNota?contacto_id="+contacto_id+"&txt_notas="+txt_notas,
  	}).done(function( msg ) {
  		 if (msg == "Creada") {
         location.reload();
  			}
  	});
  }
}


function validarCampos(modelo,campo){
  if ($("#"+modelo+"_"+campo).val() == ""){
    $("#"+modelo+"_"+campo).focus();
    $("#"+modelo+"_"+campo+"_success").hide();
    $("#"+modelo+"_"+campo+"_error").show();
  }
  else{
    $("#"+modelo+"_"+campo+"_error").hide();
    $("#"+modelo+"_"+campo+"_success").show();

  }
}


// ACTIVAR OPERARIO
function activarOperario(id) {
		$.ajax({
  		method: "PUT",
  		url: "/activarOperario?id="+id,
  		}).done(function( msg ) {
        mensagesSuccess('EXITO AL ACTIVAR','Operario Activado','Exitosamente')
        setTimeout(function(){
          location.reload();
        }, 3000);
  		});
}

// VERIFICA QUE NO EXISTA EL EMAIL
function verificarEmail() {
		email=($("#email").val());
		$.ajax({
		method: "PUT",
		url: "/verificarEmail?email="+email,
		}).done(function( msg ) {
			if (msg == "Campos Correctos") {
			}
			else if (msg == "El E-MAIL ya Existe"){
					$("#email").focus();
					var str = $("#email").val();
					var ultimo = str.length-1;
					var res = str.substring(0, ultimo);
					$("#email").val(res);
					mensagesError("ERROR:      "+email,"El E-mail","ya Existe.");
				}
		});
}


function EliminarArray(id,lista){
  var array = lista;
  var resultado;
  resultado = $.inArray(id,array);
  if (resultado >= 0){
    lista.splice(resultado,1);
  }
}


var lista_check =[]
// GUARDAR LOS CHECKED SELECCIONADOS
function guardarCheckbox(check, campo){
  if(check.checked){
    VerificarArray(check.value,lista_check)
    $("#"+campo).val(lista_check)
  }else{
    EliminarArray(check.value,lista_check)
    $("#"+campo).val(lista_check)
  }
}


// FIJA LOS CHECKED RECIBIENDO UNA STTRING CONVIRTIENDOLO ARRAY
function setChek(list_check,campo){
  var list = list_check.split(",");
	for (i=0; i<list.length; i++) {
  	$("#"+list[i]).prop( "checked", true );
    $("#"+campo).val(list)
    lista_check.push(list[i])
	}
}


var contacto = [];
function enviar_carta(){
    $("input:checkbox:checked").each(
        function() {
            contacto.push( $(this).val() );
            console.log(contacto);
          }
    );
    //ELIMINAR EL 0 DE LA LISTA
    if (contacto[0] == "0"){
        contacto.shift();
    }
    // AGREGAR LA LISTA DE LOS ID A BORRAR EN EL INPUT lista_contactos_editar
    $("#lista_contactos").val(contacto);

    if ($("#lista_contactos").val() == ""){
      mensagesWarning("","Debe","seleccionar almenos un (1) contacto.",2000);
    }
    else{
        //$( "#carta_email_contactos" ).val($( "#carta_contactos" ).val())
        blockPanel("Enviando Correo por favor espere....");
    		document.getElementById("formCarta").submit();
    }
}
