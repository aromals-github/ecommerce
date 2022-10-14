var updateButtons =document.getElementsByClassName('update-cart')


for(var i = 0; i< updateButtons.length; i++){
    updateButtons[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this .dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER:', user)
        if(user === 'AnonymousUser'){
            console.log("not logged in")
        }
        else{
            console.log(' user is logged in, start purchasing')
        }
    })
}


function updateUserOrder(productId, action){
    console.log('user is logged in ,sending data ...')
    var url = 'updateitem/'
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action })
    })

    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data:', data)
    })
}