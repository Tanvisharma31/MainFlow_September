// if (localStorage.getItem('cart') == null){
//     var cart = {};
// }

// else{
//     cart = JSON.parse(localStorage.getItem('cart'));
//     document.getElementById('cart').innerHTML = Object.keys(cart).length
//     for(item in cart){
//         console.log(item)
//         if (document.getElementById(item) != null){
//             document.getElementById(item).innerText = "Added";
//             document.getElementById(item).style.color = "green";
//             document.getElementById(item).style.background = "#b692f6"
//         }
//     }
// }

// $('.cart').click(function(){
//     var idstr = this.id.toString();
//     if (cart[idstr] == undefined){
//         cart[idstr] = 1;
//         for(item in cart){
//             if (document.getElementById(item) != null){
//                 document.getElementById(item).innerText = "Added";
//                 document.getElementById(item).style.color = "green";
//                 document.getElementById(item).style.background = "#b692f6"
//             }
//         }
//     }
//     else{
//         // cart[idstr] = 1;
//     }
//     localStorage.setItem('cart', JSON.stringify(cart));
//     document.getElementById('cart').innerHTML = Object.keys(cart).length
//     // console.log(cart)
// })



