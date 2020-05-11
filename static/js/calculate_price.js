var updateSizes = document.getElementsByClassName('update-size')

for (i = 0; i < updateSizes.length; i++) {
    updateSizes[i].addEventListener('change', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log(productId)
        console.log(action)

        if (user != 'AnonymousUser') {
            UpdateUserOrder(productId, action)
            console.log('loged in user')
        }

    })
}


