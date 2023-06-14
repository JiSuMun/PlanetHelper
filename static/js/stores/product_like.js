const likesForm = document.querySelector('#product_likes_form')
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value

likesForm.addEventListener('submit', function (event) {
  event.preventDefault()
  const storeId = event.target.dataset.storeId
  const productId = event.target.dataset.productId

  axios({
    method : 'post',
    url: `/stores/${storeId}/${productId}/likes/`,
    headers: {'X-CSRFToken': csrfToken},
  })
  .then((response) => {
    const isLiked = response.data.is_liked
    if (isLiked === true) {
      alert('WISH LIST에 추가되었습니다.')
    } else {
      alert('WISH LIST에서 삭제되었습니다.')
    }
  })
})
