const checkAll = document.getElementById('check_all')

checkAll.addEventListener('change', function() {
  const checkItems = document.querySelectorAll('input[name="item_check"]')
  checkItems.forEach(function(checkbox) {
    checkbox.checked = checkAll.checked
  })
})

const delBtn = document.getElementById('del_btn')

delBtn.addEventListener('click', function(e) {
  e.preventDefault()
  const confirmed = confirm("선택한 상품을 장바구니에서 삭제하시겠습니까?");
  
  if (confirmed) {
    const checkItems = document.querySelectorAll('input[name="item_check"]')
    const checkedItems = [...checkItems].filter((item) => item.checked)
    console.log(checkItems)
    console.log(checkedItems)

    if (isAuthenticated) {
      const productIds = checkedItems.map((item) => item.value)
      axios({
        method: 'POST',
        url: '/carts/remove_item/',
        headers: {'X-CSRFToken': csrfToken},
        data: JSON.stringify({
          productIds,
        })
      })
        .then(function(response) {
          window.location.href = '/carts/'
        })
    } else {

    }
  }
})