// $('#search-input input[type="search"]').on("keyup input", function(){
//     //alert("hijack");
//   var inputVal = $(this).val();
//   //console.log(inputVal);
//   var resultDropdown = $('#search-result');
//   if(inputVal.length){
//       var protocol = location.protocol;
//       $.ajax({
//           dataType: "json",
//           url: protocol+"//algoworld.in/backend-search.php", 
//           data : {term: inputVal},
//           success:function(data){
//           // Display the returned data in browser
//              //alert("2");
//           //var obj = $.parseJSON(data);

          
//           resultDropdown.empty();
//           var suser = "<?php echo $sessionuser ?>";
//            $.each(data, function(index, item) {
//           //   alert("1.5");
//           if (item.status){
//           //resultDropdown.html(item.name);
//            var result = '<div  style="padding-left:5%; padding-bottom: 4%;" ><a href="https://algoworld.in/productdetails.php?id='+item.id+'"  >'+item.name+'</a></div>';
//           // var link1 = "shop/joomla/benchmark/index.php?id="+item.id;
//           // var thelink = $('<a>',{
//           //   text: item.name,
//           //   title: item.name,
//           //   href: link1,
//           //   }).appendTo(resultDropdown);
//           //   resultDropdown.append("<br>");
//           // }
//           resultDropdown.append(result);
//             //$(result).insertAfter(resultDropdown);
//          // resultDropdown.append("<a href=\"shop/joomla/benchmark/index.php?id="+data.id+">"+data.name+"</a>");
//           }
//           else {
//             resultDropdown.html("No Match Found");
//           }
//           });
//           }
//       });
//   } else{
//       resultDropdown.empty();
//   }
// });

// // Set search input value on click of result item
// $(document).on("click", "#search-result p", function(){
//   $(this).parents("#search-input").find('input[type="text"]').val($(this).text());
//   $(this).parent("#search-result").empty();
// });

// $(function () {
//   $("#navbarToggle").click(function (event) {
//     $(event.target).focus();
//   });
// });