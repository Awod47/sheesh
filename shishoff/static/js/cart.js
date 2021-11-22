var updateBtns= document.getElementsByClassName('update-cart')

/* event listener */
for(var i=0;i<updateBtns.length;i++)
{
	updateBtns[i].addEventListener('click', function(){
		var productId= this.dataset.product /* data-"product" */
		var action= this.dataset.action
		console.log('productId:', productId, 'action:', action) /* check by adding to cart */
	})
}