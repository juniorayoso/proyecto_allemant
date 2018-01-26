$(document).ready(function(){
  $("#vin").click(function(){
    $("#occ").slideToggle(500);
    $("i",this).toggleClass("icon-arrow-right-5 icon-arrow-down-5");
  });
});
