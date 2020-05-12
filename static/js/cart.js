<<<<<<< HEAD
var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log(productId)
        console.log(action)

        if (user == 'AnonymousUser') {
            //  sweet alert
            swal('sorry', 'you need to login')
        
        } else {
            UpdateUserOrder(productId, action)
            console.log('loged in user')
        }

    })
}

function UpdateUserOrder(productId, action) {
    // URL you want to send data
    var url = '/update/'
    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'productId': productId,
                'action': action
            })
        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
        });
=======
console.log('hello world')

var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function () {
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId)
		console.log('action:', action)
		console.log('USER:', user)
		if (user === 'AnonymousUser') {
			console.log('not loged in')
		} else {
			updateUserOrder(productId, action)
		}

	})
}


function updateUserOrder(productId, action) {
	console.log('User is authenticated, sending data...')

	var url = '/updateItem/'

	fetch(url, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'X-CSRFToken': csrftoken,
			},
			body: JSON.stringify({
				'productId': productId,
				'action': action
			})
		})
		.then((response) => {
			return response.json();
		})
		.then((data) => {
			console.log('data:', data)
		});
>>>>>>> 5656c02d5a4ca530af0a18ce5ae52133deb031d8
}