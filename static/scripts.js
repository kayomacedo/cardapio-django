var cartItems = document.getElementById("cart-items");

let myCar = document.querySelector('#my-car');

const cartProdocts = document.getElementsByClassName("cart-product")


if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready
}


function ready() {



    myCar.addEventListener('click', descerCarrinho)

    const removeButtons = document.getElementsByClassName("remover")
    for (var i = 0; i < removeButtons.length; i++) {
        removeButtons[i].addEventListener('click', removeProducts)
        updateTotal()
    }
    const addNoCarrinhoButtons = document.getElementsByClassName("addCarrinho")
    
   for (var i = 0 ; i < addNoCarrinhoButtons.length ; i++){
        addNoCarrinhoButtons[i].addEventListener('click',(event)=>{
            const button = event.target
            const productsInfo = button.parentElement.parentElement
            var title = productsInfo.getElementsByClassName("title")[0].innerText
            var preco = productsInfo.getElementsByClassName('preco')[0].innerText.replace("Preço: ",'')
            var imagem = productsInfo.getElementsByClassName('img-pizza')[0].src
            var newCartProduct = document.createElement("tr");
            newCartProduct.classList.add("cart-product")

            newCartProduct.innerHTML = `
            <td>
            <img src="${imagem}"
                alt="${title}" srcset="">
            </td>
            <td class="title">${title}</td>
            <td class="product-price">${preco}</td>
            <td class="remover"><button>X</button></td>
            
            `
            const tableBody =document.querySelector(".card-table tbody")
            tableBody.append(newCartProduct)
            updateTotal()
            newCartProduct.getElementsByClassName('remover')[0].addEventListener('click',removeProducts)
            
            var msg = getElementById('msg')
            console.log(msg)
           
   })   
   }

}

function descerCarrinho(event) {

    if (cartItems.style.display === "block") {
        cartItems.style.display = "none";
    } else {
        cartItems.style.display = "block";
    }
}



function removeProducts(event){
    event.target.parentElement.parentElement.remove()
    updateTotal()

}





function updateTotal() {
    var valorFinal = 0
    for (i = 0; i < cartProdocts.length; i++) {
        try{

            productPrice = parseFloat(cartProdocts[i].getElementsByClassName("product-price")[0].innerText.replace("R$", "").replace(",", "."));
            valorFinal += productPrice
        }
        catch{
            valorFinal = 0
        }
    }


    var valorFinalMostrado = document.getElementById('final').innerText = 'RS ' + valorFinal.toFixed(2).replace('.', ',')


}