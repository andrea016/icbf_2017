
function mensagesWarning(titulo,campo,texto,duracion){
  var Notify=new PNotify({
	title:titulo,
	text: campo+' '+texto,
	type:"warning",
	addclass: "alert-styled-left",
	delay:duracion,
	animation:"fade",
	mobile:{swipe_dismiss:true,styling:true},
	buttons:{closer:false,sticker:false},
	desktop: {desktop: true,fallback: true},
  });
  Notify.get().click(function() {
      Notify.remove();
  });
}

function mensagesSuccess(titulo,campo,texto){
  var Notify=new PNotify({
	title:titulo,
	text: campo+' '+texto,
	type:"success",
	addclass: "alert-styled-left",
	delay:2000,
	animation:"fade",
	mobile:{swipe_dismiss:true,styling:true},
	buttons:{closer:false,sticker:false},
	desktop: {desktop: true,fallback: true},
  });
  Notify.get().click(function() {
      Notify.remove();
  });
}
function mensagesError(titulo,campo,texto){
  var Notify=new PNotify({
	title:titulo,
	text: campo+' '+texto,
	type:"error",
	addclass: "alert-styled-left",
	delay:3000,
	animation:"fade",
	mobile:{swipe_dismiss:true,styling:true},
	buttons:{closer:false,sticker:false},
	desktop: {desktop: true,fallback: true},
  });
  Notify.get().click(function() {
      Notify.remove();
  });
}
