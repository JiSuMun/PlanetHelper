// swiper

var swiper = new Swiper(".mySwiper", {
  spaceBetween: 10,
  slidesPerView: 4,
  freeMode: true,
  watchSlidesProgress: true,
});
var swiper2 = new Swiper(".mySwiper2", {
  spaceBetween: 10,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  thumbs: {
    swiper: swiper,
  },
});


//  가격 수량 버튼
const incrementBtn = document.getElementById("increment_btn")
const decrementBtn = document.getElementById("decrement_btn")
const countDiv = document.getElementById("product_count")
const price = countDiv.dataset.productPrice
const subTotalPriceSpan = document.getElementById("sub_total_price")
const totalPriceSpan = document.getElementById("total_price")
const totalCount = document.getElementById("total_count")
const buyQuantity = document.querySelector("input[name='input_quantity']")

let count = 1
let subTotalPrice = price
let totalPrice = price

// + 버튼 클릭 시 count 숫자 증가
incrementBtn.addEventListener("click", () => {
  count++;
  countDiv.textContent = count
  totalCount.textContent = count
  buyQuantity.value = count

  subTotalPrice = count * price
  totalPrice = count * price

  console.log(subTotalPrice)
  console.log(totalPrice)

  subTotalPriceSpan.textContent = subTotalPrice.toLocaleString()
  totalPriceSpan.textContent = totalPrice.toLocaleString()
})

// - 버튼 클릭 시 count 숫자 감소
decrementBtn.addEventListener("click", () => {
  if (count > 1) { // 현재 숫자가 1보다 큰 경우에만 감소
    count--;
    countDiv.textContent = count
    totalCount.textContent = count
    buyQuantity.value = count

    subTotalPrice = count * price
    totalPrice = count * price

    subTotalPriceSpan.textContent = subTotalPrice.toLocaleString()
    totalPriceSpan.textContent = totalPrice.toLocaleString()
  }
})

// 리뷰 별
const ratingStars = document.querySelectorAll('.rating-star');

ratingStars.forEach((ratingStar) => {
  const rating = ratingStar.textContent;
  ratingStar.innerHTML = '';

  for (let i = 1; i <= 5; i++) {
    const star = document.createElement('i');
    star.classList.add('fas', 'fa-star');
    if (i > rating) {
      star.classList.remove('fas');
      star.classList.add('far');
    }
    ratingStar.appendChild(star);
  }
});

// 리뷰 좋아요 비동기
const reviewForms = document.querySelectorAll('.review-like-form');
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;


reviewForms.forEach((form) => {
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    const storeId = event.target.dataset.storeId;
    const productId = event.target.dataset.productId;
    const reviewId = event.target.dataset.reviewId;
       
    axios({
      method: "POST",
      url: `/stores/${storeId}/${productId}/${reviewId}/likes/`,
      headers: {'X-CSRFToken': csrftoken},
    })
      .then((response) => {
        const risLiked = response.data.r_is_liked;
        const rlikeBtn = document.querySelector(`#review-like-${reviewId}`)
        const rlikeCount = document.querySelector(`#review_likes_count-${reviewId}`)
        
        if (risLiked === true) {
          rlikeBtn.classList.add('r-like-color')
          rlikeBtn.classList.remove('r-like-color-gray')
        } else {
          rlikeBtn.classList.add('r-like-color-gray')
          rlikeBtn.classList.remove('r-like-color')

        }
        rlikeCount.innerText = response.data.review_likes_count;
      })
      .catch((error) => {
        console.log(error.response);
      });
  });
});

// 리뷰 싫어요 비동기
const dreviewForms = document.querySelectorAll('.review-dislike-form');

dreviewForms.forEach((form) => {
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    const storeId = event.target.dataset.storeId;
    const productId = event.target.dataset.productId;
    const dreviewId = event.target.dataset.dreviewId;
       
    axios({
      method: "POST",
      url: `/stores/${storeId}/${productId}/${dreviewId}/dislikes/`,
      headers: {'X-CSRFToken': csrftoken},
    })
      .then((response) => {
        const rdisLiked = response.data.r_is_disliked;
        const rdlikeBtn = document.querySelector(`#review-dislike-${dreviewId}`)
        const rdlikeCount = document.querySelector(`#review_dislikes_count-${dreviewId}`)
        
        if (rdisLiked === true) {
          rdlikeBtn.classList.add('r-like-color')
          rdlikeBtn.classList.remove('r-like-color-gray')
        } else {
          rdlikeBtn.classList.add('r-like-color-gray')
          rdlikeBtn.classList.remove('r-like-color')

        }
        rdlikeCount.innerText = response.data.review_dislikes_count;
      })
      .catch((error) => {
        console.log(error.response);
      });
  });
});